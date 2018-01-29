# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FourthScreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os, struct, socket, re
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

class Ui_Network_IO_Form(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self) 	

    def setupUi(self, Network_IO_Form):
        Network_IO_Form.setObjectName(_fromUtf8("Network_IO_Form"))
        Network_IO_Form.setGeometry(100,60,800,500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Network_IO_Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.main_verticalLayout = QtGui.QVBoxLayout()
        self.main_verticalLayout.setObjectName(_fromUtf8("main_verticalLayout"))
	#######################
	self.enterValueToSearchLabel = QtGui.QLabel(Network_IO_Form)
        self.enterValueToSearchLabel.setObjectName(_fromUtf8("label"))
	self.main_verticalLayout.addWidget(self.enterValueToSearchLabel)
	########################
        self.horizontalLayout_For_LineEditSearchBox = QtGui.QHBoxLayout()
        self.horizontalLayout_For_LineEditSearchBox.setObjectName(_fromUtf8("horizontalLayout_For_LineEditSearchBox"))
        self.userName_SearchBox = QtGui.QLineEdit(Network_IO_Form)
        self.userName_SearchBox.setObjectName(_fromUtf8("userName_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.userName_SearchBox)
        self.processName_SearchBox = QtGui.QLineEdit(Network_IO_Form)
        self.processName_SearchBox.setObjectName(_fromUtf8("processName_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.processName_SearchBox)
        self.localAddress_SearchBox = QtGui.QLineEdit(Network_IO_Form)
        self.localAddress_SearchBox.setObjectName(_fromUtf8("localAddress_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.localAddress_SearchBox)
        self.remoteAddress_SearchBox = QtGui.QLineEdit(Network_IO_Form)
        self.remoteAddress_SearchBox.setObjectName(_fromUtf8("remoteAddress_SearchBox"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.remoteAddress_SearchBox)
        self.main_verticalLayout.addLayout(self.horizontalLayout_For_LineEditSearchBox)
	######################        
	self.hitSearch = QtGui.QPushButton(Network_IO_Form)
	self.hitSearch.setObjectName(_fromUtf8("hitSearch"))
	self.main_verticalLayout.addWidget(self.hitSearch)
	########################        
	self.main_Stacked_Widget = QtGui.QStackedWidget(Network_IO_Form)
        self.main_Stacked_Widget.setObjectName(_fromUtf8("main_Stacked_Widget"))
        self.stacked_widget_pageOne = QtGui.QWidget()
        self.stacked_widget_pageOne.setObjectName(_fromUtf8("stacked_widget_pageOne"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.stacked_widget_pageOne)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.stacked_widget_pageOne)
        #self.tableWidget.setWordWrap(True)
	self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setCornerButtonEnabled(True)
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
	self.tableWidget.horizontalHeader().setResizeMode(1)
        self.tableWidget.verticalHeader().hide()
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.main_Stacked_Widget.addWidget(self.stacked_widget_pageOne)
        self.main_verticalLayout.addWidget(self.main_Stacked_Widget)

	self.backTofirstScreen = QtGui.QPushButton(Network_IO_Form)
	self.backTofirstScreen.setObjectName(_fromUtf8("backTofirstScreen"))
	self.main_verticalLayout.addWidget(self.backTofirstScreen)

	self.backTofirstScreen.setFocusPolicy(QtCore.Qt.TabFocus)
	self.backTofirstScreen.setFocus()

        self.verticalLayout_2.addLayout(self.main_verticalLayout)

        self.retranslateUi(Network_IO_Form)
        QtCore.QMetaObject.connectSlotsByName(Network_IO_Form)

    def retranslateUi(self, Network_IO_Form):
        Network_IO_Form.setWindowTitle(_translate("Network_IO_Form", "Network I/O Statistics", None))
        self.userName_SearchBox.setPlaceholderText(_translate("Network_IO_Form", "User Name", None))
        self.processName_SearchBox.setPlaceholderText(_translate("Network_IO_Form", "Process Name", None))
        self.localAddress_SearchBox.setPlaceholderText(_translate("Network_IO_Form", "Local Address", None))
        self.remoteAddress_SearchBox.setPlaceholderText(_translate("Network_IO_Form", "Remote Address", None))
	self.backTofirstScreen.setText(_translate("Network_IO_Form", "Go Back to Previous Screen", None))		
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Network_IO_Form", "User Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Network_IO_Form", "Process Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Network_IO_Form", "Local Address", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Network_IO_Form", "Remote Address", None))
	self.hitSearch.setText(_translate("Network_IO_Form", "Submit Search Criteria", None))
	self.enterValueToSearchLabel.setText(_translate("Network_IO_Form", "Enter values to search:", None))
	self.fillArchiveTableNetwork = Ui_ArchiveTable()

    def validateSize(self,username,userMapping):
	if(len(self.userName_SearchBox.text()) == 0 and len(self.processName_SearchBox.text()) == 0 and len(self.localAddress_SearchBox.text()) == 0 and len(self.remoteAddress_SearchBox.text()) == 0):
		self.getFilterResult(username,userMapping)	

    def getFilterResult(self,userlist,userMapping):
	
	try:
		if(len(self.userName_SearchBox.text()) == 0 and len(self.processName_SearchBox.text()) == 0 and len(self.localAddress_SearchBox.text()) == 0 and len(self.remoteAddress_SearchBox.text()) == 0):
			network_total_stat = self.setNetworkTable(userlist,userMapping,"","","","")
		else:
			network_total_stat = self.setNetworkTable(userlist,userMapping,self.userName_SearchBox.text(),self.processName_SearchBox.text(),self.localAddress_SearchBox.text(),self.remoteAddress_SearchBox.text())		
	except:
		print ""
	
	self.createTable(network_total_stat)

    def createTable(self,network_total_stat):
	self.tableWidget.setSortingEnabled(False)
	self.tableWidget.setRowCount(len(network_total_stat))
	for row in range(len(network_total_stat)):
       		for column in range(4):
			usernetitem = QtGui.QTableWidgetItem(str(network_total_stat[row][column]))
			self.tableWidget.setItem(row,column,usernetitem)		
	self.tableWidget.setSortingEnabled(True)
	
    def mapUserIdToUsername(self):
	self.userMapping = {}
	with open('/etc/passwd','r') as fd:
		for line in fd:
        		data = line.split(":")
			uid = int(data[2])
			uname = data[0] 
			self.userMapping[uid] = uname
	return self.userMapping
	
    def setNetworkTable(self,userlist,userMapping,userFilter,processFilter,localAddFilter,remoteAddFilter):
	networkData = {}	
	network_total_stat = []
	i = 0
	found = False	
	pname = ""
	with open("/proc/net/tcp") as tcpFile:
		for tcpLine in tcpFile:
			if i != 0:
				tcpData = tcpLine.split()
				localAddressTcp = tcpData[1].split(":")[0]	
				localAddressTcpPort = tcpData[1].split(":")[1]
				addr_long = int(localAddressTcp,16)

				localAddressTcp = socket.inet_ntoa(struct.pack("<L", addr_long))
				try:
					dns = socket.gethostbyaddr(localAddressTcp)
					success = True
				except socket.herror:
					success = False;
					
				if success:
					localAddressTcp = dns[0]	 

				localAddressTcpPort = int(localAddressTcpPort,16)				 	

				remoteAddressTcp = tcpData[2].split(":")[0]	
				remoteAddressTcpPort = tcpData[2].split(":")[1]
				addr_long = int(remoteAddressTcp,16)
				remoteAddressTcp = socket.inet_ntoa(struct.pack("<L", addr_long))
				
				try:
					dns = socket.gethostbyaddr(remoteAddressTcp)
					success = True
				except socket.herror:
					success = False;
					
				if success:
					remoteAddressTcp = dns[0]			

				remoteAddressTcpPort = int(remoteAddressTcpPort,16)
	
				networkData[tcpData[9]] = [str(localAddressTcp)+":"+str(localAddressTcpPort),str(remoteAddressTcp)+":"+str(remoteAddressTcpPort)]
			i += 1
	i = 0	
	with open("/proc/net/udp") as udpFile:
		for udpLine in udpFile:
			if i != 0:
				udpData = udpLine.split()
				
				localAddressUdp = udpData[1].split(":")[0]	
				localAddressUdpPort = udpData[1].split(":")[1]
				addr_long = int(localAddressUdp,16)
				localAddressUdp = socket.inet_ntoa(struct.pack("<L", addr_long))

				try:
					dns = socket.gethostbyaddr(localAddressUdp)
					success = True
				except socket.herror:
					success = False;
					
				if success:
					localAddressUdp = dns[0]

				localAddressUdpPort = int(localAddressUdpPort,16)				 	

				remoteAddressUdp = udpData[2].split(":")[0]	
				remoteAddressUdpPort = udpData[2].split(":")[1]
				addr_long = int(remoteAddressUdp,16)
				remoteAddressUdp = socket.inet_ntoa(struct.pack("<L", addr_long))

				try:
					dns = socket.gethostbyaddr(remoteAddressUdp)
					success = True
				except socket.herror:
					success = False;
					
				if success:
					remoteAddressUdp = dns[0]

				remoteAddressUdpPort = int(remoteAddressUdpPort,16)
	
				networkData[udpData[9]] = [str(localAddressUdp)+":"+str(localAddressUdpPort),str(remoteAddressUdp)+":"+str(remoteAddressUdpPort)]
			i += 1
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
						if str(username) == "*" or re.search(str(username),str(userMapping.get(int(statusData[8].split()[1])))):	
							for fds in os.listdir(processPath+"fd"):						
								getInodes = ""
								try:
									getInodes = os.readlink(os.path.join(processPath+"fd",fds))
								except OSError:
									continue;
								if getInodes.startswith("socket:"):
									iNode = getInodes.split(":")[1][1:-1]
									if networkData.get(iNode):
										localAddress = networkData[iNode][0]
										remoteAddress = networkData[iNode][1]
										if (re.search(str(localAddFilter),str(localAddress)) or localAddFilter == ""):
											if (re.search(str(remoteAddFilter),str(remoteAddress)) or remoteAddFilter == ""): 
												network_total_stat.append([userMapping.get(int(statusData[8].split()[1])),pname,localAddress,remoteAddress])					
												if userFilter == "" and processFilter == "" and localAddFilter == "" and remoteAddFilter=="":
																self.fillArchiveTableNetwork.createLogForNetwork(network_total_stat,False,"")
							
			except IOError:		
				continue;
	if(len(self.userName_SearchBox.text()) == 0 and len(self.processName_SearchBox.text()) == 0 and len(self.localAddress_SearchBox.text()) == 0 and len(self.remoteAddress_SearchBox.text()) == 0):
		self.createTable(network_total_stat)

	return network_total_stat

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Network_IO_Form()
	ex.show()	
