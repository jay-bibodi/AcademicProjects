# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from FourthScreen import Ui_Network_IO_Form
from SecondScreen import Ui_SecondScreen
from ThirdScreen import Ui_File_IO_Form
from controlUserActivities import Ui_ControlUserActivities
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

class Ui_FirstScreen(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self)

    def setupUi(self, FirstScreen):
        FirstScreen.setObjectName(_fromUtf8("FirstScreen"))
	FirstScreen.setGeometry(100,60,800,500)

        self.label = QtGui.QLabel(FirstScreen)
        self.label.setGeometry(QtCore.QRect(10, 50, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.username_firstScreen = QtGui.QTextEdit(FirstScreen)
        self.username_firstScreen.setGeometry(QtCore.QRect(10, 80, 161, 27))
        self.username_firstScreen.setObjectName(_fromUtf8("username_firstScreen"))
	
	self.add = QtGui.QPushButton(FirstScreen)
        self.add.setGeometry(QtCore.QRect(180, 80, 81, 27))
        self.add.setObjectName(_fromUtf8("add"))

	self.file_radiobtn = QtGui.QRadioButton(FirstScreen)
        self.file_radiobtn.setGeometry(QtCore.QRect(20, 140, 117, 22))
        self.file_radiobtn.setObjectName(_fromUtf8("file_radiobtn"))

        self.network_radiobtn = QtGui.QRadioButton(FirstScreen)
        self.network_radiobtn.setGeometry(QtCore.QRect(20, 170, 117, 22))
        self.network_radiobtn.setObjectName(_fromUtf8("network_radiobtn"))

       	self.label_2 = QtGui.QLabel(FirstScreen)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
		
	self.realDataRefreshLabel = QtGui.QLabel(FirstScreen)
	self.realDataRefreshLabel.setGeometry(QtCore.QRect(10, 200, 221, 17))
	self.realDataRefreshLabel.setObjectName(_fromUtf8("realDataRefreshLabel"))
	
	self.lineEditRealData = QtGui.QLineEdit(FirstScreen)
        self.lineEditRealData.setGeometry(QtCore.QRect(10, 230, 231, 27))
        self.lineEditRealData.setObjectName(_fromUtf8("lineEditRealData"))

	self.checkbox = QtGui.QCheckBox(FirstScreen)
	self.checkbox.setGeometry(QtCore.QRect(10, 270, 241, 17))
	self.checkbox.setObjectName(_fromUtf8("checkbox"))

	self.label_4 = QtGui.QLabel(FirstScreen)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 241, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

	self.lineEdit_3 = QtGui.QLineEdit(FirstScreen)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 340, 231, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.submit_firstScreen = QtGui.QPushButton(FirstScreen)
        self.submit_firstScreen.setGeometry(QtCore.QRect(10, 390, 231, 27))
        self.submit_firstScreen.setObjectName(_fromUtf8("submit_firstScreen"))

	self.listWidget = QtGui.QListWidget(FirstScreen)
	self.listWidget.setGeometry(QtCore.QRect(270, 80, 371, 281))

	self.remove = QtGui.QPushButton(FirstScreen)
        self.remove.setGeometry(QtCore.QRect(270, 390, 371, 27))
        self.remove.setObjectName(_fromUtf8("remove"))

	self.label_5 = QtGui.QLabel(FirstScreen)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 381, 20))
        self.label_5.setStyleSheet(_fromUtf8("font: 75 12pt \"Ubuntu\";\n"
"text-decoration: underline;\n"
"font-weight: bold;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(FirstScreen)
        QtCore.QMetaObject.connectSlotsByName(FirstScreen)

    def retranslateUi(self, FirstScreen):
        FirstScreen.setWindowTitle(_translate("FirstScreen", "Main Window", None))
        self.label.setText(_translate("FirstScreen", "Username:", None))
	self.realDataRefreshLabel.setText(_translate("FirstScreen", "Real Data Refresh Time(in secs):", None))
        self.file_radiobtn.setText(_translate("FirstScreen", "File I/O", None))
	self.checkbox.setText(_translate("FirstScreen", "Show Archive Table", None))
        self.network_radiobtn.setText(_translate("FirstScreen", "Network I/O", None))
        self.label_2.setText(_translate("FirstScreen", "Monitor Activities:", None))
        self.submit_firstScreen.setText(_translate("FirstScreen", "Submit", None))		
	self.submit_firstScreen.clicked.connect(self.getUserInputFirstScreen)
	self.add.setText(_translate("FirstScreen", "Add User", None))
	self.remove.setText(_translate("FirstScreen","Remove User",None))
	self.lineEditRealData.setPlaceholderText(_translate("FirstScreen", "Enter time in seconds", None))
	self.label_5.setText(_translate("FirstScreen", "CSC 239 Project: Monitor & Control User Activities", None))
	self.label_4.setText(_translate("FirstScreen", "Archive Data Refresh Time(in mins):", None))
	self.lineEdit_3.setPlaceholderText(_translate("FirstScreen", "Enter time in minutes", None))	

	self.add.clicked.connect(self.addUserToList)
	self.remove.clicked.connect(self.removeUserFromList)
	self.archiveDataUI = Ui_ArchiveTable()
	self.firstTimeArchiveData = False

    def addUserToList(self):
	username = self.username_firstScreen.toPlainText()	
	
	if username == "":
		self.showMessageBox("Warning","No username to display")
	else:
		if username == "*" and self.listWidget.count() != 0:
			msg = QtGui.QMessageBox()
   			msg.setIcon(QtGui.QMessageBox.Information)
   			msg.setText("* indicate all users")
   			msg.setInformativeText("Other username in the list will not be considered.\n\nDo you want to continue?")
   			msg.setWindowTitle("Alert")
   			msg.setDetailedText("* indicate all users in the system.\nYou cannot add specific user name along with *.\nTo monitor for specific username remove * from the list.\nAny previously entered user name won't be considered as * is present in the list.")
   			msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
   			msg.buttonClicked.connect(self.msgbtn)
   			retval = msg.exec_()
			if retval == 16384:
				for index in xrange(self.listWidget.count()):
					self.listWidget.takeItem(self.listWidget.row(self.listWidget.item(0)))		
				item = QtGui.QListWidgetItem(username)
  				self.listWidget.addItem(item)
				self.username_firstScreen.setText("")
   			
		else:	
			isStarPresent = False
			isUsernamePresent = False
	
			for index in xrange(self.listWidget.count()):
				if self.listWidget.item(index).text() == "*":     		
					isStarPresent = True
					break;
				if self.listWidget.item(index).text() == username:
					isUsernamePresent = True
					break;

			if isStarPresent == False and isUsernamePresent == False:
				item = QtGui.QListWidgetItem(username)
  				self.listWidget.addItem(item)
				self.username_firstScreen.setText("")
			elif isStarPresent == True and isUsernamePresent == False:
				self.showMessageBox("Warning","* already present which indicates all users to monitor.\nRemove * to monitor specific username.")			
			elif isStarPresent == False and isUsernamePresent == True:
				self.showMessageBox("Warning","Username already present!")
		
    def msgbtn(self,i):
	print "Button pressed is:",i.text()

    def removeUserFromList(self):
    	listItems=self.listWidget.selectedItems()
    	if not listItems: return        
    	for item in listItems:
		self.listWidget.takeItem(self.listWidget.row(item))

    def getUserInputFirstScreen(self):
	username = self.username_firstScreen.toPlainText()	
	
	qValidator = QtGui.QIntValidator(0,100, self);
	self.lineEditRealData.setValidator(qValidator)
	self.lineEdit_3.setValidator(qValidator)
	
	timeInSecs = qValidator.validate(self.lineEditRealData.text(), 0)
	timeInMins = qValidator.validate(self.lineEdit_3.text(), 0)

	if str(self.lineEditRealData.text()) == "":
		if timeInSecs[1:-4] != 2:
			self.showMessageBox("Warning","Real data refresh time cannot be empty")
	elif self.checkbox.isChecked() and str(self.lineEdit_3.text()) == "":
		if timeInMins[1:-4] != 2:
			self.showMessageBox("Warning","Archive data refresh time cannot be empty")
	else:
		if self.checkbox.isChecked():
			self.archiveDataUI.loadRecordsFromCSVToDataStruct()

		if self.listWidget.count() != 0:
			if self.file_radiobtn.isChecked():	
				radioButton = self.file_radiobtn.text()
				self.getFileNameInput(username)	
			elif self.network_radiobtn.isChecked():
				radioButton = self.network_radiobtn.text()		
				self.initializeNetworkScreen(username)
			else:
				self.showMessageBox("Warning","Please select radio button of what you want to monitor!")	
		else:
			self.showMessageBox("Warning","Add username to list")

    def getFileNameInput(self,username):
	self.secondScreen = QtGui.QWidget()
	self.ui = Ui_SecondScreen()
	self.ui.setupUi(self.secondScreen)
	
	username = ""
	for index in xrange(self.listWidget.count()):	
     		username = username + self.listWidget.item(index).text() + ", "

	username = username[:-2]

	try:
		if self.ThirdToSecond == True:
			x = self.secondScreenListWidget.split(", ")
			for val in x:
				item = QtGui.QListWidgetItem(val)
  				self.ui.secondScreenlistWidget.addItem(item)
	except:
		print ""

	self.ui.label.setText(username)
	self.hide()
	self.secondScreen.show()
	self.ui.pushButton.clicked.connect(lambda :self.addFilePathToList())
	self.ui.pushButton_2.clicked.connect(lambda :self.removeFilePathFromList())
	self.ui.pushButton_3.clicked.connect(lambda :self.invokeThirdScreen(username,self.ui.secondScreenlistWidget))
	self.ui.pushButton_4.clicked.connect(lambda :self.restoreMainScreenFromSecondScreen())

    def addFilePathToList(self):	
	filepath = self.ui.lineEdit.text()	
	if filepath == "":
		self.showMessageBox("Warning","No filepath to add")
	else:
		if filepath == "*" and self.ui.secondScreenlistWidget.count() != 0:
			msg = QtGui.QMessageBox()
   			msg.setIcon(QtGui.QMessageBox.Information)
   			msg.setText("* indicate all filepath in the system.")
   			msg.setInformativeText("Other filepath in the list will not be considered.\n\nDo you want to continue?")
   			msg.setWindowTitle("Alert")
   			msg.setDetailedText("* indicate all filepath in the system.\n\nYou cannot add specific file path along with *.\n\nTo monitor for specific filepath remove * from the list.\n\nAny previously entered filepath won't be considered as * is present in the list.")
   			msg.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
   			msg.buttonClicked.connect(self.secondScreenMsgbtn)
   			retval = msg.exec_()
			if retval == 16384:
				for index in xrange(self.ui.secondScreenlistWidget.count()):
					self.ui.secondScreenlistWidget.takeItem(self.ui.secondScreenlistWidget.row(self.ui.secondScreenlistWidget.item(0)))		
				item = QtGui.QListWidgetItem(filepath)
  				self.ui.secondScreenlistWidget.addItem(item)
				self.ui.lineEdit.setText("")
   			
		else:	
			isStarPresent = False
			isFilePathPresent = False
	
			for index in xrange(self.ui.secondScreenlistWidget.count()):
				if self.ui.secondScreenlistWidget.item(index).text() == "*":     		
					isStarPresent = True
					break;
				if self.ui.secondScreenlistWidget.item(index).text() == filepath:
					isFilePathPresent = True
					break;

			if isStarPresent == False and isFilePathPresent == False:
				item = QtGui.QListWidgetItem(filepath)
  				self.ui.secondScreenlistWidget.addItem(item)
				self.ui.lineEdit.setText("")
			elif isStarPresent == True and isFilePathPresent == False:
				self.showMessageBox("Warning","* already present which indicates all filepath to monitor.\nRemove * to monitor specific filepath.")			
			elif isStarPresent == False and isFilePathPresent == True:
				self.showMessageBox("Warning","Filepath already present!")
		
    def secondScreenMsgbtn(self,i):
	print "Button pressed is:",i.text()

    def removeFilePathFromList(self):
	listItems=self.ui.secondScreenlistWidget.selectedItems()
    	if not listItems: return        
    	for item in listItems:
		self.ui.secondScreenlistWidget.takeItem(self.ui.secondScreenlistWidget.row(item))

    def invokeThirdScreen(self,username,filename):
	self.ThirdToSecond = True
	self.secondScreenListWidget = ""

	for index in xrange(self.ui.secondScreenlistWidget.count()):
     		self.secondScreenListWidget = self.secondScreenListWidget + self.ui.secondScreenlistWidget.item(index).text() + ", "

	self.secondScreenListWidget = self.secondScreenListWidget[:-2]

	self.thirdScreen = QtGui.QWidget()
	self.controlUserActivitiesFile = QtGui.QWidget()

	self.ui = Ui_File_IO_Form()
	self.controlUserActivityFileUI = Ui_ControlUserActivities()

	self.ui.setupUi(self.thirdScreen)
	self.controlUserActivityFileUI.setupUi(self.controlUserActivitiesFile)

	userMapping = self.ui.mapUserIdToUsername()
	self.ui.setFileTable(self.listWidget,filename,userMapping,"","","","")
	self.ui.backTofirstScreen.clicked.connect(lambda :self.restoreSecondScreenFromThirdScreen(username))
	self.ui.userName_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,filename,userMapping))
	self.ui.processName_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,filename,userMapping))
	self.ui.localAddress_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,filename,userMapping))
	self.ui.remoteAddress_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,filename,userMapping))
	self.ui.hitSearch.clicked.connect(lambda :self.ui.getFilterResult(self.listWidget,filename,userMapping))
	self.controlUserActivityFileUI.cua_file_addFilepath_button.clicked.connect(lambda :self.controlUserActivityFileUI.addFilePathToBlock())
	self.controlUserActivityFileUI.cua_file_removePath_button.clicked.connect(lambda :self.controlUserActivityFileUI.removeFilepathFromList())

	self.controlUserActivityFileUI.cua_file_blockPath_button.clicked.connect(lambda :self.controlUserActivityFileUI.blockFilePath())
	# unblock file	
	#self.controlUserActivityFileUI.cua_file_unblock_path_button.clicked.connect(lambda :self.)
	self.secondScreen.hide()

	self.controlUserActivityFileUI.control_user_activities.setTabEnabled(1, False)
	self.thirdScreen.show()
	self.controlUserActivitiesFile.show()

	self.timer = QtCore.QTimer()
        self.timer.setInterval(int(self.lineEditRealData.text())*1000)
        self.timer.timeout.connect(lambda :self.ui.setFileTable(self.listWidget,filename,userMapping,"","","",""))
	self.timer.start()

	if self.checkbox.isChecked():
		self.openArchiveDataTable()

    def restoreSecondScreenFromThirdScreen(self,username):
	self.timer.stop()	
	self.getFileNameInput(username)
	self.thirdScreen.hide()	
	self.controlUserActivitiesFile.hide()

    def restoreMainScreenFromSecondScreen(self):
	self.secondScreen.hide()
	self.show()	

    def initializeNetworkScreen(self,username):
	self.fourthScreen = QtGui.QWidget()
	self.controlUserActivities = QtGui.QWidget()

	self.ui = Ui_Network_IO_Form()
	self.controlActivityUI = Ui_ControlUserActivities()

	self.ui.setupUi(self.fourthScreen)
	self.controlActivityUI.setupUi(self.controlUserActivities)

	userMapping = self.ui.mapUserIdToUsername()	
	self.ui.setNetworkTable(self.listWidget,userMapping,"","","","")
	self.ui.userName_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,userMapping))
	self.ui.processName_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,userMapping))
	self.ui.localAddress_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,userMapping))
	self.ui.remoteAddress_SearchBox.textEdited.connect(lambda :self.ui.validateSize(self.listWidget,userMapping))
	self.ui.hitSearch.clicked.connect(lambda :self.ui.getFilterResult(self.listWidget,userMapping))
	self.controlActivityUI.pushButton_7.clicked.connect(lambda :self.controlActivityUI.addRemoteAddressToBlock())
	self.controlActivityUI.pushButton_5.clicked.connect(lambda :self.controlActivityUI.removeRemoteAddressFromList())
	self.controlActivityUI.pushButton_8.clicked.connect(lambda :self.controlActivityUI.blockRemoteAddress())
	# unblock file	
	#self.controlActivityUI.pushButton_6.clicked.connect(lambda :self.)
	
	self.hide()

	self.controlActivityUI.control_user_activities.setCurrentIndex(1)
	self.controlActivityUI.control_user_activities.setTabEnabled(0, False)
	self.fourthScreen.show()
	self.controlUserActivities.show()

	self.timer = QtCore.QTimer()
        self.timer.setInterval(int(self.lineEditRealData.text())*1000)
	self.timer.timeout.connect(lambda :self.ui.setNetworkTable(self.listWidget,userMapping,"","","",""))
	self.timer.start()
	self.ui.backTofirstScreen.clicked.connect(lambda :self.restoreMainScreen())	

	if self.checkbox.isChecked():
		self.openArchiveDataTable()

    def restoreMainScreen(self):
	self.timer.stop()
	self.fourthScreen.hide()
	self.controlUserActivities.hide()
	self.show()

    def showMessageBox(self,title,message):
	msgBox = QtGui.QMessageBox()
	msgBox.setIcon(QtGui.QMessageBox.Warning)
	msgBox.setWindowTitle(title)
	msgBox.setText(message)
	msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
	msgBox.exec_()	
   
    def openArchiveDataTable(self):
	self.archiveDataScreen = QtGui.QWidget()
	self.archiveDataUI.setupUi(self.archiveDataScreen)
	#if self.firstTimeArchiveData == False:
	self.archiveDataUI.createLogForFile("",True,int(self.lineEdit_3.text()))
	self.archiveDataUI.createLogForNetwork("",True,int(self.lineEdit_3.text()))		
	#self.firstTimeArchiveData = True
	self.archiveDataScreen.show()

	self.timerArchiveTable = QtCore.QTimer()
        self.timerArchiveTable.setInterval(int(self.lineEdit_3.text())*1000*12*5)
	self.timerArchiveTable.timeout.connect(lambda :self.archiveDataUI.createLogForFile("",True,int(self.lineEdit_3.text())))
	self.timerArchiveTable.timeout.connect(lambda :self.archiveDataUI.createLogForNetwork("",True,int(self.lineEdit_3.text())))
	self.timerArchiveTable.start()

	#self.archiveDataUI.file_userName_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveFileData,True,int(self.lineEdit_3.text())))
	#self.archiveDataUI.file_processName_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveFileData,True,int(self.lineEdit_3.text())))
	#self.archiveDataUI.file_localAddress_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveFileData,True,int(self.lineEdit_3.text())))
	#self.archiveDataUI.file_remoteAddress_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveFileData,True,int(self.lineEdit_3.text())))
	#self.archiveDataUI.file_hitSearch.clicked.connect(lambda :self.archiveDataUI.getFilterResult(self.updatedArchiveFileData,self.archiveDataUI.file_tableWidget,self.archiveDataUI.file_userName_SearchBox,self.archiveDataUI.file_processName_SearchBox,self.archiveDataUI.file_localAddress_SearchBox,self.archiveDataUI.file_remoteAddress_SearchBox,int(self.lineEdit_3.text()),True))

	#self.archiveDataUI.network_userName_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveNetworkData,False,int(self.lineEdit_3.text())))
	#self.archiveDataUI.network_processName_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveNetworkData,False,int(self.lineEdit_3.text())))
	#self.archiveDataUI.network_localAddress_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveNetworkData,False,int(self.lineEdit_3.text())))
	#self.archiveDataUI.network_remoteAddress_SearchBox.textEdited.connect(lambda :self.archiveDataUI.validateSize(self.updatedArchiveNetworkData,False,int(self.lineEdit_3.text())))
	#self.archiveDataUI.network_hitSearch.clicked.connect(lambda :self.archiveDataUI.getFilterResult(self.updatedArchiveNetworkData,self.archiveDataUI.network_tableWidget,self.archiveDataUI.network_userName_SearchBox,self.archiveDataUI.network_processName_SearchBox,self.archiveDataUI.network_localAddress_SearchBox,self.archiveDataUI.network_remoteAddress_SearchBox,int(self.lineEdit_3.text()),False))	

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_FirstScreen()
	ex.show()
	sys.exit(app.exec_())
