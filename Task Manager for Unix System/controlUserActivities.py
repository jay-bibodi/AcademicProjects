# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlUserActivities.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, subprocess

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

class Ui_ControlUserActivities(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self)
	
    def setupUi(self, ControlUserActivities):
        ControlUserActivities.setObjectName(_fromUtf8("ControlUserActivities"))
        ControlUserActivities.resize(764, 550)
	
	self.verticalLayout_2 = QtGui.QVBoxLayout(ControlUserActivities)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        
	self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.control_user_activities = QtGui.QTabWidget(ControlUserActivities)
        self.control_user_activities.setGeometry(QtCore.QRect(0, 0, 900, 570))
        self.control_user_activities.setAccessibleName(_fromUtf8(""))
        self.control_user_activities.setObjectName(_fromUtf8("control_user_activities"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.cua_file_list_of_blockled_file_paths = QtGui.QLabel(self.tab_3)
        self.cua_file_list_of_blockled_file_paths.setGeometry(QtCore.QRect(390, 90, 231, 17))
        self.cua_file_list_of_blockled_file_paths.setObjectName(_fromUtf8("cua_file_list_of_blockled_file_paths"))
        self.cua_file_removePath_button = QtGui.QPushButton(self.tab_3)
        self.cua_file_removePath_button.setGeometry(QtCore.QRect(10, 440, 211, 27))
        self.cua_file_removePath_button.setObjectName(_fromUtf8("cua_file_removePath_button"))
        self.cua_file_unblock_path_button = QtGui.QPushButton(self.tab_3)
        self.cua_file_unblock_path_button.setGeometry(QtCore.QRect(490, 440, 251, 27))
        self.cua_file_unblock_path_button.setObjectName(_fromUtf8("cua_file_unblock_path_button"))
        self.cua_file_addFilepath_button = QtGui.QPushButton(self.tab_3)
        self.cua_file_addFilepath_button.setGeometry(QtCore.QRect(130, 40, 121, 27))
        self.cua_file_addFilepath_button.setObjectName(_fromUtf8("cua_file_addFilepath_button"))
        self.cua_file_list_of_file_path_to_block_file_access = QtGui.QLabel(self.tab_3)
        self.cua_file_list_of_file_path_to_block_file_access.setGeometry(QtCore.QRect(10, 90, 251, 17))
        self.cua_file_list_of_file_path_to_block_file_access.setObjectName(_fromUtf8("cua_file_list_of_file_path_to_block_file_access"))
        self.cua_file_listWidget1 = QtGui.QListWidget(self.tab_3)
        self.cua_file_listWidget1.setGeometry(QtCore.QRect(10, 120, 351, 311))
        self.cua_file_listWidget1.setObjectName(_fromUtf8("cua_file_listWidget1"))
        self.cua_file_line_edit_enter_file_path = QtGui.QLineEdit(self.tab_3)
        self.cua_file_line_edit_enter_file_path.setGeometry(QtCore.QRect(130, 10, 451, 27))
        self.cua_file_line_edit_enter_file_path.setObjectName(_fromUtf8("cua_file_line_edit_enter_file_path"))
        self.cua_file_blockPath_button = QtGui.QPushButton(self.tab_3)
        self.cua_file_blockPath_button.setGeometry(QtCore.QRect(240, 440, 231, 27))
        self.cua_file_blockPath_button.setObjectName(_fromUtf8("cua_file_blockPath_button"))
        self.cua_file_listWidget_2 = QtGui.QListWidget(self.tab_3)
        self.cua_file_listWidget_2.setGeometry(QtCore.QRect(390, 120, 351, 311))
        self.cua_file_listWidget_2.setObjectName(_fromUtf8("cua_file_listWidget_2"))
        self.cua_file_enter_file_path_label = QtGui.QLabel(self.tab_3)
        self.cua_file_enter_file_path_label.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.cua_file_enter_file_path_label.setStyleSheet(_fromUtf8(""))
        self.cua_file_enter_file_path_label.setObjectName(_fromUtf8("cua_file_enter_file_path_label"))
        self.control_user_activities.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_5 = QtGui.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(390, 90, 271, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 440, 211, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 440, 251, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 40, 181, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 251, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.listWidget_3 = QtGui.QListWidget(self.tab_4)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 120, 351, 311))
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 10, 451, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(240, 440, 231, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.listWidget_4 = QtGui.QListWidget(self.tab_4)
        self.listWidget_4.setGeometry(QtCore.QRect(390, 120, 351, 311))
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.label_7.setStyleSheet(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.control_user_activities.addTab(self.tab_4, _fromUtf8(""))

	self.verticalLayout.addWidget(self.control_user_activities)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(ControlUserActivities)
	# sets active tab
        self.control_user_activities.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ControlUserActivities)

    def retranslateUi(self, ControlUserActivities):
        ControlUserActivities.setWindowTitle(_translate("ControlUserActivities", "Control User Activities", None))
        self.cua_file_list_of_blockled_file_paths.setText(_translate("ControlUserActivities", "List of already blocked file paths", None))
        self.cua_file_removePath_button.setText(_translate("ControlUserActivities", "Remove Path From List", None))
        self.cua_file_unblock_path_button.setText(_translate("ControlUserActivities", "Unblock Path", None))
        self.cua_file_addFilepath_button.setText(_translate("ControlUserActivities", "Add File Path", None))
        self.cua_file_list_of_file_path_to_block_file_access.setText(_translate("ControlUserActivities", "List of file paths to block file access", None))
        self.cua_file_blockPath_button.setText(_translate("ControlUserActivities", "Block Path", None))
        self.cua_file_enter_file_path_label.setText(_translate("ControlUserActivities", "Enter File path: ", None))
        self.control_user_activities.setTabText(self.control_user_activities.indexOf(self.tab_3), _translate("ControlUserActivities", "Control File I/O Activities", None))
        self.label_5.setText(_translate("ControlUserActivities", "List of already blocked remote address", None))
        self.pushButton_5.setText(_translate("ControlUserActivities", "Remove Path From List", None))
        self.pushButton_6.setText(_translate("ControlUserActivities", "Unblock Path", None))
        self.pushButton_7.setText(_translate("ControlUserActivities", "Add Remote Address", None))
        self.label_6.setText(_translate("ControlUserActivities", "List of remote address to block", None))
        self.pushButton_8.setText(_translate("ControlUserActivities", "Block Path", None))
        self.label_7.setText(_translate("ControlUserActivities", "Enter Remote Address: ", None))
        self.control_user_activities.setTabText(self.control_user_activities.indexOf(self.tab_4), _translate("ControlUserActivities", "Control Network Activities", None))

    def addRemoteAddressToBlock(self):
	remoteAddressPath = self.lineEdit_2.text()
	if remoteAddressPath == "":
		self.showAlertBox("Warning","No remote Address path to add")
	else:
		if remoteAddressPath == "*" and self.cua_file_listWidget1.count() != 0:
			msgBoxOne = QtGui.QMessageBox()
   			msgBoxOne.setIcon(QtGui.QMessageBox.Information)
   			msgBoxOne.setText("* indicate all filepath in the system.")
   			msgBoxOne.setInformativeText("Other filepath in the list will not be considered.\n\nDo you want to continue?")
   			msgBoxOne.setWindowTitle("Alert")
   			msgBoxOne.setDetailedText("* indicate all filepath in the system.\n\nYou cannot add specific remote address path along with *.\n\nTo block a specific remote address path remove * from the list.\n\nAny previously entered remote address path won't be considered as * is present in the list.")
   			msgBoxOne.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
   			msgBoxOne.buttonClicked.connect(self.controlUserMsgButton)
   			retval = msg.exec_()
			if retval == 16384:
				for index in xrange(self.listWidget_3.count()):
					self.listWidget_3.takeItem(self.listWidget_3.row(self.listWidget_3.item(0)))		
				item = QtGui.QListWidgetItem(remoteAddressPath)
  				self.listWidget_3.addItem(item)
				self.lineEdit_2.setText("")
   			
		else:	
			isStarPresent = False
			isremoteAddressPathPresent = False
	
			for index in xrange(self.listWidget_3.count()):
				if self.listWidget_3.item(index).text() == "*":     		
					isStarPresent = True
					break;
				if self.listWidget_3.item(index).text() == remoteAddressPath:
					isremoteAddressPathPresent = True
					break;

			if isStarPresent == False and isremoteAddressPathPresent == False:
				item = QtGui.QListWidgetItem(remoteAddressPath)
  				self.listWidget_3.addItem(item)
				self.lineEdit_2.setText("")
			elif isStarPresent == True and isremoteAddressPathPresent == False:
				self.showAlertBox("Warning","* already present which indicates all remoteAddressPath to block.\nRemove * to block specific remoteAddressPath.")			
			elif isStarPresent == False and isremoteAddressPathPresent == True:
				self.showAlertBox("Warning","remote address path already present!")
		
    def controlUserMsgButton(self,i):
	print "Button pressed is:",i.text()

    def removeRemoteAddressFromList(self):
	listItems=self.listWidget_3.selectedItems()
    	if not listItems: return        
    	for item in listItems:
		self.listWidget_3.takeItem(self.listWidget_3.row(item))

    def addFilePathToBlock(self):
	filepath = self.cua_file_line_edit_enter_file_path.text()
	if filepath == "":
		self.showAlertBox("Warning","No filepath to add")
	else:
		if filepath == "*" and self.cua_file_listWidget1.count() != 0:
			msgBoxOne = QtGui.QMessageBox()
   			msgBoxOne.setIcon(QtGui.QMessageBox.Information)
   			msgBoxOne.setText("* indicate all filepath in the system.")
   			msgBoxOne.setInformativeText("Other filepath in the list will not be considered.\n\nDo you want to continue?")
   			msgBoxOne.setWindowTitle("Alert")
   			msgBoxOne.setDetailedText("* indicate all filepath in the system.\n\nYou cannot add specific filepath along with *.\n\nTo block a specific filepath remove * from the list.\n\nAny previously entered filepath won't be considered as * is present in the list.")
   			msgBoxOne.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
   			msgBoxOne.buttonClicked.connect(self.controlUserMsgButtonFile)
   			retval = msgBoxOne.exec_()
			if retval == 16384:
				for index in xrange(self.cua_file_listWidget1.count()):
					self.cua_file_listWidget1.takeItem(self.cua_file_listWidget1.row(self.cua_file_listWidget1.item(0)))		
				item = QtGui.QListWidgetItem(filepath)
  				self.cua_file_listWidget1.addItem(item)
				self.cua_file_line_edit_enter_file_path.setText("")
   			
		else:	
			isStarPresent = False
			isremoteAddressPathPresent = False
	
			for index in xrange(self.cua_file_listWidget1.count()):
				if self.cua_file_listWidget1.item(index).text() == "*":     		
					isStarPresent = True
					break;
				if self.cua_file_listWidget1.item(index).text() == filepath:
					isremoteAddressPathPresent = True
					break;

			if isStarPresent == False and isremoteAddressPathPresent == False:
				item = QtGui.QListWidgetItem(filepath)
  				self.cua_file_listWidget1.addItem(item)
				self.cua_file_line_edit_enter_file_path.setText("")
			elif isStarPresent == True and isremoteAddressPathPresent == False:
				self.showAlertBox("Warning","* already present which indicates all filepath to block.\nRemove * to block specific filepath.")			
			elif isStarPresent == False and isremoteAddressPathPresent == True:
				self.showAlertBox("Warning","filepath already present!")
		
    def controlUserMsgButtonFile(self,i):
	print "Button pressed is:",i.text()

    def removeFilepathFromList(self):
	listItems=self.cua_file_listWidget1.selectedItems()
    	if not listItems: return        
    	for item in listItems:
		self.cua_file_listWidget1.takeItem(self.cua_file_listWidget1.row(item))

    def showAlertBox(self,title,message):
	msgAlertBox = QtGui.QMessageBox()
	msgAlertBox.setIcon(QtGui.QMessageBox.Warning)
	msgAlertBox.setWindowTitle(title)
	msgAlertBox.setText(message)
	msgAlertBox.setStandardButtons(QtGui.QMessageBox.Ok)
	msgAlertBox.exec_()	

    def blockFilePath(self):
	isfilepathBlocked = False
	for index in xrange(self.cua_file_listWidget1.count()):
		filepath = self.cua_file_listWidget1.item(index).text()
		for x in xrange(self.cua_file_listWidget_2.count()):
			if self.cua_file_listWidget_2.item(x).text() == filepath:
				isfilepathBlocked = True
				break;

		if isfilepathBlocked == False:
			if filepath == "*":
				msgBoxOne = QtGui.QMessageBox()
   				msgBoxOne.setIcon(QtGui.QMessageBox.Information)
   				msgBoxOne.setText("* indicate all filepath in the system.")
   				msgBoxOne.setInformativeText("All filepaths in the system will be blocked.\n\nDo you want to continue?")
   				msgBoxOne.setWindowTitle("Alert")
   				msgBoxOne.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
   				msgBoxOne.buttonClicked.connect(self.controlUserMsgButtonFile)
   				retval = msgBoxOne.exec_()
				if retval == 16384:
					for y in xrange(self.cua_file_listWidget_2.count()):
						self.cua_file_listWidget_2.takeItem(self.cua_file_listWidget_2.row(self.cua_file_listWidget_2.item(y)))
					self.cua_file_listWidget1.takeItem(self.cua_file_listWidget1.row(self.cua_file_listWidget1.item(index)))
					item = QtGui.QListWidgetItem(filepath)
  					self.cua_file_listWidget_2.addItem(item)			
			else: 
				self.cua_file_listWidget1.takeItem(self.cua_file_listWidget1.row(self.cua_file_listWidget1.item(index)))
				item = QtGui.QListWidgetItem(filepath)
  				self.cua_file_listWidget_2.addItem(item)
	subprocess.call(['./test.sh'])	

    def blockRemoteAddress(self):
	isRemoteAddressBlocked = False
	for index in xrange(self.listWidget_3.count()):
		remoteAddress = self.listWidget_3.item(index).text()
		for x in xrange(self.listWidget_4.count()):
			if self.listWidget_4.item(x).text() == remoteAddress:
				isRemoteAddressBlocked = True
				break;

		if isRemoteAddressBlocked == False:
			if remoteAddress == "*":
				msgBoxOne = QtGui.QMessageBox()
   				msgBoxOne.setIcon(QtGui.QMessageBox.Information)
   				msgBoxOne.setText("* indicate all remote address path in the system.")
   				msgBoxOne.setInformativeText("All remote address path in the system will be blocked.\n\nDo you want to continue?")
   				msgBoxOne.setWindowTitle("Alert")
   				msgBoxOne.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
   				msgBoxOne.buttonClicked.connect(self.controlUserMsgButtonFile)
   				retval = msgBoxOne.exec_()
				if retval == 16384:
					for y in xrange(self.listWidget_4.count()):
						self.listWidget_4.takeItem(self.listWidget_4.row(self.listWidget_4.item(y)))
					self.listWidget_3.takeItem(self.listWidget_3.row(self.listWidget_3.item(index)))
					item = QtGui.QListWidgetItem(remoteAddress)
  					self.listWidget_4.addItem(item)		
			else:
				self.listWidget_3.takeItem(self.listWidget_3.row(self.listWidget_3.item(index)))
				item = QtGui.QListWidgetItem(remoteAddress)
  				self.listWidget_4.addItem(item)

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_ControlUserActivities()
	ex.show()
	sys.exit(app.exec_())
