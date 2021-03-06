# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_user.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addUserWindow(object):
    def setupUi(self, addUserWindow):
        addUserWindow.setObjectName("addUserWindow")
        addUserWindow.setWindowModality(QtCore.Qt.NonModal)
        addUserWindow.resize(366, 385)
        addUserWindow.setMinimumSize(QtCore.QSize(366, 385))
        addUserWindow.setMaximumSize(QtCore.QSize(366, 385))
        addUserWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addUserWindow.setWindowIcon(icon)
        self.card_number_label = QtWidgets.QLabel(addUserWindow)
        self.card_number_label.setGeometry(QtCore.QRect(19, 28, 71, 16))
        self.card_number_label.setObjectName("card_number_label")
        self.card_number_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.card_number_lineEdit.setGeometry(QtCore.QRect(130, 28, 210, 20))
        self.card_number_lineEdit.setText("")
        self.card_number_lineEdit.setMaxLength(8)
        self.card_number_lineEdit.setClearButtonEnabled(True)
        self.card_number_lineEdit.setObjectName("card_number_lineEdit")
        self.card_number_lineEdit.setInputMask("00000000")
        self.full_name_label = QtWidgets.QLabel(addUserWindow)
        self.full_name_label.setGeometry(QtCore.QRect(19, 73, 56, 16))
        self.full_name_label.setObjectName("full_name_label")
        self.full_name_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.full_name_lineEdit.setGeometry(QtCore.QRect(130, 73, 210, 20))
        self.full_name_lineEdit.setMaxLength(28)
        self.full_name_lineEdit.setClearButtonEnabled(True)
        self.full_name_lineEdit.setObjectName("full_name_lineEdit")
        self.group_label = QtWidgets.QLabel(addUserWindow)
        self.group_label.setGeometry(QtCore.QRect(19, 116, 55, 16))
        self.group_label.setObjectName("group_label")
        self.group_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.group_lineEdit.setGeometry(QtCore.QRect(130, 116, 210, 20))
        # self.group_lineEdit.setMaxLength(4)
        self.group_lineEdit.setInputMask("aa00")
        self.group_lineEdit.setClearButtonEnabled(True)
        self.group_lineEdit.setObjectName("group_lineEdit")
        self.username_label = QtWidgets.QLabel(addUserWindow)
        self.username_label.setGeometry(QtCore.QRect(19, 210, 54, 16))
        self.username_label.setObjectName("username_label")
        self.username_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.username_lineEdit.setGeometry(QtCore.QRect(130, 210, 210, 20))
        self.username_lineEdit.setMaxLength(28)
        self.username_lineEdit.setClearButtonEnabled(True)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password_label = QtWidgets.QLabel(addUserWindow)
        self.password_label.setGeometry(QtCore.QRect(19, 255, 52, 16))
        self.password_label.setObjectName("password_label")
        self.password_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.password_lineEdit.setGeometry(QtCore.QRect(130, 255, 210, 20))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setMaxLength(28)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_lineEdit.setClearButtonEnabled(True)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.email_label = QtWidgets.QLabel(addUserWindow)
        self.email_label.setGeometry(QtCore.QRect(19, 300, 30, 16))
        self.email_label.setObjectName("email_label")
        self.email_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.email_lineEdit.setGeometry(QtCore.QRect(130, 300, 210, 20))
        self.email_lineEdit.setMaxLength(28)
        self.email_lineEdit.setClearButtonEnabled(True)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.ok_cancel_buttonBox = QtWidgets.QDialogButtonBox(addUserWindow)
        self.ok_cancel_buttonBox.setGeometry(QtCore.QRect(130, 350, 211, 23))
        self.ok_cancel_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_cancel_buttonBox.setObjectName("ok_cancel_buttonBox")
        self.phone_number_lineEdit = QtWidgets.QLineEdit(addUserWindow)
        self.phone_number_lineEdit.setGeometry(QtCore.QRect(130, 159, 210, 20))
        self.phone_number_lineEdit.setInputMask("0000000000")
        self.phone_number_lineEdit.setClearButtonEnabled(True)
        self.phone_number_lineEdit.setObjectName("phone_number_lineEdit")
        self.phone_number_label = QtWidgets.QLabel(addUserWindow)
        self.phone_number_label.setGeometry(QtCore.QRect(20, 159, 81, 16))
        self.phone_number_label.setObjectName("phone_number_label")
        self.card_number_error = QtWidgets.QLabel(addUserWindow)
        self.card_number_error.setGeometry(QtCore.QRect(131, 47, 210, 13))
        self.card_number_error.setObjectName("card_number_error")
        self.full_name_error = QtWidgets.QLabel(addUserWindow)
        self.full_name_error.setGeometry(QtCore.QRect(131, 93, 210, 13))
        self.full_name_error.setText("")
        self.full_name_error.setObjectName("full_name_error")
        self.phone_number_error = QtWidgets.QLabel(addUserWindow)
        self.phone_number_error.setGeometry(QtCore.QRect(131, 180, 210, 13))
        self.phone_number_error.setText("")
        self.phone_number_error.setObjectName("phone_number_error")
        self.group_error = QtWidgets.QLabel(addUserWindow)
        self.group_error.setGeometry(QtCore.QRect(131, 137, 210, 13))
        self.group_error.setText("")
        self.group_error.setObjectName("group_error")
        self.username_error = QtWidgets.QLabel(addUserWindow)
        self.username_error.setGeometry(QtCore.QRect(131, 230, 210, 13))
        self.username_error.setText("")
        self.username_error.setObjectName("username_error")
        self.password_error = QtWidgets.QLabel(addUserWindow)
        self.password_error.setGeometry(QtCore.QRect(131, 275, 210, 13))
        self.password_error.setText("")
        self.password_error.setObjectName("password_error")
        self.email_error = QtWidgets.QLabel(addUserWindow)
        self.email_error.setGeometry(QtCore.QRect(131, 320, 210, 13))
        self.email_error.setText("")
        self.email_error.setObjectName("email_error")
        self.group_lineEdit.raise_()
        self.card_number_label.raise_()
        self.card_number_lineEdit.raise_()
        self.full_name_label.raise_()
        self.full_name_lineEdit.raise_()
        self.group_label.raise_()
        self.username_label.raise_()
        self.username_lineEdit.raise_()
        self.password_label.raise_()
        self.password_lineEdit.raise_()
        self.email_label.raise_()
        self.email_lineEdit.raise_()
        self.ok_cancel_buttonBox.raise_()
        self.phone_number_lineEdit.raise_()
        self.phone_number_label.raise_()
        self.card_number_error.raise_()
        self.full_name_error.raise_()
        self.phone_number_error.raise_()
        self.group_error.raise_()
        self.username_error.raise_()
        self.password_error.raise_()
        self.email_error.raise_()

        self.retranslateUi(addUserWindow)
        QtCore.QMetaObject.connectSlotsByName(addUserWindow)

    def retranslateUi(self, addUserWindow):
        _translate = QtCore.QCoreApplication.translate
        addUserWindow.setWindowTitle(_translate("addUserWindow", "Student health Add user - Admin"))
        self.card_number_label.setText(_translate("addUserWindow", "Card number*"))
        self.card_number_lineEdit.setPlaceholderText(_translate("addUserWindow", "12345678"))
        self.full_name_label.setText(_translate("addUserWindow", "Full name*"))
        self.full_name_lineEdit.setPlaceholderText(_translate("addUserWindow", "Taras Rudnyk"))
        self.group_label.setText(_translate("addUserWindow", "Group*"))
        self.group_lineEdit.setPlaceholderText(_translate("addUserWindow", "km23"))
        self.username_label.setText(_translate("addUserWindow", "Username*"))
        self.username_lineEdit.setPlaceholderText(_translate("addUserWindow", "TarasRudnyk"))
        self.password_label.setText(_translate("addUserWindow", "Password*"))
        self.password_lineEdit.setPlaceholderText(_translate("addUserWindow", "my_password"))
        self.email_label.setText(_translate("addUserWindow", "Email"))
        self.email_lineEdit.setPlaceholderText(_translate("addUserWindow", "TarasRudnyk@gmail.com"))
        self.phone_number_lineEdit.setPlaceholderText(_translate("addUserWindow", "0954659168"))
        self.phone_number_label.setText(_translate("addUserWindow", "Phone number"))
        self.card_number_error.setText(_translate("addUserWindow", "<html><head/><body><p><br/></p></body></html>"))

