# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registration.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Students_health_records_registration_ui(object):
    def setupUi(self, Students_health_records_registration_ui):
        Students_health_records_registration_ui.setObjectName("Students_health_records_registration_ui")
        Students_health_records_registration_ui.resize(348, 333)
        Students_health_records_registration_ui.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Students_health_records/ui/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Students_health_records_registration_ui.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label.setGeometry(QtCore.QRect(9, 9, 50, 16))
        self.label.setObjectName("label")
        self.lineEdit_first_name = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(110, 8, 210, 20))
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")
        self.First_name_error = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.First_name_error.setGeometry(QtCore.QRect(110, 34, 211, 16))
        self.First_name_error.setText("")
        self.First_name_error.setObjectName("First_name_error")
        self.label_2 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_2.setGeometry(QtCore.QRect(9, 67, 49, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_last_name = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(110, 66, 210, 20))
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")
        self.Last_name_error = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.Last_name_error.setGeometry(QtCore.QRect(110, 92, 211, 16))
        self.Last_name_error.setText("")
        self.Last_name_error.setObjectName("Last_name_error")
        self.label_3 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_3.setGeometry(QtCore.QRect(9, 126, 54, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_username = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_username.setGeometry(QtCore.QRect(110, 125, 210, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.User_name_error = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.User_name_error.setGeometry(QtCore.QRect(110, 151, 211, 16))
        self.User_name_error.setText("")
        self.User_name_error.setObjectName("User_name_error")
        self.label_4 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_4.setGeometry(QtCore.QRect(9, 184, 52, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_password = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_password.setGeometry(QtCore.QRect(110, 183, 210, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.Password_error = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.Password_error.setGeometry(QtCore.QRect(110, 209, 211, 16))
        self.Password_error.setText("")
        self.Password_error.setObjectName("Password_error")
        self.label_5 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_5.setGeometry(QtCore.QRect(9, 243, 30, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_Email = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_Email.setGeometry(QtCore.QRect(110, 242, 210, 20))
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.Emai_error = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.Emai_error.setGeometry(QtCore.QRect(110, 268, 16, 16))
        self.Emai_error.setText("")
        self.Emai_error.setObjectName("Emai_error")
        self.sign_up_button = QtWidgets.QPushButton(Students_health_records_registration_ui)
        self.sign_up_button.setGeometry(QtCore.QRect(110, 300, 75, 23))
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_in_button = QtWidgets.QPushButton(Students_health_records_registration_ui)
        self.sign_in_button.setGeometry(QtCore.QRect(240, 300, 75, 23))
        self.sign_in_button.setObjectName("sign_in_button")

        self.retranslateUi(Students_health_records_registration_ui)
        QtCore.QMetaObject.connectSlotsByName(Students_health_records_registration_ui)

    def retranslateUi(self, Students_health_records_registration_ui):
        _translate = QtCore.QCoreApplication.translate
        Students_health_records_registration_ui.setWindowTitle(_translate("Students_health_records_registration_ui", "Students_health_records"))
        self.label.setText(_translate("Students_health_records_registration_ui", "First name"))
        self.label_2.setText(_translate("Students_health_records_registration_ui", "Last name"))
        self.label_3.setText(_translate("Students_health_records_registration_ui", "Username*"))
        self.label_4.setText(_translate("Students_health_records_registration_ui", "Password*"))
        self.label_5.setText(_translate("Students_health_records_registration_ui", "Email*"))
        self.sign_up_button.setText(_translate("Students_health_records_registration_ui", "Confirm"))
        self.sign_in_button.setText(_translate("Students_health_records_registration_ui", "Back"))

