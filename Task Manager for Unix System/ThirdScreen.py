# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FourthScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os, datetime, re
from archiveTable import Ui_ArchiveTable

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

class Ui_File_IO_Form(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self) 	

    def setupUi(self, File_IO_Form):
        File_IO_Form.setObjectName(_fromUtf8("File_IO_Form"))
        File_IO_Form.setGeometry(100,60,800,500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(File_IO_Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.main_verticalLayout = QtGui.QVBoxLayout()
        self.main_verticalLayout.setObjectName(_fromUtf8("main_verticalLayout"))
	#################	
	self.enterValueToSearchLabel = QtGui.QLabel(File_IO_Form)
        self.enterValueToSearchLabel.setObjectName(_fromUtf8("label"))
	self.main_verticalLayout.addWidget(self.enterValueToSearchLabel)
	#################
        self.horizontalLayout_For_LineEditSearchBox = QtGui.QHBoxLayout()
        self.horizontalLayout_For_LineEditSearchBox.setObjectName(_fromUtf8("horizontalLayout_For_LineEditSearchBox"))
        self.userName_SearchBox = QtGui.QLineEdit(File_IO_Form)
        self.userName_SearchBox.setObjectName(_fromUtf8("userName_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.userName_SearchBox)
        self.processName_SearchBox = QtGui.QLineEdit(File_IO_Form)
        self.processName_SearchBox.setObjectName(_fromUtf8("processName_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.processName_SearchBox)
        self.localAddress_SearchBox = QtGui.QLineEdit(File_IO_Form)
        self.localAddress_SearchBox.setObjectName(_fromUtf8("localAddress_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.localAddress_SearchBox)
        self.remoteAddress_SearchBox = QtGui.QLineEdit(File_IO_Form)
        self.remoteAddress_SearchBox.setObjectName(_fromUtf8("remoteAddress_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.remoteAddress_SearchBox)        
	self.main_verticalLayout.addLayout(self.horizontalLayout_For_LineEditSearchBox)
	######################        
	self.hitSearch = QtGui.QPushButton(File_IO_Form)
	self.hitSearch.setObjectName(_fromUtf8("hitSearch"))
	self.main_verticalLayout.addWidget(self.hitSearch)
	########################
	self.main_Stacked_Widget = QtGui.QStackedWidget(File_IO_Form)
        self.main_Stacked_Widget.setObjectName(_fromUtf8("main_Stacked_Widget"))
        self.stacked_widget_pageOne = QtGui.QWidget()
        self.stacked_widget_pageOne.setObjectName(_fromUtf8("stacked_widget_pageOne"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.stacked_widget_pageOne)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.stacked_widget_pageOne)
        self.tableWidget.setWordWrap(True)
	self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)        
	#self.tableWidget.horizontalHeader().setResizeMode(1)
	#self.tableWidget.horizontalHeader().setHorizontalScrollBarPolicy(2)
	self.tableWidget.resizeColumnsToContents()
        self.tableWidget.verticalHeader().hide()
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.main_Stacked_Widget.addWidget(self.stacked_widget_pageOne)
        self.main_verticalLayout.addWidget(self.main_Stacked_Widget)

	self.backTofirstScreen = QtGui.QPushButton(File_IO_Form)
	self.backTofirstScreen.setObjectName(_fromUtf8("backTofirstScreen"))
	self.main_verticalLayout.addWidget(self.backTofirstScreen)

	self.backTofirstScreen.setFocusPolicy(QtCore.Qt.TabFocus)
	self.backTofirstScreen.setFocus()

        self.verticalLayout_2.addLayout(self.main_verticalLayout)

        self.retranslateUi(File_IO_Form)
        QtCore.QMetaObject.connectSlotsByName(File_IO_Form)

    def retranslateUi(self, File_IO_Form):
        File_IO_Form.setWindowTitle(_translate("File_IO_Form", "File I/O Statistics", None))
        self.userName_SearchBox.setPlaceholderText(_translate("File_IO_Form", "User Name", None))
        self.processName_SearchBox.setPlaceholderText(_translate("File_IO_Form", "Process Name", None))
        self.localAddress_SearchBox.setPlaceholderText(_translate("File_IO_Form", "Access Date & Time", None))
        self.remoteAddress_SearchBox.setPlaceholderText(_translate("File_IO_Form", "Path Name", None))
	self.backTofirstScreen.setText(_translate("File_IO_Form", "Go Back to Previous Screen", None))		
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("File_IO_Form", "User Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("File_IO_Form", "Process Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("File_IO_Form", "Access Date & Time", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("File_IO_Form", "Path Name", None))
	self.hitSearch.setText(_translate("File_IO_Form", "Submit Search Criteria", None))
	self.enterValueToSearchLabel.setText(_translate("File_IO_Form", "Enter values to search:", None))
	self.fillArchiveTableFile = Ui_ArchiveTable()

    def mapUserIdToUsername(self):
	self.userMapping = {}
	with open('/etc/passwd','r') as fd:
		for line in fd:
        		data = line.split(":")
			uid = int(data[2])
			uname = data[0] 
			self.userMapping[uid] = uname
	return self.userMapping 

    def createTable(self,openFiles):
	self.tableWidget.setSortingEnabled(False)
	self.tableWidget.setRowCount(len(openFiles))
	for row in range(len(openFiles)):
       		for column in range(4):
			userFileitem = QtGui.QTableWidgetItem(str(openFiles[row][column]))
			self.tableWidget.setItem(row,column,userFileitem)		
	self.tableWidget.setSortingEnabled(True)
	self.tableWidget.resizeColumnsToContents()	
	self.tableWidget.horizontalHeader().setResizeMode(0)
	self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def validateSize(self,username,filename,userMapping):
	if(len(self.userName_SearchBox.text()) == 0 and len(self.processName_SearchBox.text()) == 0 and len(self.localAddress_SearchBox.text()) == 0 and len(self.remoteAddress_SearchBox.text()) == 0):
		self.getFilterResult(username,filename,userMapping)

    def getFilterResult(self,username,filename,userMapping):
	
	try:
		if(len(self.userName_SearchBox.text()) == 0 and len(self.processName_SearchBox.text()) == 0 and len(self.localAddress_SearchBox.text()) == 0 and len(self.remoteAddress_SearchBox.text()) == 0):
			file_total_stat = self.setFileTable(username,filename,userMapping,"","","","")
		else:
			file_total_stat = self.setFileTable(username,filename,userMapping,self.userName_SearchBox.text(),self.processName_SearchBox.text(),self.localAddress_SearchBox.text(),self.remoteAddress_SearchBox.text())

			
	
	except:
		print ""

	self.createTable(file_total_stat)
	
    def setFileTable(self,userlist,filelist,userMapping,userFilter,processFilter,dateAndTimeFilter,filePathFilter):
	openFiles = []
	found = False	
	pname = ""
	processDirectoryInProc = os.listdir('/proc')
	for processId in processDirectoryInProc:
		bool = any(not char.isdigit() for char in processId)
		if not bool:
			processPath = '/proc/'+processId+"/"
			try:
				statusData = ""
				with open(processPath+"status") as userId:
					statusData = userId.readlines()
					pname = str(statusData[0].split()[1])				
				if (re.search(str(processFilter),pname)) or processFilter =="":
					x = userlist.count()					
					if userFilter != "":					
						username = userFilter					
						x = 1
						found = True					
					for i in range(x):
						if found == False:
							username = userlist.item(i).text()
						if username == "*" or re.search(str(username),str(userMapping.get(int(statusData[8].split()[1])))):	
							for fds in os.listdir(processPath+"fd/"):
            							if os.path.isfile(processPath+"fd/"+fds) or os.path.isdir(processPath+"fd/"+fds):
                							filepath = os.readlink(processPath+"fd/"+fds)
									if filePathFilter == "" or re.search(str(filePathFilter),filepath):
                								if os.path.isfile(filepath) or os.path.isdir(processPath+"fd/"+fds):
											y = filelist.count()
											for j in range(y):
												filename = filelist.item(j).text()
                    										if str(filename) in str(filepath) or filename == "*":
                        										filterStrings = ['/dev/', 'socket:[', 'pipe','anon_inode:']
                        										found = False
                        										for filter1 in filterStrings:
                            											if filter1 in filepath:
                                											found = True
                                											break
                       	 										if not found:
                            											time_access = datetime.datetime.fromtimestamp(os.stat(filepath).st_atime)
        													stime_access = time_access.strftime('%m/%d/%Y - %H:%M:%S')							
														if re.search(str(dateAndTimeFilter),str(stime_access)) or dateAndTimeFilter == "":	
                            												openFiles.append([userMapping.get(int(statusData[8].split()[1])),pname,stime_access,filepath])
															if userFilter == "" and processFilter == "" and dateAndTimeFilter=="" and filePathFilter=="":
																self.fillArchiveTableFile.createLogForFile(openFiles,False,"")
																	
			except IOError:		
				continue;
	if(len(self.userName_SearchBox.text()) == 0 and len(self.processName_SearchBox.text()) == 0 and len(self.localAddress_SearchBox.text()) == 0 and len(self.remoteAddress_SearchBox.text()) == 0):
		self.createTable(openFiles)

	return openFiles		

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_File_IO_Form()
	ex.show()	
