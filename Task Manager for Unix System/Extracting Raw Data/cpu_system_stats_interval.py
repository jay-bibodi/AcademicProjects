import time
import os

# userTime[cpu,cpu0,cpu1,cpu2,...] each column will be filled when if cpu in statInfoLines[i] condition will be true
userTime_list = []

# userTime[cpu,cpu0,cpu1,cpu2,...]
cpuTime_list = []

# userTime[cpu,cpu0,cpu1,cpu2,...]
idleTime_list = []

prev_usedMemory = 0.0

curr_CPU_UserTime = 0.0
prev_CPU_UserTime = 0.0
delta_CPU_UserTime = 0.0

curr_CPU_SysTime = 0.0
prev_CPU_SysTime = 0.0
delta_CPU_SysTime = 0.0

curr_CPU_IdleTime = 0.0
prev_CPU_IdleTime = 0.0
delta_CPU_IdleTime = 0.0

curr_interrupts = 0
prev_interrupts = 0
	
curr_ctxtSwtich = 0
prev_ctxtSwtich = 0

#infinite loop
while(1):

	#open stat file to get cpu user time and cpu system time, interrupts and context swtich 
	statFile = open("/proc/stat")
	
	#open file meminfo to get total and available memory information
	memFile  = open("/proc/meminfo")

	# read all the lines in the file and return them in a list
	statInfoLines = statFile.readlines()
	memInfoLines = memFile.readlines()
	
	#counter to iterate over all lines
	i = 0
	while(1):
		if "cpu" in statInfoLines[i]:
			statInfoRow = statInfoLines[i].split()
			curr_CPU_UserTime = float(statInfoRow[1])
			curr_CPU_SysTime = float(statInfoRow[3])
			curr_CPU_IdleTime = float(statInfoRow[4])	
			
			if len(userTime_list)-1 >= i: 
				prev_CPU_UserTime = userTime_list.pop(0)
			else:
				prev_CPU_UserTime = 0.0
			
			delta_CPU_UserTime = curr_CPU_UserTime - prev_CPU_UserTime
			
			if len(cpuTime_list)-1 >= i:
				prev_CPU_SysTime = cpuTime_list.pop(0)
			else:
				prev_CPU_SysTime = 0.0
			
			delta_CPU_SysTime = curr_CPU_SysTime - prev_CPU_SysTime
			
			if len(idleTime_list)-1 >= i:
				prev_CPU_IdleTime = idleTime_list.pop(0)
			else:
				prev_CPU_IdleTime = 0.0
			
			delta_CPU_IdleTime = curr_CPU_IdleTime - prev_CPU_IdleTime
				
			print('{0:-^70}'.format(statInfoRow[0]))
			print('{0:<40} {1:15.2f} {2:10}'.format("CPU Utilization in User mode:",round(float(statInfoRow[1])/100,2)," Seconds"))
			print('{0:<40} {1:15.2f} {2:10}'.format("CPU Utilization in System mode:",round(float(statInfoRow[3])/100,2)," Seconds"))
			
			overall_utilization = (((delta_CPU_UserTime + delta_CPU_SysTime) * 100) / (delta_CPU_UserTime + delta_CPU_SysTime + delta_CPU_IdleTime))
		
			userTime_list.append(curr_CPU_UserTime)	
			cpuTime_list.append(curr_CPU_SysTime)
			idleTime_list.append(curr_CPU_IdleTime)
			
			print('{0:<40} {1:15.2f} {2:10}'.format("Overall CPU Utilization:",round(overall_utilization,2)," %"))
		
		elif "intr" in statInfoLines[i]:
			print('{0:-^70}'.format("Interrupts"))
			
			interrupts = statInfoLines[i].split(" ")
			curr_interrupts = int(interrupts[1])
			total_interrupts = curr_interrupts - prev_interrupts
			
			print('{0:<40} {1:15d}'.format("# of interrupts:",curr_interrupts))
			print('{0:<40} {1:15d}'.format("Change in # of interrupts:",total_interrupts))
			
			prev_interrupts = curr_interrupts
		
		elif "ctxt" in statInfoLines[i]:
			print('{0:-^70}'.format("Context Swtich"))
			
			contextSwtich = statInfoLines[i].split(" ")
			curr_ctxtSwtich = int(contextSwtich[1])
			total_ctxtSwtich = curr_ctxtSwtich - prev_ctxtSwtich
			
			print('{0:<40} {1:15d}'.format("# of  Context Swtiches:",curr_ctxtSwtich))
			print('{0:<40} {1:15d}'.format("Change # of Context Swtiches:",total_ctxtSwtich))
			
			prev_ctxtSwtich = curr_ctxtSwtich
		else:
			break
		i = i+1
	
	memFree = memInfoLines[1].split()
	memTotal = memInfoLines[0].split()
	print('{0:-^70}'.format("Memory Info"))
	
	print('{0:<40} {1:15d} {2:10}'.format("Available memory:",(int(memFree[1])/1000)," MB"))
	print('{0:<40} {1:15d} {2:10}'.format("Total memory:",(int(memTotal[1])/1000)," MB"))
	
	curr_usedMemory = float(memTotal[1]) - float(memFree[1])
	average_Memory = (curr_usedMemory + prev_usedMemory) / 2
	prev_usedMemory = curr_usedMemory
	memUtilization = (average_Memory*100)/float(memTotal[1])		
	
	print('{0:<40} {1:15.3f} {2:10}'.format("Memory Utilization",round(memUtilization,3)," %"))
	time.sleep(5)
	os.system("clear")