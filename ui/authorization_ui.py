# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Students_health_records_authorization(object):
    def setupUi(self, Students_health_records_authorization):
        Students_health_records_authorization.setObjectName("Students_health_records_authorization")
        Students_health_records_authorization.resize(400, 300)
        Students_health_records_authorization.setAccessibleName("")
        self.label = QtWidgets.QLabel(Students_health_records_authorization)
        self.label.setGeometry(QtCore.QRect(50, 60, 50, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Students_health_records_authorization)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 50, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Students_health_records_authorization)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Students_health_records_authorization)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 110, 200, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.log_in_button = QtWidgets.QPushButton(Students_health_records_authorization)
        self.log_in_button.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.log_in_button.setObjectName("log_in_button")
        self.label_3 = QtWidgets.QLabel(Students_health_records_authorization)
        self.label_3.setGeometry(QtCore.QRect(140, 210, 121, 31))
        self.label_3.setObjectName("label_3")
        self.sign_up_button = QtWidgets.QPushButton(Students_health_records_authorization)
        self.sign_up_button.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.sign_up_button.setObjectName("sign_up_button")


        self.retranslateUi(Students_health_records_authorization)
        QtCore.QMetaObject.connectSlotsByName(Students_health_records_authorization)

    def retranslateUi(self, Students_health_records_authorization):
        _translate = QtCore.QCoreApplication.translate
        Students_health_records_authorization.setWindowTitle(_translate("Students_health_records_authorization", "Students_health_records_authorization"))
        self.label.setText(_translate("Students_health_records_authorization", "Username"))
        self.label_2.setText(_translate("Students_health_records_authorization", "Password"))
        self.log_in_button.setText(_translate("Students_health_records_authorization", "Log in"))
        self.label_3.setText(_translate("Students_health_records_authorization", "Forgot your password?"))
        self.sign_up_button.setText(_translate("Students_health_records_authorization", "Sign up"))

