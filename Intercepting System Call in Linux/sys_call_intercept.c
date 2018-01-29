#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/errno.h>
#include <linux/types.h>
#include <asm/current.h>
#include <linux/sched.h>
#include <linux/syscalls.h>
//#include <asm/system.h>
#include<linux/slab.h>
#include<linux/socket.h>
#include<linux/in.h>
#include<net/sock.h>
#include<linux/file.h>
#include<linux/net.h>
#include<linux/fdtable.h>
#include<linux/path.h>
#include <linux/proc_fs.h>	/* Necessary because we use the proc fs */
#include <asm/uaccess.h>	/* for copy_from_user */
#include <linux/mutex.h>

#define PROCFS_MAX_SIZE		1024
#define PROCFS1_NAME 		"blockedfile"
#define PROCFS2_NAME 		"blockednet"

MODULE_LICENSE("GPL");

char USER_NAME[7]="USRNAM\0";
char USER_TIME[11]="###:##:###";
char log_filename[11]="##_##_####";
unsigned long *syscall_table = (unsigned long *) 0xffffffff81601440;

//struct mutex my_mutex;

struct userNFile
{
	char userName[50];
	char fileName[100];
	char IP[30];
};

struct userNFile List[100];
unsigned int ListCount;

static struct proc_dir_entry *Our_Proc_File1;
static struct proc_dir_entry *Our_Proc_File2;

static char procfs_buffer[PROCFS_MAX_SIZE];
static unsigned long procfs_buffer_size = 0;

asmlinkage int (*original_write)(unsigned int, const char __user *, size_t);
asmlinkage size_t (*original_read)(int, char *, size_t);
asmlinkage int (*original_close)(unsigned int);
asmlinkage int (*original_open)(const char __user *, int, int);
asmlinkage int (*original_socketcall)(int call, unsigned long __user *args);
asmlinkage int (*original_getsockname)(int,struct sockaddr __user *,int *);
asmlinkage int (*original_getpeername)(int,struct sockaddr __user *,int *);
asmlinkage int (*original_fstat) (int,struct stat *);
asmlinkage long (*original_connect)(int, struct sockaddr __user *, int);
asmlinkage long (*original_accept)(int, struct sockaddr __user *, int __user *);
asmlinkage long (*original_sendto)(int, void __user *, size_t, unsigned,struct sockaddr __user *, int);
asmlinkage long (*original_recvfrom)(int, void __user *, size_t, unsigned, struct sockaddr __user *, int __user *);
asmlinkage int new_open(const char __user *, int, int);

void print_time(char char_time[]);
int get_username(char *);
void write_file(char *,char *);
char *inet_ntoa(struct in_addr inn);
short unsigned int my_ntoh(short unsigned int src_port);
void getfilename(char *pathname,struct files_struct *files,int fd);

int fileParsing(void);

asmlinkage size_t our_sys_write(int fd,char __user *buf,size_t count)
{
/*
	struct files_struct *files = current->files;
	struct file *file;
	char *pathname;
	
	char *tmp = (char *)__get_free_page(GFP_TEMPORARY);

	file = fcheck_files(files, fd);

	if(file == NULL)
	{	
		printk(KERN_ALERT "\nfcheck_files failed");
	}
	else
	{	
		if(!tmp){
			printk(KERN_ALERT "\ntmp not returned good");
		}
		else{
			pathname = d_path(&file->f_path,tmp,PAGE_SIZE);
			free_page((unsigned long)tmp);			
		}
	}
		
	long long offset = file->f_pos;
	char fileinfo_buff[200], path[120],tmp_count[100];
	int ret;
	
	print_time(USER_TIME); // Get Current Time
	strcpy(fileinfo_buff,USER_TIME+1); // Store Time in Log Array

	ret=get_username(USER_NAME);
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username in our_sys_write for file %s",pathname);}
	else
	{ strcat(fileinfo_buff,USER_NAME);}

	strcat(fileinfo_buff,"#Writing#");

	strcat(fileinfo_buff,pathname);
	snprintf(tmp_count,100,"#count=%d,pid=%d,fd=%d,offset=%ld#",count,current->pid,fd,offset);
	strcat(fileinfo_buff,tmp_count);
	strcat(fileinfo_buff,"\n");

	strcpy(path,"/home/vagrant/CSC239/OUTPUT/file");
	strcat(path,log_filename);

	if((USER_NAME[0]>='A' && USER_NAME[0]<='Z')||(USER_NAME[0]>='a' && USER_NAME[0]<='z'))
	{
		write_file(fileinfo_buff,path);
	}
	else
	{
		printk(KERN_ALERT "\nmissing write in file %s",pathname);		
	}
*/
	return original_write(fd,buf,count);
}

asmlinkage size_t our_sys_read(int fd,char __user *buf,size_t count)
{
	// printk("Read intercepted \n");
/*
	struct files_struct *files = current->files;
	struct file *file;
	char *pathname;
	
	char *tmp = (char *)__get_free_page(GFP_TEMPORARY);
//	printk("\n write intercepted");

	file = fcheck_files(files, fd);

	if(file == NULL)
	{	
		printk(KERN_ALERT "\nfcheck_files failed");
	}
	else
	{	
		if(!tmp){
		printk(KERN_ALERT "\ntmp not returned good");
		}
		else{
			pathname = d_path(&file->f_path,tmp,PAGE_SIZE);
					//printk("path name is %s",pathname);
			free_page((unsigned long)tmp);			
		}
	}
		
	long long offset = file->f_pos;
	char fileinfo_buff[200], path[120],tmp_count[100];
	int ret;
	
	print_time(USER_TIME); // Get Current Time
	strcpy(fileinfo_buff,USER_TIME+1); // Store Time in Log Array

	ret=get_username(USER_NAME);
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username in our_sys_write for file %s",pathname);}
	else
	{ strcat(fileinfo_buff,USER_NAME);}

	strcat(fileinfo_buff,"#Reading#");

	strcat(fileinfo_buff,pathname);
	snprintf(tmp_count,100,"#count=%d,pid=%d,fd=%d,offset=%ld#",count,current->pid,fd,offset);
	strcat(fileinfo_buff,tmp_count);
	strcat(fileinfo_buff,"\n");

	strcpy(path,"/home/vagrant/CSC239/OUTPUT/file");
	strcat(path,log_filename);

	if((USER_NAME[0]>='A' && USER_NAME[0]<='Z')||(USER_NAME[0]>='a' && USER_NAME[0]<='z'))
	{
		write_file(fileinfo_buff,path);
	}
	else
	{
		printk("\nmissing write in file %s",pathname);		
	}
*/	return original_read(fd,buf,count);
}

asmlinkage long new_connect(int fd, struct sockaddr __user *buff1, int flag)
{
/*	int ret, ret1, ret2,fc;
	struct sockaddr_in getsock, getpeer;
	struct sockaddr_in *getsock_p, *getpeer_p;
	int socklen;
	char netinfo_buff[200], path[120];
	char buff[100];
	socklen=sizeof(getsock);
	mm_segment_t old_fs=get_fs();
	set_fs(KERNEL_DS);
	ret1=original_getsockname(fd,(struct sockaddr *)&getsock,&socklen);
	getsock_p=&getsock;
	ret2=original_getpeername(fd,(struct sockaddr *)&getpeer,&socklen);
	getpeer_p=&getpeer;
	set_fs(old_fs);
	printk("\nret1 is %d %d",ret1, ret2);
	if(getsock.sin_family==2)
	{
	print_time(USER_TIME);
	strcpy(netinfo_buff,USER_TIME+1);
	ret=get_username(USER_NAME);
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username");}
	else
	{ strcat(netinfo_buff,USER_NAME);}
	snprintf(buff,9,"#%s","Connect");
	strcat(netinfo_buff,buff);
	snprintf(buff,18, "#%s",inet_ntoa(getsock.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u",my_ntoh(getsock.sin_port));
	strcat(netinfo_buff,buff);
	snprintf(buff,18,"#%s",inet_ntoa(getpeer.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u\n",my_ntoh(getpeer.sin_port));
	strcat(netinfo_buff,buff);
	strcpy(path,"/home/vagrant/CSC239/OUTPUT/file");
	strcat(path,log_filename);
	write_file(netinfo_buff,path);
	}
*/	return original_connect(fd,buff1,flag);
}

asmlinkage long new_accept(int fd, struct sockaddr __user *buff1, int __user *buff2)
{
/*	int ret, ret1, ret2;
	struct sockaddr_in getsock, getpeer;
	struct sockaddr_in *getsock_p, *getpeer_p;
	int socklen;
	char netinfo_buff[200], path[120];
	char buff[100];
	socklen=sizeof(getsock);
	mm_segment_t old_fs=get_fs();
	set_fs(KERNEL_DS);
	ret1=original_getsockname(fd,(struct sockaddr *)&getsock,&socklen);
	getsock_p=&getsock;
	ret2=original_getpeername(fd,(struct sockaddr *)&getpeer,&socklen);

	getpeer_p=&getpeer;
	set_fs(old_fs);
	printk("\nret1 is %d %d",ret1, ret2);
	if(getsock.sin_family==2)
	{
	print_time(USER_TIME);
	strcpy(netinfo_buff,USER_TIME+1);
	ret=get_username(USER_NAME);
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username");}
	else
	{ strcat(netinfo_buff,USER_NAME);}
	snprintf(buff,8,"#%s","Accept");
	strcat(netinfo_buff,buff);
	snprintf(buff,18, "#%s",inet_ntoa(getsock.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u",my_ntoh(getsock.sin_port));
	strcat(netinfo_buff,buff);
	snprintf(buff,18,"#%s",inet_ntoa(getpeer.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u\n",my_ntoh(getpeer.sin_port));
	strcat(netinfo_buff,buff);
	strcpy(path,"/home/vagrant/CSC239/OUTPUT/file");
	strcat(path,log_filename);
	write_file(netinfo_buff,path);
	}
*/	return original_accept(fd,buff1,buff2);
}

asmlinkage long new_sendto(int fd, void __user *buff1, size_t len, unsigned flags, struct sockaddr __user *addr, int addr_len)
{
/*	int ret, ret1, ret2;
	struct sockaddr_in getsock, getpeer;
	struct sockaddr_in *getsock_p, *getpeer_p;
	int socklen;
	char netinfo_buff[200], path[120];
	char buff[100];
	socklen=sizeof(getsock);
	mm_segment_t old_fs=get_fs();
	set_fs(KERNEL_DS);
	ret1=original_getsockname(fd,(struct sockaddr *)&getsock,&socklen);
	getsock_p=&getsock;
	ret2=original_getpeername(fd,(struct sockaddr *)&getpeer,&socklen);
	getpeer_p=&getpeer;
	set_fs(old_fs);
	printk("\nret1 is %d %d",ret1, ret2);
	if(getsock.sin_family==2)
	{
	printk("Hi\n");
	print_time(USER_TIME);
	strcpy(netinfo_buff,USER_TIME+1);
	ret=get_username(USER_NAME);
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username");}
	else
	{ strcat(netinfo_buff,USER_NAME);}
	snprintf(buff,8,"#%s","SEND");
	strcat(netinfo_buff,buff);
	snprintf(buff,18, "#%s",inet_ntoa(getsock.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u",my_ntoh(getsock.sin_port));
	strcat(netinfo_buff,buff);
	snprintf(buff,18,"#%s",inet_ntoa(getpeer.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u\n",my_ntoh(getpeer.sin_port));
	strcat(netinfo_buff,buff);
	strcpy(path,"/home/vagrant/CSC239/OUTPUT/file");
	strcat(path,log_filename);
	write_file(netinfo_buff,path);
	}
*/	return original_sendto(fd,buff1,len,flags,addr,addr_len);
}

asmlinkage long new_recvfrom(int fd, void __user *buff1, size_t len, unsigned flags, struct sockaddr __user *ar, int
__user *buff2)
{
/*	int ret, ret1, ret2,fc;
	struct sockaddr_in getsock, getpeer;
	struct sockaddr_in *getsock_p, *getpeer_p;
	int socklen;
	char netinfo_buff[200], path[120];
	char buff[100];
	socklen=sizeof(getsock);
	mm_segment_t old_fs=get_fs();
	set_fs(KERNEL_DS);
	ret1=original_getsockname(fd,(struct sockaddr *)&getsock,&socklen);
	getsock_p=&getsock;
	ret2=original_getpeername(fd,(struct sockaddr *)&getpeer,&socklen);
	getpeer_p=&getpeer;
	set_fs(old_fs);
	printk("\nret1 is %d %d",ret1, ret2);
	if(getsock.sin_family==2)
	{
	printk("Hi\n");
	print_time(USER_TIME);
	strcpy(netinfo_buff,USER_TIME+1);
	ret=get_username(USER_NAME);
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username");}
	else
	{ strcat(netinfo_buff,USER_NAME);}
	snprintf(buff,9,"#%s","RECEIVE");
	strcat(netinfo_buff,buff);
	snprintf(buff,18, "#%s",inet_ntoa(getsock.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u",my_ntoh(getsock.sin_port));
	strcat(netinfo_buff,buff);
	snprintf(buff,18,"#%s",inet_ntoa(getpeer.sin_addr));
	strcat(netinfo_buff,buff);
	snprintf(buff,10,"#%u\n",my_ntoh(getpeer.sin_port));
	strcat(netinfo_buff,buff);
	strcpy(path,"/home/vagrant/CSC239/OUTPUT/network");
	strcat(path,log_filename);
	write_file(netinfo_buff,path);
	}
*/	return (*original_recvfrom)(fd,buff1,len,flags,ar,buff2);
}

asmlinkage int new_open(const char __user *filename, int flags, int mode)
{
	char fileinfo_buff[200], path[120];
	char username[7] = "USERNA\0";
	int ret;
	int i = 0;
	
	//return (*original_open)(filename, flags, mode);

	//mutex_lock(&my_mutex);
	ret=get_username(USER_NAME);
	
	while(i != ListCount)
	{
		int d1 = strcmp(USER_NAME,List[i].userName);
		int d2 = strcmp(filename, List[i].fileName);
		if((d1 == 0) && (d2 == 0))
		{
			printk("the matched username is %s and filename is %s\n",USER_NAME,filename);
			break;
		}		
		i++;
	}
	
	if(i == ListCount)
	{
		//mutex_unlock(&my_mutex);
		
		return (*original_open)(filename, flags, mode);
	}

	print_time(USER_TIME); // Get Current Time
	strcpy(fileinfo_buff,USER_TIME+1); // Store Time in Log Array
	if(ret < 0)
	{ printk(KERN_ALERT "\n error in get_username in new_open for file %s",filename);}
	else
	{ strcat(fileinfo_buff,USER_NAME);}

	if(flags & (O_WRONLY|O_APPEND))
	{
	strcat(fileinfo_buff,"#WR#");
	}
	else
	{
	strcat(fileinfo_buff,"#RD#");
	}

	strcat(fileinfo_buff,filename);
	strcat(fileinfo_buff,"\n");
	strcpy(path,"/proc/blockedfile");
	//strcat(path,log_filename);

	if((USER_NAME[0]>='A' && USER_NAME[0]<='Z')||(USER_NAME[0]>='a' && USER_NAME[0]<='z'))
	{
	write_file(fileinfo_buff,path);
	}
	else
	{
	printk("missing write in file %s\n",filename);		
	}
	//mutex_lock(&my_mutex);
	return EACCES; 
	
}

//HELPER FUNCTIONS

void write_file(char *buffer,char *path)
{
	mm_segment_t old_fs;
	int fd;
	old_fs=get_fs();
	set_fs(KERNEL_DS);
	fd = original_open(path, O_WRONLY|O_APPEND,0777);
	// printk(cd " %d %s",fd,buffer);

	if(fd >= 0)
	{
		original_write(fd,buffer,strlen(buffer));
		original_close(fd);
		printk("Writing into %s with %s\n", path, buffer);
	}
	else
	{
		printk(KERN_ALERT "\n Errro in write_file() while opening a file with fd =%d",fd);
	}
	set_fs(old_fs);
	return;
}

short unsigned int my_ntoh(short unsigned int src_port)
{
	short unsigned int t,t1,t2;
	t = (src_port >> 8);
	t1 = (src_port << 8);
	t2 = t|t1;
	return(t2);
}

char *inet_ntoa(struct in_addr inn)
{
	static char m[18];
	register char *m1;
	m1 = (char *)&inn;
	#define UCC(m) (((int)m)&0xff)
	(void)snprintf(m, sizeof(m),"%u.%u.%u.%u", UCC(m1[0]), UCC(m1[1]), UCC(m1[2]), UCC(m1[3]));
	return(m);
}

void print_time(char char_time[])
{
	struct timeval my_tv;
	int sec, hr, min, tmp1, tmp2;
	int days,years,days_past_currentyear;
	int i=0,month=0,date=0;
	unsigned long get_time;
	char_time[11]="#00:00:00#";
	do_gettimeofday(&my_tv); // Get System Time From Kernel Mode
	get_time = my_tv.tv_sec; // Fetch System time in Seconds
	// printk(KERN_ALERT "\n %ld",get_time);
	get_time = get_time + 43200;
	sec = get_time % 60; // Convert into Seconds
	tmp1 = get_time / 60;
	min = tmp1 % 60; // Convert into Minutes
	tmp2 = tmp1 / 60;
	hr = (tmp2+4) % 24; // Convert into Hours
	hr=hr+1;
	char_time[1]=(hr/10)+48; // Convert into Char from Int
	char_time[2]=(hr%10)+48;
	char_time[4]=(min/10)+48;
	char_time[5]=(min%10)+48;
	char_time[7]=(sec/10)+48;
	char_time[8]=(sec%10)+48;
	char_time[10]='\0';
	/* calculating date from time in seconds */
	days = (tmp2+4)/24;
	days_past_currentyear = days % 365;
	years = days / 365;
	for(i=1970;i<=(1970+years);i++)
	{
	if ((i % 4) == 0)
	days_past_currentyear--;
	}
	if((1970+years % 4) != 0)
	{
	if(days_past_currentyear >=1 && days_past_currentyear <=31)
	{
	month=1; //JAN
	date = days_past_currentyear;
	}
	else if (days_past_currentyear >31 && days_past_currentyear <= 59)
	{
	month = 2;
	date = days_past_currentyear - 31;
	}
	else if (days_past_currentyear >59 && days_past_currentyear <= 90)
	{
	month = 3;
	date = days_past_currentyear - 59;
	}
	else if (days_past_currentyear >90 && days_past_currentyear <= 120)
	{
	month = 4;
	date = days_past_currentyear - 90;
	}
	else if (days_past_currentyear >120 && days_past_currentyear <= 151)
	{
	month = 5;
	date = days_past_currentyear - 120;
	}
	else if (days_past_currentyear >151 && days_past_currentyear <= 181)
	{
	month = 6;
	date = days_past_currentyear - 151;
	}
	else if (days_past_currentyear >181 && days_past_currentyear <= 212)
	{
	month = 7;
	date = days_past_currentyear - 181;
	}
	else if (days_past_currentyear >212 && days_past_currentyear <= 243)
	{
	month = 8;
	date = days_past_currentyear - 212;
	}
	else if (days_past_currentyear >243 && days_past_currentyear <= 273)
	{
	month = 9;
	date = days_past_currentyear - 243;
	}
	else if (days_past_currentyear >273 && days_past_currentyear <= 304)
	{
	month = 10;
	date = days_past_currentyear - 273;
	}
	else if (days_past_currentyear >304 && days_past_currentyear <= 334)
	{
	month = 11;
	date = days_past_currentyear - 304;
	}
	else if (days_past_currentyear >334 && days_past_currentyear <= 365)
	{
	month = 12;
	date = days_past_currentyear - 334;
	}
	// printk(KERN_ALERT "month=%d date=%d year=%d",month,date,(1970+years));
	}
	// for leap years..
	else
	{
	if(days_past_currentyear >=1 && days_past_currentyear <=31)
	{
	month=1; //JAN
	date = days_past_currentyear;
	}
	else if (days_past_currentyear >31 && days_past_currentyear <= 60)
	{
	month = 2;
	date = days_past_currentyear - 31;
	}
	else if (days_past_currentyear >60 && days_past_currentyear <= 91)
	{
	month = 3;
	date = days_past_currentyear - 60;
	}
	else if (days_past_currentyear >91 && days_past_currentyear <= 121)
	{
	month = 4;
	date = days_past_currentyear - 91;
	}
	else if (days_past_currentyear >121 && days_past_currentyear <= 152)
	{
	month = 5;
	date = days_past_currentyear - 121;
	}
	else if (days_past_currentyear >152 && days_past_currentyear <= 182)
	{
	month = 6;
	date = days_past_currentyear - 152;
	}
	else if (days_past_currentyear >182 && days_past_currentyear <= 213)
	{
	month = 7;
	date = days_past_currentyear - 182;
	}
	else if (days_past_currentyear >213 && days_past_currentyear <= 244)
	{
	month = 8;
	date = days_past_currentyear - 213;
	}
	else if (days_past_currentyear >244 && days_past_currentyear <= 274)
	{
	month = 9;
	date = days_past_currentyear - 244;
	}
	else if (days_past_currentyear >274 && days_past_currentyear <= 305)
	{
	month = 10;
	date = days_past_currentyear - 274;
	}
	else if (days_past_currentyear >305 && days_past_currentyear <= 335)
	{
	month = 11;
	date = days_past_currentyear - 305;
	}
	else if (days_past_currentyear >335 && days_past_currentyear <= 366)
	{
	month = 12;
	date = days_past_currentyear - 335;
	}
	// printk(KERN_ALERT "\nmonth=%d date=%d year=%d",month,date,(1970+years));
	}
	log_filename[0]=(month/10)+48; // Convert into Char from Int
	log_filename[1]=(month%10)+48;
	log_filename[3]=(date/10)+48;
	log_filename[4]=(date%10)+48;
	tmp1 = ((1970+years) % 10) + 48;
	log_filename[9]= tmp1;
	tmp1 = (1970+years)/ 10;
	tmp2 = tmp1 % 10;
	log_filename[8]= tmp2 + 48;
	tmp1 = tmp1 / 10;
	tmp2 = tmp1 % 10;
	log_filename[7]=tmp2 + 48;
	tmp1 = tmp1 / 10;
	log_filename[6]= tmp1+48;
	log_filename[10]='\0';
}

void getfilename(char *pathname,struct files_struct *files,int fd ){
	char *tmp;
	struct file *file;
	struct path *path;

	spin_lock(&files->file_lock);
	file = fcheck_files(files, fd);
	if (!file) {
	    spin_unlock(&files->file_lock);
	    return -ENOENT;
	}

	path = &file->f_path;
	path_get(path);
	spin_unlock(&files->file_lock);

	tmp = (char *)__get_free_page(GFP_TEMPORARY);

	if (!tmp) {
	    path_put(path);
	    return -ENOMEM;
	}

	pathname = d_path(path, tmp, PAGE_SIZE);
	path_put(&path);

	if (IS_ERR(pathname)) {
	    free_page((unsigned long)tmp);
	    return PTR_ERR(pathname);
	}

	/* do something here with pathname */

	free_page((unsigned long)tmp);
}

int get_username(char *name)
{
	char *read_buff,*path,*tk,*tk1;
	char tmp_buff[12];
	int fd,ret,my_i,error=0;
	mm_segment_t old_fs_username;

	read_buff = (char *)kmalloc(2024,GFP_ATOMIC);
	if(!read_buff){
	printk(KERN_ALERT "\n kmalloc error");
	return -1;
	}

	path = (char *)kmalloc(120,GFP_ATOMIC);
	if(!path){
	printk(KERN_ALERT "\n kmalloc error for path");
	return -1;
	}

	strcpy(path,"/proc/");
	snprintf(tmp_buff,12,"%u",current->pid);
	strcat(path,tmp_buff);
	strcat(path,"/environ");

	old_fs_username = get_fs();
	set_fs(KERNEL_DS);

	fd = original_open(path, O_RDONLY|O_LARGEFILE,0700); // Original Stolenaddress of sys_open system call
	if(fd < 0){
		printk(KERN_ALERT "\n error in sys_open in get_username function");
		error = -1;
		goto my_error;
	}
	else{
		if((ret=original_read(fd,read_buff,2024)) < 0){
		printk(KERN_ALERT "\nError in sys_read in get_username function");
		error = -1;
		goto my_error;
            	}
		else{
			for(my_i=0;my_i<ret;my_i++){
				if(read_buff[my_i] == '\0')
				read_buff[my_i] = ' ';
			}
			read_buff[ret-1] = '\0';
			
			tk = strstr(read_buff,"USER=");
			//printk("\ntk is %s",tk);
			if(!tk){
			//printk(KERN_ALERT "Error in strstr");
			error = -1;
			goto my_error;
			}
			tk1 = strsep(&tk," ");
			tk1 = tk1+5;
			strncpy(name,tk1,strlen(tk1));
			//printk("\nname is %s",name);
		     }
		original_close(fd);
	}
	my_error:
	set_fs(old_fs_username);
	kfree(read_buff);
	kfree(path);
	return error;
}

int len,temp;
char *msg1;
char *msg2;

int read_proc1(struct file *filp,char *buf,size_t count,loff_t *offp ) 
{
	if(count>temp)
	{
		count=temp;
	}
	temp=temp-count;
	copy_to_user(buf,msg1, count);
	if(count==0)
		temp=len;
   
	return count;
}

int write_proc1(struct file *filp,const char *buf,size_t count,loff_t *offp)
{
	copy_from_user(msg1,buf,count);
	len=count;
	temp=len;
	return count;
}

int read_proc2(struct file *filp,char *buf,size_t count,loff_t *offp ) 
{
	if(count>temp)
	{
		count=temp;
	}
	temp=temp-count;
	copy_to_user(buf,msg2, count);
	if(count==0)
		temp=len;
   
	return count;
}

int write_proc2(struct file *filp,const char *buf,size_t count,loff_t *offp)
{
	copy_from_user(msg2,buf,count);
	len=count;
	temp=len;
	return count;
}
struct file_operations proc_fops1 = {
	read: read_proc1,
	write: write_proc1
};

struct file_operations proc_fops2 = {
	read: read_proc2,
	write: write_proc2
};

void create_new_proc_entry(void)  //use of void for no arguments is compulsory now 
{
	proc_create(PROCFS1_NAME,O_RDWR|O_APPEND|O_LARGEFILE,NULL,&proc_fops1);
	proc_create(PROCFS2_NAME,O_RDWR|O_APPEND|O_LARGEFILE,NULL,&proc_fops2);
	msg1=kmalloc(2000*sizeof(char),GFP_KERNEL);
	msg2=kmalloc(2000*sizeof(char),GFP_KERNEL);
}

//pases file and populates the data structure
int fileParsing(void) 
{
	mm_segment_t old_fs;
	old_fs= get_fs();
	set_fs(KERNEL_DS);

	char c;		//temp character to put into buffer 
	int i = 0;	//offset into name
	int UserNameMode = 0; 	//expecting user name
	int iList = 0;

	int fd = original_open("/home/vagrant/test", O_RDWR|O_LARGEFILE,0700);
	if(fd < 0)
		return -1;

	while(1)
	{
		ssize_t temp = original_read(fd, &c, 1);
		if(temp == 0)	//finish parsing for this file
		   break;
		else if(c == '\n'){	//finish parsing one entry
		   List[iList].IP[i] = '\0';
		   iList++;
		   UserNameMode = 0;	//will expect user name next time
		   i = 0;
		}
		else if(c == ','){
		  	if(UserNameMode == 0){
				UserNameMode = 1;
				List[iList].userName[i] = '\0';
		  	}
		  	else if(UserNameMode == 1){
				UserNameMode = 2;
				List[iList].fileName[i] = '\0';
		  	}
		  	else{	//Should not come : error condition
				return -1;
		  	}
		  	i = 0;
		}		
		else{
			if(UserNameMode == 0)
				List[iList].userName[i] = c;
			else if(UserNameMode == 1)
				List[iList].fileName[i] = c;
			else
				List[iList].IP[i] = c;
			i++;
		}		   
	}
	set_fs(old_fs);	
	ListCount = iList+1;
	return 0; 
}

static int init(void)
{
	printk("\n******************************************Module starting...***************************************\n");
	
	create_new_proc_entry();
	printk(KERN_INFO "/proc/files reated\n");

	//mutex_init(&my_mutex);
	write_cr0 (read_cr0 () & (~ 0x10000));
	original_write= (void *)syscall_table[__NR_write];
	original_read=(void *)syscall_table[__NR_read];
	original_close=(void *)syscall_table[__NR_close];
	original_open=(void *)syscall_table[__NR_open];
	original_getsockname=(void *)syscall_table[__NR_getsockname];
	original_getpeername=(void *)syscall_table[__NR_getpeername];
	original_fstat=(void *)syscall_table[__NR_fstat];
	original_connect=(void *)syscall_table[__NR_connect];
	original_accept=(void *)syscall_table[__NR_accept];
	original_sendto=(void *)syscall_table[__NR_sendto];
	original_recvfrom=(void *)syscall_table[__NR_recvfrom];
	//original_readlink=(void *)syscall_table[__NR_readlink];

	syscall_table[__NR_open]=new_open;
	syscall_table[__NR_write]=our_sys_write;
	syscall_table[__NR_read]=our_sys_read;
	syscall_table[__NR_sendto]=new_sendto;
	syscall_table[__NR_recvfrom]=new_recvfrom;
	syscall_table[__NR_connect]=new_connect;
	syscall_table[__NR_accept]=new_accept;
	write_cr0 (read_cr0 () | 0x10000);

	int i = fileParsing();
	for(i = 0; i < ListCount; i++)
		printk(" Entry No. %d is %s,%s,%s\n", i, List[i].userName, List[i].fileName, List[i].IP);

	return 0;
}

static void exit(void)
{
	remove_proc_entry(PROCFS1_NAME, NULL);
	remove_proc_entry(PROCFS2_NAME, NULL);

	write_cr0 (read_cr0 () & (~ 0x10000));
	syscall_table[__NR_open]=original_open;
	syscall_table[__NR_write]=original_write;
	syscall_table[__NR_read]=original_read;
	syscall_table[__NR_sendto]=original_sendto;
	syscall_table[__NR_recvfrom]=original_recvfrom;
	syscall_table[__NR_connect]=original_connect;
	syscall_table[__NR_accept]=original_accept;
	write_cr0 (read_cr0 () | 0x10000);
	printk("**********************************************Module exiting*********************************************\n");
	return;
}

module_init(init);
module_exit(exit);
