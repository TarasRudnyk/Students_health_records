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
        Students_health_records_registration_ui.resize(347, 300)
        self.gridLayout = QtWidgets.QGridLayout(Students_health_records_registration_ui)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(Students_health_records_registration_ui)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Students_health_records_registration_ui)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 2)
        self.sign_up_button = QtWidgets.QPushButton(Students_health_records_registration_ui)
        self.sign_up_button.setObjectName("sign_up_button")
        self.gridLayout.addWidget(self.sign_up_button, 5, 1, 1, 1)
        self.sign_in_button = QtWidgets.QPushButton(Students_health_records_registration_ui)
        self.sign_in_button.setObjectName("sign_in_button")
        self.gridLayout.addWidget(self.sign_in_button, 5, 2, 1, 1)

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
        self.sign_up_button.setText(_translate("Students_health_records_registration_ui", "Sign up"))
        self.sign_in_button.setText(_translate("Students_health_records_registration_ui", "Sign in"))

