# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        AuthorizationWindow.setObjectName("AuthorizationWindow")
        AuthorizationWindow.resize(355, 161)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AuthorizationWindow.sizePolicy().hasHeightForWidth())
        AuthorizationWindow.setSizePolicy(sizePolicy)
        AuthorizationWindow.setMinimumSize(QtCore.QSize(355, 161))
        AuthorizationWindow.setMaximumSize(QtCore.QSize(355, 161))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AuthorizationWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AuthorizationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_lineEdit.setGeometry(QtCore.QRect(117, 24, 200, 20))
        self.username_lineEdit.setMaximumSize(QtCore.QSize(201, 16777215))
        self.username_lineEdit.setMaxLength(24)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 67, 46, 16))
        self.password_label.setObjectName("password_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(117, 67, 201, 20))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(201, 16777215))
        self.password_lineEdit.setMaxLength(26)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(20, 24, 48, 16))
        self.username_label.setObjectName("username_label")
        self.log_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_button.setGeometry(QtCore.QRect(117, 110, 201, 23))
        self.log_in_button.setObjectName("log_in_button")
        self.show_pass_button = QtWidgets.QToolButton(self.centralwidget)
        self.show_pass_button.setEnabled(True)
        self.show_pass_button.setGeometry(QtCore.QRect(300, 67, 20, 20))
        self.show_pass_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("views/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_pass_button.setIcon(icon1)
        self.show_pass_button.setObjectName("show_pass_button")
        self.username_error_label = QtWidgets.QLabel(self.centralwidget)
        self.username_error_label.setGeometry(QtCore.QRect(117, 43, 400, 13))
        self.username_error_label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.username_error_label.setScaledContents(False)
        self.username_error_label.setObjectName("username_error_label")
        self.password_error_label = QtWidgets.QLabel(self.centralwidget)
        self.password_error_label.setGeometry(QtCore.QRect(117, 86, 400, 13))
        self.password_error_label.setObjectName("password_error_label")
        AuthorizationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AuthorizationWindow)
        self.statusbar.setObjectName("statusbar")
        AuthorizationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationWindow)

    def retranslateUi(self, AuthorizationWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationWindow.setWindowTitle(_translate("AuthorizationWindow", "Student health records"))
        self.username_lineEdit.setPlaceholderText(_translate("AuthorizationWindow", "username"))
        self.password_label.setText(_translate("AuthorizationWindow", "Password"))
        self.password_lineEdit.setPlaceholderText(_translate("AuthorizationWindow", "password"))
        self.username_label.setText(_translate("AuthorizationWindow", "Username"))
        self.log_in_button.setText(_translate("AuthorizationWindow", "Log in"))
        self.username_error_label.setText(_translate("AuthorizationWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.password_error_label.setText(_translate("AuthorizationWindow", "<html><head/><body><p><br/></p></body></html>"))

