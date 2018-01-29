import time
import os

diskReadsList = []
blockReadsList = []
diskWritesList = []
blockWritesList = []

prevDiskRead = 0
currDiskRead = 0

prevBlockRead = 0
currBlockRead = 0

prevDiskWrite = 0
currDiskWrite = 0

prevBlockWrite = 0
currBlockWrite = 0

deltaDiskRead = 0
deltaBlockRead = 0
deltaDiskWrite = 0
deltaBlockWrite = 0

while(1):

	diskIOStat = open("/proc/diskstats")	
	lines = diskIOStat.readlines()
	i = 0
	
	for arr in lines:
		
		sdaObj = arr.split()
		
		if "sd" in sdaObj[2]:  
			bool = any(char.isdigit() for char in sdaObj[2])
			
			if not bool:
				currDiskRead = int(sdaObj[3])
				currBlockRead = int(sdaObj[5])
				currDiskWrite = int(sdaObj[7])
				currBlockWrite = int(sdaObj[9])
			
				if len(diskReadsList)-1 >= i:
					prevDiskRead = diskReadsList.pop(0)
				else:	
					prevDiskRead = 0
				
				deltaDiskRead = currDiskRead - prevDiskRead	
					
				if len(blockReadsList)-1 >= i:
					prevBlockRead = blockReadsList.pop(0)
				else:
					prevBlockRead = 0
				
				deltaBlockRead = currBlockRead - prevBlockRead	
				
				if len(diskWritesList)-1 >= i:
					prevDiskWrite = diskWritesList.pop(0)
				else:
					prevDiskWrite = 0
					
				deltaDiskWrite = currDiskWrite - prevDiskWrite	
					
				if len(blockWritesList)-1 >= i:
					prevBlockWrite = blockWritesList.pop(0)
				else:
					prevBlockWrite = 0
					
				deltaBlockWrite = currBlockWrite - prevBlockWrite	
					
				print('{0:-^85}'.format(sdaObj[2]))
				print('{0:<25} {1:15d} {2:^25} {3:15d}'.format("Number of disk reads:",currDiskRead,",Change in # disk reads:",deltaDiskRead))
				print('{0:<25} {1:15d} {2:^25} {3:15d}'.format("Number of block reads:",currBlockRead,",Change in # block reads:",deltaBlockRead))
				print('{0:<25} {1:15d} {2:^25} {3:15d}'.format("Number of disk writes:",currDiskWrite,",Change in # disk writes:",deltaDiskWrite))
				print('{0:<25} {1:15d} {2:^25} {3:14d}'.format("Number of block writes:",currBlockWrite,",Change in # block writes:",deltaBlockWrite))
				
				diskReadsList.append(int(sdaObj[3]))
				blockReadsList.append(int(sdaObj[5]))
				diskWritesList.append(int(sdaObj[7]))
				blockWritesList.append(int(sdaObj[9]))
				i = i+1	
	time.sleep(5)
	os.system("clear")