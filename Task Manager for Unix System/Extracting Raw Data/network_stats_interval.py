import time
import subprocess
import re
import os

# stores transmitted bytes, [curr , prev]
curr_receivedBytes = 0.0
prev_receivedBytes = 0.0

# stores transmitted bytes, [curr , prev]
curr_transmitedBytes = 0.0
prev_transmitedBytes = 0.0

curr_activeOpens = 0
prev_activeOpens = 0
delta_activeOpens = 0

curr_currEsta = 0
prev_currEsta = 0
delta_currEsta = 0

while(1):
	snmpFile = open("/proc/net/snmp")
	devFile = open("/proc/net/dev")

	snmpdata = snmpFile.readlines()
	devData = devFile.readlines()

	i = 0	
	while(1):
		snmpRow = snmpdata[i]
		snmpRow = snmpRow.split()	
		if snmpRow[0] == "Tcp:":
			nextRow = snmpdata[i+1].split()
			
			curr_activeOpens = int(nextRow[5])
			curr_currEsta = int(nextRow[9])
	
			print('{0:<35} {1:15}'.format(snmpRow[5]+":",nextRow[5]))
			delta_activeOpens = curr_activeOpens - prev_activeOpens
			print('{0:<35} {1:0d}'.format("Change in Active Opens:",delta_activeOpens))
			print""
			
			print('{0:<35} {1:15}'.format(snmpRow[9]+":",nextRow[9]))
			delta_currEsta = (curr_currEsta + prev_currEsta)/2
			print('{0:<35} {1:0d}'.format("Average in Current Established:",delta_currEsta))
			print ""
			
			prev_activeOpens = curr_activeOpens
			prev_currEsta = curr_currEsta
			
			break;
		i = i + 1
		
	for arr in devData[2:]:
		devRow = arr.split()
		
		if devRow[0] != "lo:":
			
			curr_receivedBytes = float(devRow[1]) / 10**6
			curr_transmitedBytes = float(devRow[9]) / 10**6
						
			delta_receivedBytes = curr_receivedBytes - prev_receivedBytes
			delta_transmitedBytes = curr_transmitedBytes - prev_transmitedBytes
			
			#print ('{0:<35} {1:15.3} {2:10}'.format("Received Bytes:",round(curr_receivedBytes,3)," MB"))
			#print ('{0:<35} {1:15.3} {2:10}'.format("Transmitted Bytes:",round(curr_transmitedBytes,3)," MB"))
			#print ('{0:<35} {1:15.3} {2:10}'.format("Difference in bytes received:",round(delta_receivedBytes,3)," MB"))
			#print ('{0:<35} {1:15.3} {2:10}'.format("Difference in bytes transmitted:",round(delta_transmitedBytes,3)," MB"))
			
			o = open('output.txt','wb')
			subprocess.call(['ethtool',devRow[0][:-1]],stdout = o,stderr=subprocess.STDOUT)
			f = open('output.txt','r')
			
			for lines in f:
				values = lines.split()
				for i in values:
					if "Speed" in i:	
						max_bandwidth = float(values[1][:-4])/8
						#print ('{0:<35} {1:15.3} {2:10}'.format("Bandwidth:",round(max_bandwidth,3)," MBps"))
			
			utilization = (((delta_receivedBytes + delta_transmitedBytes)/5)*100) / max_bandwidth
			print('{0:<35} {1:5.3f} {2:5}'.format("Network Utilization:",round(utilization,3)," %"))
			
			prev_receivedBytes = curr_receivedBytes
			prev_transmitedBytes = 	curr_transmitedBytes
	time.sleep(5)
	os.system("clear")