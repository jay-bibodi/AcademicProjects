# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArchiveTable.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, subprocess, os, re
from datetime import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ArchiveTable(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self)
	
    def setupUi(self, ArchiveTable):
        ArchiveTable.setObjectName(_fromUtf8("ArchiveTable"))
        ArchiveTable.resize(764, 550)
	self.verticalLayout_2 = QtGui.QVBoxLayout(ArchiveTable)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
	self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.control_user_activities = QtGui.QTabWidget(ArchiveTable)
        self.control_user_activities.setGeometry(QtCore.QRect(0, 0, 900, 570))
        self.control_user_activities.setAccessibleName(_fromUtf8(""))
        self.control_user_activities.setObjectName(_fromUtf8("control_user_activities"))
	self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
	########### New ###############################		
	self.network_verticalLayout_3 = QtGui.QVBoxLayout(self.tab_3)
        self.network_verticalLayout_3.setObjectName(_fromUtf8("network_verticalLayout_3"))
        self.network_verticalLayout_4 = QtGui.QVBoxLayout()
        self.network_verticalLayout_4.setObjectName(_fromUtf8("network_verticalLayout_4"))
	self.network_enterValueToSearchLabel = QtGui.QLabel(self.tab_3)
        self.network_enterValueToSearchLabel.setObjectName(_fromUtf8("network_label"))
	self.network_verticalLayout_4.addWidget(self.network_enterValueToSearchLabel)
        self.network_horizontalLayout_For_LineEditSearchBox = QtGui.QHBoxLayout()
        self.network_horizontalLayout_For_LineEditSearchBox.setObjectName(_fromUtf8("network_horizontalLayout_For_LineEditSearchBox"))
        self.network_userName_SearchBox = QtGui.QLineEdit(self.tab_3)
        self.network_userName_SearchBox.setObjectName(_fromUtf8("network_userName_SearchBox"))
        self.network_horizontalLayout_For_LineEditSearchBox.addWidget(self.network_userName_SearchBox)
        self.network_processName_SearchBox = QtGui.QLineEdit(self.tab_3)
        self.network_processName_SearchBox.setObjectName(_fromUtf8("network_processName_SearchBox"))
        self.network_horizontalLayout_For_LineEditSearchBox.addWidget(self.network_processName_SearchBox)
        self.network_localAddress_SearchBox = QtGui.QLineEdit(self.tab_3)
        self.network_localAddress_SearchBox.setObjectName(_fromUtf8("network_localAddress_SearchBox"))
        self.network_horizontalLayout_For_LineEditSearchBox.addWidget(self.network_localAddress_SearchBox)
        self.network_remoteAddress_SearchBox = QtGui.QLineEdit(self.tab_3)
        self.network_remoteAddress_SearchBox.setObjectName(_fromUtf8("network_remoteAddress_SearchBox"))
        self.network_horizontalLayout_For_LineEditSearchBox.addWidget(self.network_remoteAddress_SearchBox)
        self.network_verticalLayout_4.addLayout(self.network_horizontalLayout_For_LineEditSearchBox)
	self.network_hitSearch = QtGui.QPushButton(self.tab_3)
	self.network_hitSearch.setObjectName(_fromUtf8("network_hitSearch"))
	self.network_verticalLayout_4.addWidget(self.network_hitSearch)
	self.network_main_Stacked_Widget = QtGui.QStackedWidget(self.tab_3)
        self.network_main_Stacked_Widget.setObjectName(_fromUtf8("network_main_Stacked_Widget"))
        self.network_stacked_widget_pageOne = QtGui.QWidget()
        self.network_stacked_widget_pageOne.setObjectName(_fromUtf8("network_stacked_widget_pageOne"))
        self.network_horizontalLayout_3 = QtGui.QHBoxLayout(self.network_stacked_widget_pageOne)
        self.network_horizontalLayout_3.setObjectName(_fromUtf8("network_horizontalLayout_3"))
        self.network_tableWidget = QtGui.QTableWidget(self.network_stacked_widget_pageOne)
        #self.tableWidget.setWordWrap(True)
	self.network_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.network_tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.network_tableWidget.setCornerButtonEnabled(True)
        self.network_tableWidget.setObjectName(_fromUtf8("network_tableWidget"))
        self.network_tableWidget.setColumnCount(4)
        self.network_tableWidget.setRowCount(0)
        network_item = QtGui.QTableWidgetItem()
        self.network_tableWidget.setHorizontalHeaderItem(0, network_item)
        network_item = QtGui.QTableWidgetItem()
        self.network_tableWidget.setHorizontalHeaderItem(1, network_item)
        network_item = QtGui.QTableWidgetItem()
        self.network_tableWidget.setHorizontalHeaderItem(2, network_item)
        network_item = QtGui.QTableWidgetItem()
        self.network_tableWidget.setHorizontalHeaderItem(3, network_item)
        self.network_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.network_tableWidget.horizontalHeader().setSortIndicatorShown(True)        
	self.network_tableWidget.horizontalHeader().setResizeMode(1)
	self.network_tableWidget.verticalHeader().hide()
        self.network_horizontalLayout_3.addWidget(self.network_tableWidget)
        self.network_main_Stacked_Widget.addWidget(self.network_stacked_widget_pageOne)
        self.network_verticalLayout_4.addWidget(self.network_main_Stacked_Widget)
	#self.backTofirstScreen = QtGui.QPushButton(self.tab_3)
	#self.backTofirstScreen.setObjectName(_fromUtf8("backTofirstScreen"))
	#self.verticalLayout_4.addWidget(self.backTofirstScreen)
	#self.backTofirstScreen.setFocusPolicy(QtCore.Qt.TabFocus)
	#self.backTofirstScreen.setFocus()
        self.network_verticalLayout_3.addLayout(self.network_verticalLayout_4)
	self.control_user_activities.addTab(self.tab_3, _fromUtf8(""))
	#################################################################################
        
	########### New ###################################################################	
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))	
	self.file_verticalLayout_3 = QtGui.QVBoxLayout(self.tab_4)
        self.file_verticalLayout_3.setObjectName(_fromUtf8("file_verticalLayout_3"))
        self.file_verticalLayout_4 = QtGui.QVBoxLayout()
        self.file_verticalLayout_4.setObjectName(_fromUtf8("file_verticalLayout_4"))
	self.file_enterValueToSearchLabel = QtGui.QLabel(self.tab_4)
        self.file_enterValueToSearchLabel.setObjectName(_fromUtf8("file_label"))
	self.file_verticalLayout_4.addWidget(self.file_enterValueToSearchLabel)
        self.file_horizontalLayout_For_LineEditSearchBox = QtGui.QHBoxLayout()
        self.file_horizontalLayout_For_LineEditSearchBox.setObjectName(_fromUtf8("file_horizontalLayout_For_LineEditSearchBox"))
        self.file_userName_SearchBox = QtGui.QLineEdit(self.tab_4)
        self.file_userName_SearchBox.setObjectName(_fromUtf8("file_userName_SearchBox"))
        self.file_horizontalLayout_For_LineEditSearchBox.addWidget(self.file_userName_SearchBox)
        self.file_processName_SearchBox = QtGui.QLineEdit(self.tab_4)
        self.file_processName_SearchBox.setObjectName(_fromUtf8("file_processName_SearchBox"))
        self.file_horizontalLayout_For_LineEditSearchBox.addWidget(self.file_processName_SearchBox)
        self.file_localAddress_SearchBox = QtGui.QLineEdit(self.tab_4)
        self.file_localAddress_SearchBox.setObjectName(_fromUtf8("file_localAddress_SearchBox"))
        self.file_horizontalLayout_For_LineEditSearchBox.addWidget(self.file_localAddress_SearchBox)
        self.file_remoteAddress_SearchBox = QtGui.QLineEdit(self.tab_4)
        self.file_remoteAddress_SearchBox.setObjectName(_fromUtf8("file_remoteAddress_SearchBox"))
        self.file_horizontalLayout_For_LineEditSearchBox.addWidget(self.file_remoteAddress_SearchBox)        
	self.file_verticalLayout_4.addLayout(self.file_horizontalLayout_For_LineEditSearchBox)
	self.file_hitSearch = QtGui.QPushButton(self.tab_4)
	self.file_hitSearch.setObjectName(_fromUtf8("file_hitSearch"))
	self.file_verticalLayout_4.addWidget(self.file_hitSearch)
	self.file_main_Stacked_Widget = QtGui.QStackedWidget(self.tab_4)
        self.file_main_Stacked_Widget.setObjectName(_fromUtf8("file_main_Stacked_Widget"))
        self.file_stacked_widget_pageOne = QtGui.QWidget()
        self.file_stacked_widget_pageOne.setObjectName(_fromUtf8("file_stacked_widget_pageOne"))
        self.file_horizontalLayout_3 = QtGui.QHBoxLayout(self.file_stacked_widget_pageOne)
        self.file_horizontalLayout_3.setObjectName(_fromUtf8("file_horizontalLayout_3"))
        self.file_tableWidget = QtGui.QTableWidget(self.file_stacked_widget_pageOne)
        self.file_tableWidget.setWordWrap(True)
	self.file_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.file_tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.file_tableWidget.setCornerButtonEnabled(False)
        self.file_tableWidget.setObjectName(_fromUtf8("file_tableWidget"))
        self.file_tableWidget.setColumnCount(4)
        self.file_tableWidget.setRowCount(0)
        file_item = QtGui.QTableWidgetItem()
        self.file_tableWidget.setHorizontalHeaderItem(0, file_item)
        file_item = QtGui.QTableWidgetItem()
        self.file_tableWidget.setHorizontalHeaderItem(1, file_item)
        file_item = QtGui.QTableWidgetItem()
        self.file_tableWidget.setHorizontalHeaderItem(2, file_item)
        file_item = QtGui.QTableWidgetItem()
        self.file_tableWidget.setHorizontalHeaderItem(3, file_item)
        self.file_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.file_tableWidget.horizontalHeader().setSortIndicatorShown(True)        
	#self.tableWidget.horizontalHeader().setResizeMode(1)
	#self.tableWidget.horizontalHeader().setHorizontalScrollBarPolicy(2)
	self.file_tableWidget.resizeColumnsToContents()
        self.file_tableWidget.verticalHeader().hide()
        self.file_horizontalLayout_3.addWidget(self.file_tableWidget)
        self.file_main_Stacked_Widget.addWidget(self.file_stacked_widget_pageOne)
        self.file_verticalLayout_4.addWidget(self.file_main_Stacked_Widget)

	#self.backTofirstScreen = QtGui.QPushButton(self.tab_4)
	#self.backTofirstScreen.setObjectName(_fromUtf8("backTofirstScreen"))
	#self.verticalLayout_4.addWidget(self.backTofirstScreen)
	#self.backTofirstScreen.setFocusPolicy(QtCore.Qt.TabFocus)
	#self.backTofirstScreen.setFocus()

        self.file_verticalLayout_3.addLayout(self.file_verticalLayout_4)
	self.control_user_activities.addTab(self.tab_4, _fromUtf8(""))
	####################################################################################


	self.verticalLayout.addWidget(self.control_user_activities)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ArchiveTable)
	# sets active tab
        self.control_user_activities.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ArchiveTable)

    def retranslateUi(self, ArchiveTable):
	ArchiveTable.setWindowTitle(_translate("ArchiveTable", "Archive Data", None))
        self.network_userName_SearchBox.setPlaceholderText(_translate("ArchiveTable", "User Name", None))
        self.network_processName_SearchBox.setPlaceholderText(_translate("ArchiveTable", "Process Name", None))
        self.network_localAddress_SearchBox.setPlaceholderText(_translate("ArchiveTable", "Local Address", None))
        self.network_remoteAddress_SearchBox.setPlaceholderText(_translate("ArchiveTable", "Remote Address", None))
	self.network_hitSearch.setText(_translate("ArchiveTable", "Submit Search Criteria", None))	
	self.network_enterValueToSearchLabel.setText(_translate("ArchiveTable", "Enter values to search:", None))	
        network_item = self.network_tableWidget.horizontalHeaderItem(0)
        network_item.setText(_translate("ArchiveTable", "User Name", None))
        network_item = self.network_tableWidget.horizontalHeaderItem(1)
        network_item.setText(_translate("ArchiveTable", "Process Name", None))
        network_item = self.network_tableWidget.horizontalHeaderItem(2)
        network_item.setText(_translate("ArchiveTable", "Local Address", None))
        network_item = self.network_tableWidget.horizontalHeaderItem(3)
        network_item.setText(_translate("ArchiveTable", "Remote Address", None))
	self.control_user_activities.setTabText(self.control_user_activities.indexOf(self.tab_3), _translate("ArchiveTable", "Network I/O Archive Data", None))
		
        self.file_userName_SearchBox.setPlaceholderText(_translate("ArchiveTable", "User Name", None))
        self.file_processName_SearchBox.setPlaceholderText(_translate("ArchiveTable", "Process Name", None))
        self.file_localAddress_SearchBox.setPlaceholderText(_translate("ArchiveTable", "Access Date & Time", None))
        self.file_remoteAddress_SearchBox.setPlaceholderText(_translate("ArchiveTable", "Path Name", None))
	self.file_hitSearch.setText(_translate("ArchiveTable", "Submit Search Criteria", None))	
	self.file_enterValueToSearchLabel.setText(_translate("ArchiveTable", "Enter values to search:", None))	
        file_item = self.file_tableWidget.horizontalHeaderItem(0)
        file_item.setText(_translate("ArchiveTable", "User Name", None))
        file_item = self.file_tableWidget.horizontalHeaderItem(1)
        file_item.setText(_translate("ArchiveTable", "Process Name", None))
        file_item = self.file_tableWidget.horizontalHeaderItem(2)
        file_item.setText(_translate("ArchiveTable", "Access Date & Time", None))
        file_item = self.file_tableWidget.horizontalHeaderItem(3)
        file_item.setText(_translate("ArchiveTable", "Path Name", None))
	self.control_user_activities.setTabText(self.control_user_activities.indexOf(self.tab_4), _translate("ArchiveTable", "File I/O Archive Data", None))

	self.filelogset = set()
        self.netlogset = set()

	self.fileCSVPath = "/home/bibodijay/Desktop/CSC239-GUI/Python/CSVFiles/fileLog.csv"
	self.networkCSVPath = "/home/bibodijay/Desktop/CSC239-GUI/Python/CSVFiles/networkLog.csv"
	
	self.dateTimeFormat = "%m/%d/%Y - %H:%M:%S"

    def loadRecordsFromCSVToDataStruct(self):	
	filelogList = []
        if os.path.isfile(self.fileCSVPath):
            with open(self.fileCSVPath, 'r') as filelog:
                filelogList = filelog.readlines()
        self.totalFileLogRecords = len(filelogList)
        for log in filelogList:
            record = log.strip()
            self.filelogset.add(record)

        networkLogList = []
        if os.path.isfile(self.networkCSVPath):
            with open(self.networkCSVPath, 'r') as networkLog:
                networkLogList = networkLog.readlines()
        self.totalNetworkLogRecords = len(networkLogList)
        for log in networkLogList:
            record = log.strip()
            self.netlogset.add(record)

    def createLogForFile(self,openFiles,isTimerUp,timerValueInMinutes):
	self.loadRecordsFromCSVToDataStruct()
	if isTimerUp == True:
		iSet = False
		self.addFileLogListToArchiveTable = []
		fileLogList = list(self.filelogset)
		length = len(fileLogList)
		i = 1
		while i < length:	
			fileLogi = fileLogList[i]	
			fileLogi = fileLogi[1:-1]
			colValuesi = fileLogi.split(",")			
			accessTimei = datetime.strptime(str(colValuesi[2].strip()[1:-1]),self.dateTimeFormat)
			j = 1
			while j < length:
				fileLogj = fileLogList[j]
				x = fileLogj[1:-1]
				colValuesj = x.split(",")
				if colValuesj[0]==colValuesi[0] and colValuesj[1]==colValuesi[1] and colValuesj[3]==colValuesi[3] and i!=j:  
					#accessTimej = colValuesj[2]
					accessTimej = datetime.strptime(str(colValuesj[2].strip()[1:-1]),self.dateTimeFormat)
					timeDiff = ""
					if (accessTimei - accessTimej) > (accessTimej-accessTimei):
						timeDiff = accessTimei - accessTimej
					else:
						timeDiff = accessTimej - accessTimei
					
					timeDiff = str(timeDiff)
					timeDiff = timeDiff.split(":")

					accessTime = 0
					if int(timeDiff[0]) != 0:
						accessTime = int(timeDiff[0])*60

					accessTime = accessTime + int(timeDiff[1]) + int(timeDiff[2])/60
	
					if accessTime > int(timerValueInMinutes): 
						#insert i
						self.addFileLogListToArchiveTable.append([colValuesi[0].strip()[1:-1],colValuesi[1].strip()[1:-1],colValuesi[2].strip()[1:-1],colValuesi[3].strip()[1:-1]])
						iSet = True
						break;
					else:
						fileLogList.remove(fileLogj) #remove j from the list
						length = len(fileLogList)
				j = j+1
			i = i+1
			if not iSet:
				self.addFileLogListToArchiveTable.append([colValuesi[0].strip()[1:-1],colValuesi[1].strip()[1:-1],colValuesi[2].strip()[1:-1],colValuesi[3].strip()[1:-1]])
			else:
				iSet = False			
		self.createTable(self.addFileLogListToArchiveTable,self.file_tableWidget)
	else:
		with open(self.fileCSVPath, 'a') as legacy_log:
			for row in openFiles:
				rowValue = str(tuple(row))
				if rowValue not in self.filelogset:
					self.filelogset.add(rowValue)
					legacy_log.write(rowValue+"\n")	 
	
    def createLogForNetwork(self,network_total_stats,isTimerUp,timerValueInMinutes):
	self.loadRecordsFromCSVToDataStruct()
	if isTimerUp == True:
		self.addNetworkLogListToArchiveTable = []
		networkLogList = list(self.netlogset)
		length = len(networkLogList)
		i = 1
		while i < length:	
			networkLogi = networkLogList[i]	
			networkLogi = networkLogi[1:-1]
			colValuesi = networkLogi.split(",")			
			self.addNetworkLogListToArchiveTable.append([colValuesi[0].strip()[1:-1],colValuesi[1].strip()[1:-1],colValuesi[2].strip()[1:-1],colValuesi[3].strip()[1:-1]])
				
		self.createTable(self.addNetworkLogListToArchiveTable,self.network_tableWidget)
	else:
		with open(self.networkCSVPath, 'a') as legacy_log:
			for row in network_total_stats:
				rowValue = str(tuple(row))
				if rowValue not in self.netlogset:
					self.netlogset.add(rowValue)
					legacy_log.write(rowValue+"\n")	

    def createTable(self,data,tableWidget):
	tableWidget.setSortingEnabled(False)
	tableWidget.setRowCount(len(data))
	for row in range(len(data)):
       		for column in range(4):
			userFileitem = QtGui.QTableWidgetItem(str(data[row][column]))
			tableWidget.setItem(row,column,userFileitem)		
	tableWidget.setSortingEnabled(True)
	tableWidget.resizeColumnsToContents()	
	tableWidget.horizontalHeader().setResizeMode(0)
	tableWidget.horizontalHeader().setStretchLastSection(True)

    #def validateSize(self,updatedArchiveData,isFromFile,timerInMinutes):
	#if isFromFile == True:		
	#	if(len(self.file_userName_SearchBox.text()) == 0 and len(self.file_processName_SearchBox.text()) == 0 and len(self.file_localAddress_SearchBox.text()) == 0 and len(self.file_remoteAddress_SearchBox.text()) == 0):
	#		self.getFilterResult(updatedArchiveData,self.file_tableWidget,self.file_userName_SearchBox,self.file_processName_SearchBox,self.file_localAddress_SearchBox,self.file_remoteAddress_SearchBox,timerInMinutes,isFromFile)
		#else:
		#	self.getFilterResult(updatedArchiveData,self.file_tableWidget,self.file_userName_SearchBox,self.file_processName_SearchBox,self.file_localAddress_SearchBox,self.file_remoteAddress_SearchBox)
	#else:
	#	if(len(self.network_userName_SearchBox.text()) == 0 and len(self.network_processName_SearchBox.text()) == 0 and len(self.network_localAddress_SearchBox.text()) == 0 and len(self.network_remoteAddress_SearchBox.text()) == 0):
	#		self.getFilterResult(updatedArchiveData,self.network_tableWidget,self.network_userName_SearchBox,self.network_processName_SearchBox,self.network_localAddress_SearchBox,self.network_remoteAddress_SearchBox,timerInMinutes,isFromFile)
		#else:
		#	self.getFilterResult(updatedArchiveData,self.network_tableWidget,self.network_userName_SearchBox,self.network_processName_SearchBox,self.network_localAddress_SearchBox,self.network_remoteAddress_SearchBox)


    #def getFilterResult(self,updatedArchiveData,tableWidget,userName,processName,localAddress,remoteAddress,timerInMinutes,isFromFile):
	#if isFromFile == True:
	#	self.createLogForFile("",True,timerInMinutes)
#		updatedArchiveData = self.addFileLogListToArchiveTable
	#else:
	#	self.createLogForNetwork("",True,timerInMinutes)
	#	updatedArchiveData = self.addNetworkLogListToArchiveTable
#
#	if userName.text() == "" and processName.text() == "" and localAddress.text() == "" and remoteAddress.text() == "":
#		self.createTable(updatedArchiveData,tableWidget)
#	else:
#		newList = []
#		processFilteredResult = []
#		localAddFilteredResult = []
#		remoteAddFilteredResult = []
#		
#		isRemoteAddressPresent = False
#		isLocalAddressPresent = False
#		isProcessNamePresent = False
#
#		if len(userName.text()) > 0:
#			for records in updatedArchiveData:
#				if re.search(str(userName.text()),str(records[0])):
#					newList.append(records)
#
#		if len(processName.text()) > 0:
#			processFilteredResult = [] 
#			
#			if newList != []:
#				processFilteredResult = newList
#			else:
#				processFilteredResult = updatedArchiveData
#
#			for records in processFilteredResult:
#				if re.search(str(processName.text()),str(records[1])):
#					processFilteredResult.append(records) 	
#			isProcessNamePresent = True
#
#		if len(localAddress.text()) > 0:
#			localAddFilteredResult = [] 
#
#			if processFilteredResult != []: 
#				localAddFilteredResult = processFilteredResult
#			elif newList != []: 
#				localAddFilteredResult = newList
#			else:
#				 localAddFilteredResult = updatedArchiveData
#
#			for records in localAddFilteredResult:
#				if re.search(str(localAddress.text()),str(records[2])):
#					localAddFilteredResult.append(records) 	
#			isLocalAddressPresent = True
#				
#
#		if len(remoteAddress.text()) > 0:
#			remoteAddFilteredResult = []
#
#			if localAddFilteredResult != []:
#				remoteAddFilteredResult = localAddFilteredResult
#			elif processFilteredResult != []:
#				remoteAddFilteredResult = processFilteredResult
#			elif newList != []:
#				remoteAddFilteredResult = newList
#			else:
#				remoteAddFilteredResult = updatedArchiveData
#
#
#			for records in remoteAddFilteredResult:
#				if re.search(str(remoteAddress.text()),str(records[3])):
#					remoteAddFilteredResult.append(records)
#			isRemoteAddressPresent = True
#
#		if isRemoteAddressPresent == True:
#			self.createTable(remoteAddFilteredResult,tableWidget)
#		elif isLocalAddressPresent == True:
#			self.createTable(localAddFilteredResult,tableWidget)
#		elif isProcessNamePresent == True:
#			self.createTable(processFilteredResult,tableWidget)
#		else:
#			self.createTable(newList,tableWidget)
#
		
if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_ArchiveTable()
	ex.show()
	sys.exit(app.exec_())
