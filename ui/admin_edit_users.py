# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_edit_users.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student_health_records(object):
    def setupUi(self, Student_health_records):
        Student_health_records.setObjectName("Student_health_records")
        Student_health_records.resize(704, 483)
        self.pushButton = QtWidgets.QPushButton(Student_health_records)
        self.pushButton.setGeometry(QtCore.QRect(580, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Student_health_records)
        self.label.setGeometry(QtCore.QRect(360, 10, 61, 41))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Student_health_records)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 20, 111, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Student_health_records)
        self.textEdit.setGeometry(QtCore.QRect(360, 80, 295, 61))
        self.textEdit.setObjectName("textEdit")
        self.name_error = QtWidgets.QLabel(Student_health_records)
        self.name_error.setGeometry(QtCore.QRect(50, 46, 211, 16))
        self.name_error.setText("")
        self.name_error.setObjectName("name_error")
        self.card_number_error = QtWidgets.QLabel(Student_health_records)
        self.card_number_error.setGeometry(QtCore.QRect(50, 96, 211, 16))
        self.card_number_error.setText("")
        self.card_number_error.setObjectName("card_number_error")
        self.group_error = QtWidgets.QLabel(Student_health_records)
        self.group_error.setGeometry(QtCore.QRect(50, 145, 211, 16))
        self.group_error.setText("")
        self.group_error.setObjectName("group_error")
        self.email_error = QtWidgets.QLabel(Student_health_records)
        self.email_error.setGeometry(QtCore.QRect(50, 195, 211, 16))
        self.email_error.setText("")
        self.email_error.setObjectName("email_error")
        self.phone_number_error = QtWidgets.QLabel(Student_health_records)
        self.phone_number_error.setGeometry(QtCore.QRect(50, 246, 211, 16))
        self.phone_number_error.setText("")
        self.phone_number_error.setObjectName("phone_number_error")
        self.lineEdit_name = QtWidgets.QLineEdit(Student_health_records)
        self.lineEdit_name.setEnabled(True)
        self.lineEdit_name.setGeometry(QtCore.QRect(51, 26, 210, 20))
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setFrame(True)
        self.lineEdit_name.setDragEnabled(False)
        self.lineEdit_name.setPlaceholderText("")
        self.lineEdit_name.setClearButtonEnabled(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_card_number = QtWidgets.QLineEdit(Student_health_records)
        self.lineEdit_card_number.setGeometry(QtCore.QRect(51, 77, 210, 20))
        self.lineEdit_card_number.setText("")
        self.lineEdit_card_number.setClearButtonEnabled(True)
        self.lineEdit_card_number.setObjectName("lineEdit_card_number")
        self.lineEdit_group = QtWidgets.QLineEdit(Student_health_records)
        self.lineEdit_group.setGeometry(QtCore.QRect(51, 128, 210, 20))
        self.lineEdit_group.setText("")
        self.lineEdit_group.setClearButtonEnabled(True)
        self.lineEdit_group.setObjectName("lineEdit_group")
        self.lineEdit_email = QtWidgets.QLineEdit(Student_health_records)
        self.lineEdit_email.setGeometry(QtCore.QRect(51, 179, 210, 20))
        self.lineEdit_email.setText("")
        self.lineEdit_email.setClearButtonEnabled(True)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_phone_number = QtWidgets.QLineEdit(Student_health_records)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(51, 230, 210, 20))
        self.lineEdit_phone_number.setText("")
        self.lineEdit_phone_number.setClearButtonEnabled(True)
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")

        self.retranslateUi(Student_health_records)
        QtCore.QMetaObject.connectSlotsByName(Student_health_records)

    def retranslateUi(self, Student_health_records):
        _translate = QtCore.QCoreApplication.translate
        Student_health_records.setWindowTitle(_translate("Student_health_records", "Student_health_records"))
        self.pushButton.setText(_translate("Student_health_records", "Save"))
        self.label.setText(_translate("Student_health_records", "Diagnoses:"))
        self.pushButton_2.setText(_translate("Student_health_records", "Add new"))

