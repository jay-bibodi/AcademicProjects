# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os

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

class Ui_SecondScreen(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self) 

    def setupUi(self, SecondScreen):
        SecondScreen.setObjectName(_fromUtf8("SecondScreen"))
        SecondScreen.setGeometry(100,60,800,500)
        
        self.label = QtGui.QLabel(SecondScreen)
        self.label.setGeometry(QtCore.QRect(140, 10, 100, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SecondScreen)
        self.label_2.setGeometry(QtCore.QRect(9, 10, 68, 17))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(SecondScreen)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 68, 17))
        self.label_3.setMaximumSize(QtCore.QSize(100, 100))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(SecondScreen)
        self.label_4.setGeometry(QtCore.QRect(140, 40, 68, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(SecondScreen)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 101, 17))
        self.label_5.setMaximumSize(QtCore.QSize(150, 150))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(SecondScreen)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 221, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(SecondScreen)
        self.pushButton.setGeometry(QtCore.QRect(380, 70, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.secondScreenlistWidget = QtGui.QListWidget(SecondScreen)
        self.secondScreenlistWidget.setGeometry(QtCore.QRect(140, 110, 341, 241))
        self.secondScreenlistWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_2 = QtGui.QPushButton(SecondScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 360, 341, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(SecondScreen)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 390, 163, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(SecondScreen)
        self.pushButton_4.setGeometry(QtCore.QRect(308, 390, 175, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
	self.label_2.setFocusPolicy(QtCore.Qt.TabFocus)
	self.label_2.setFocus()

        self.retranslateUi(SecondScreen)
        QtCore.QMetaObject.connectSlotsByName(SecondScreen)

    def retranslateUi(self, SecondScreen):
        SecondScreen.setWindowTitle(_translate("SecondScreen", "Monitor File I/O", None))
        self.label.setText(_translate("SecondScreen", "TextLabel", None))
        self.label_2.setText(_translate("SecondScreen", "Username", None))
        self.label_3.setText(_translate("SecondScreen", "Monitor", None))
        self.label_4.setText(_translate("SecondScreen", "File I/O", None))
        self.label_5.setText(_translate("SecondScreen", "Enter File Path", None))
        self.pushButton.setText(_translate("SecondScreen", "Add Path ", None))
        self.pushButton_2.setText(_translate("SecondScreen", "Remove Path", None))
        self.pushButton_3.setText(_translate("SecondScreen", "Submit", None))
        self.pushButton_4.setText(_translate("SecondScreen", "Go Back To Previous Screen", None))
	self.lineEdit.setPlaceholderText(_translate("SecondScreen", "Enter File Path", None))

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_SecondScreen()
	ex.show()	
	sys.exit(app.exec_())
