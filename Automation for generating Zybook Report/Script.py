import csv

sacctFileReader = open("/home/bibodijay/Desktop/CSC28/SacctReader.csv","r")
sacctReader = csv.reader(sacctFileReader)

sacctFileWriter = open("/home/bibodijay/Desktop/CSC28/gc_2178-CSC28DF-MASTER_fullgc_2017-09-25-11-15-47.csv","wb")
sacctWriter = csv.writer(sacctFileWriter, quoting=csv.QUOTE_ALL)
j = 0

for sacctData in sacctReader:
	if(j != 0):
		with open("/home/bibodijay/Desktop/CSC28/CSUSCSC28FletterFall2017_report_2017-09-25_1116.csv","r") as zybookFile:
			ff = csv.reader(zybookFile)			
			for data in ff:	
				if str(data[3][:-9]).lower() == str(sacctData[3]).lower():
					totalScore =  data[5]
					sacctData[11] = totalScore	
	
	sacctData_arr = str(sacctData)
	new_line = str.replace(sacctData_arr,'[','')
	new_line = str.replace(new_line,'\'','')
	sacctWriter.writerow(new_line.split(','))
	j += 1