from PyQt5 import QtCore, QtGui, QtWidgets
from cryptography.fernet import Fernet
import mysql.connector, threading, Recoil, os, subprocess, time, Overlay

class Ui_MainWindow(object):
    def __login(self):
        encH = b'' #SQL Conn Host Encrypted
        encU = b'' #SQL Conn Username Encrypted
        encPW = b'' #SQL Conn Password Encrypted
        encDB = b'' #SQL Conn DB IP Encrypted

        UlXJn8jT = b'' #Encryption Key
        naviFer = Fernet(UlXJn8jT) #Encryption Class Init

        __hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip() #Get HWID from users PC
        __u = self.txtUser.text()
        __p = self.txtPass.text()
        #__u = naviFer.encrypt(self.txtUser.text().encode())
        #__p = naviFer.encrypt(self.txtPass.text().encode())

        if __u and __p:
            __mydb = mysql.connector.connect(
            host = str(naviFer.decrypt(encH))[2:-1], #SQL Conn Host Decrypted
            user = str(naviFer.decrypt(encU))[2:-1], #SQL Username Decrypted
            password = str(naviFer.decrypt(encPW))[2:-1], #SQL password Decrypted
            database = str(naviFer.decrypt(encDB))[2:-1] #SQL DB ip Decrypted
            )

            __mycursor = __mydb.cursor()
            __mycursor.execute("SELECT `id` FROM `LoginList` WHERE `user` = '"+ __u +"' AND `key` = '"+ __p +"'") #Get id from user and pass
            __id = __mycursor.fetchall()

            if (__id == []): #If id was not found
                self.lblStatus.setText("Login Failed")
            else: #If id exists in db
                __mycursor.execute("SELECT `id` FROM `LoginList` WHERE `user` = '"+ __u +"' AND `key` = '"+ __p +"' AND `hwid` = '"+ __hwid +"'") # Grab id if HWID exists from db from user and pass
                __idHWID = __mycursor.fetchall()
                if (__idHWID == []): # If no id found with that hwid
                    __mycursor.execute("UPDATE `LoginList` SET HWID = '"+ __hwid +"', reg_date = current_timestamp() WHERE id = '"+ str(__id[0][0]) +"';") # Update the hwid
                else: # If HWID is set
                    __mycursor.execute("SELECT `hwid` FROM `LoginList` WHERE `user` = '"+ __u +"' AND `key` = '"+ __p +"' AND '"+ __hwid +"'") # HWID
                    __HWID = __mycursor.fetchall()
                    if (__HWID[0][0] != __hwid): #Check user hwid vs stored hwid
                        self.lblStatus.setText("Login Failed")
                        time.sleep(2)
                        sys.exit()
                #overlayThread = threading.Thread(target=Overlay.draw)
                #overlayThread.start()
                scriptThread = threading.Thread(target=Recoil.run) #Start Script
                self.lblStatus.setText("Logged In")
                self.hide()
                scriptThread.start()
                scriptThread.join()
                #overlayThread.join()
            threading.Timer(2.5, sys.exit()).start()

    def __register(self):
        encH = b'' #SQL Conn Host
        encU = b'' #SQL Conn Username
        encPW = b'' #SQL Conn Password
        encDB = b'' #SQL Conn DB IP

        UlXJn8jT = b'' #Encryption Key
        naviFer = Fernet(UlXJn8jT) #Encryption Class Init

        __hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        __u = self.txtUser.text()
        __p = self.txtPass.text()

        if __u and __p:
            __mydb = mysql.connector.connect(
            host = str(naviFer.decrypt(encH))[2:-1], #SQL Conn Host Decrypted
            user = str(naviFer.decrypt(encU))[2:-1], #SQL Username Decrypted
            password = str(naviFer.decrypt(encPW))[2:-1], #SQL password Decrypted
            database = str(naviFer.decrypt(encDB))[2:-1] #SQL DB ip Decrypted
            )

            __mycursor = __mydb.cursor()
            __mycursor.execute("SELECT `key` FROM `LoginList` WHERE `key` = '"+ __p +"'") #Check key is valid
            __id = __mycursor.fetchall()

            if (__id == []): #If key was not found
                self.lblStatus.setText("Invalid Key")
            else: #If key exists
                __mycursor.execute("UPDATE `LoginList` SET `hwid` = '"+ __hwid +"', `user` = '"+ __u +"' , `reg_date` = current_timestamp() WHERE `key` = '"+ __p +"';")
                self.lblStatus.setText("Registered")
            threading.Timer(2.5, sys.exit()).start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 250))
        MainWindow.setMaximumSize(QtCore.QSize(600, 250))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:rgb(56, 56, 56)\n"
"}")
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(260, 202, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.btnRegister.setObjectName("btnRegister")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(260, 162, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.btnLogin.setCheckable(False)
        self.btnLogin.setObjectName("btnLogin")
        self.lblMain = QtWidgets.QLabel(self.centralwidget)
        self.lblMain.setGeometry(QtCore.QRect(160, 0, 281, 81))
        font = QtGui.QFont()
        font.setFamily("Akira Expanded")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lblMain.setFont(font)
        self.lblMain.setAutoFillBackground(False)
        self.lblMain.setStyleSheet("color:white;")
        self.lblMain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMain.setObjectName("lblMain")
        self.txtPass = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPass.setGeometry(QtCore.QRect(240, 121, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.txtPass.setFont(font)
        self.txtPass.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.txtPass.setText("")
        self.txtPass.setFrame(True)
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPass.setClearButtonEnabled(False)
        self.txtPass.setObjectName("txtPass")
        self.txtUser = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(240, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.txtUser.setFont(font)
        self.txtUser.setStyleSheet("background-color:Transparent;\n"
"border:1px solid white;\n"
"color:white;")
        self.txtUser.setText("")
        self.txtUser.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUser.setObjectName("txtUser")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(3, 210, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(10)
        self.lblStatus.setFont(font)
        self.lblStatus.setStyleSheet("color:white;")
        self.lblStatus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblStatus.setObjectName("lblStatus")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 600, 6))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(600, 10))
        self.frame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231, 60, 126, 255), stop:1 rgba(35, 166, 213, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(0, 244, 600, 8))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame2.setMaximumSize(QtCore.QSize(600, 10))
        self.frame2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231, 60, 126, 255), stop:1 rgba(35, 166, 213, 255))")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(581, 2, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Pixel Font7")
        font.setPointSize(12)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("background-color:Transparent;\n"
"color:White;")
        self.btnExit.setObjectName("btnExit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtUser, self.txtPass)
        MainWindow.setTabOrder(self.txtPass, self.btnLogin)
        MainWindow.setTabOrder(self.btnLogin, self.btnRegister)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy4.me"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.lblMain.setText(_translate("MainWindow", "Easy4.me"))
        self.txtPass.setPlaceholderText(_translate("MainWindow", "Key"))
        self.txtUser.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lblStatus.setText(_translate("MainWindow", "Status"))
        self.btnExit.setText(_translate("MainWindow", "X"))

        #Button Event
        self.btnLogin.clicked.connect(self.__login)
        self.btnRegister.clicked.connect(self.__register)
        self.btnExit.clicked.connect(self.close)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec_())
