import time
import subprocess
import os

process_id = raw_input("Please enter process id: \n")

# userTime[cpu,cpu0,cpu1,cpu2,...] each column will be filled when if cpu in statInfoLines[i] condition will be true
uTime_list = []

# userTime[cpu,cpu0,cpu1,cpu2,...]
sTime_list = []

# userTime[cpu,cpu0,cpu1,cpu2,...]
idleTime_list = []

curr_process_uTime = 0.0
prev_process_uTime = 0.0
delta_process_uTime = 0.0

curr_process_sTime = 0.0
prev_process_sTime = 0.0
delta_process_sTime = 0.0

curr_process_IdleTime = 0.0
prev_process_IdleTime = 0.0
delta_process_IdleTime = 0.0

#infinite loop
while(1):

	#open stat file to get cpu user time and cpu system time, interrupts and context swtich 
	statFile = open("/proc/"+process_id+"/stat")
	
	#open file meminfo to get total and available memory information
	memFile  = open("/proc/meminfo")

	# read all the lines in the file and return them in a list
	statInfoLines = statFile.readlines()
	memInfoLines = memFile.readlines()
	
	statInfoRow = statInfoLines[0].split()
	curr_process_uTime = float(statInfoRow[13])
	curr_process_sTime = float(statInfoRow[14])
	curr_process_IdleTime = float(statInfoRow[15]) + float(statInfoRow[16])	
			
	if len(uTime_list)-1 >= 0: 
		prev_process_uTime = uTime_list.pop(0)
	else:
		prev_process_uTime = 0.0
			
	delta_process_uTime = curr_process_uTime - prev_process_uTime
			
	if len(sTime_list)-1 >= 0:
		prev_process_sTime = sTime_list.pop(0)
	else:
		prev_process_sTime = 0.0
			
	delta_process_sTime = curr_process_sTime - prev_process_sTime
			
	if len(idleTime_list)-1 >= 0:
		prev_process_IdleTime = idleTime_list.pop(0)
	else:
		prev_process_IdleTime = 0.0
			
	delta_process_IdleTime = curr_process_IdleTime - prev_process_IdleTime
	
	###############################################################################################################################
	
	print('{0:-^70}'.format("PID: "+statInfoRow[0]+" CPU-STATS"))
	print('{0:<45} {1:15.2f} {2:10}'.format("Process spent time in User mode:",round(curr_process_uTime/100,2)," Seconds"))
	print('{0:<45} {1:15.2f} {2:10}'.format("Process spent time in System mode:",round(curr_process_sTime/100,2)," Seconds"))
	print('{0:<45} {1:15.2f} {2:10}'.format("Process spent time in Idle mode",round(curr_process_IdleTime/100,2)," Seconds"))
	
	#print('{0:<45} {1:15.2f} {2:10}'.format("Change in User mode:",round(delta_process_uTime/100,2)," Seconds"))
	#print('{0:<45} {1:15.2f} {2:10}'.format("Change in System mode:",round(delta_process_sTime/100,2)," Seconds"))
	#print('{0:<45} {1:15.2f} {2:10}'.format("Change in Idle mode:",round(delta_process_IdleTime/100,2)," Seconds"))
	
	try:
		overall_utilization = (((delta_process_uTime + delta_process_sTime) * 100) / (delta_process_uTime + delta_process_sTime + delta_process_IdleTime))
	except ZeroDivisionError:
		overall_utilization = 0.0
	
	uTime_list.append(curr_process_uTime)	
	sTime_list.append(curr_process_sTime)
	idleTime_list.append(curr_process_IdleTime)
	
	print('{0:<45} {1:15.2f} {2:10}'.format("Overall CPU Utilization:",round(overall_utilization,2)," %"))	
	
	################################################## For Virtual Memory #########################################################
	
	print('{0:-^70}'.format("Memory-STATS"))
	o = open('process_level.txt','wb')		
	subprocess.call(['uname','-m'],stdout = o,stderr=subprocess.STDOUT)
	f = open('process_level.txt','r')
	
	architecture = f.readline()
	#print architecture
	
	#clear file data
	open('process_level', 'w').close()
	
	if architecture == 'x86_64':
		architecture = 64
	else:
		architecture = 32

	#print('{0:<45} {1:15d}'.format("Architecture Type:",architecture))		
	
	# vsize is in bytes
	vsize = float(statInfoRow[22])	
	print('{0:<45} {1:15.3f} {2:10}'.format("Virtual Memory used by the process:",round((vsize/(10**6)),3)," MB"))	

	virtualMemoryUtilization = (vsize * 100) / (2**architecture)
	print('{0:<45} {1:15.3f} {2:10}'.format("Virtual Memory Utilization:",round(virtualMemoryUtilization,3)," %"))	
	
	################################################### For Physical memory #########################################################
	physicalMemoryInPage = statInfoRow[23]
	#print('{0:<45} {1:15} {2:10}'.format("Physical Memory:",physicalMemoryInPage," pages"))		
	
	o = open('process_level.txt','wb')		
	subprocess.call(['getconf','PAGESIZE'],stdout = o,stderr=subprocess.STDOUT)
	f = open('process_level.txt','r')
	
	pageSizeInBytes = f.readline()
	#print pageSizeInBytes
	
	#clear file data
	open('process_level', 'w').close()
	
	physicalMemorySizeInBytes = float(physicalMemoryInPage)*float(pageSizeInBytes)
	print('{0:<45} {1:15.3f} {2:10}'.format("Physical Memory:",round((physicalMemorySizeInBytes/(10**6)),3)," MB"))	
	
	memTotal = float(memInfoLines[0].split()[1])
	print('{0:<45} {1:15.3f} {2:10}'.format("Total Physical Memory in System:",round((memTotal/1000),3)," MB"))	

	physicalMemoryUtilization = (physicalMemorySizeInBytes/1000)*100 / memTotal
	print('{0:<45} {1:15.3f} {2:10}'.format("Physical Memory Utilization:",round(physicalMemoryUtilization,3)," %"))	
		
	time.sleep(5)
	os.system("clear")
	####################################################################################################################################