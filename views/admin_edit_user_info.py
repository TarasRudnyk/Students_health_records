# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin3.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student_health_records(object):
    def setupUi(self, Student_health_records):
        Student_health_records.setObjectName("Student_health_records")
        Student_health_records.resize(704, 483)
        Student_health_records.setMinimumSize(QtCore.QSize(704, 483))
        Student_health_records.setMaximumSize(QtCore.QSize(704, 483))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Student_health_records.setWindowIcon(icon)
        self.save_button = QtWidgets.QPushButton(Student_health_records)
        self.save_button.setGeometry(QtCore.QRect(580, 20, 75, 23))
        self.save_button.setObjectName("save_button")
        self.diagnose_label = QtWidgets.QLabel(Student_health_records)
        self.diagnose_label.setGeometry(QtCore.QRect(360, 10, 61, 41))
        self.diagnose_label.setObjectName("diagnose_label")
        self.add_new_button = QtWidgets.QPushButton(Student_health_records)
        self.add_new_button.setGeometry(QtCore.QRect(440, 20, 111, 21))
        self.add_new_button.setObjectName("add_new_button")
        self.diagnose_textEdit = QtWidgets.QTextEdit(Student_health_records)
        self.diagnose_textEdit.setGeometry(QtCore.QRect(360, 80, 295, 61))
        self.diagnose_textEdit.setObjectName("diagnose_textEdit")
        self.name_error = QtWidgets.QLabel(Student_health_records)
        self.name_error.setGeometry(QtCore.QRect(49, 86, 211, 16))
        self.name_error.setObjectName("name_error")
        self.card_number_error = QtWidgets.QLabel(Student_health_records)
        self.card_number_error.setGeometry(QtCore.QRect(49, 136, 211, 16))
        self.card_number_error.setText("")
        self.card_number_error.setObjectName("card_number_error")
        self.group_error = QtWidgets.QLabel(Student_health_records)
        self.group_error.setGeometry(QtCore.QRect(49, 185, 211, 16))
        self.group_error.setText("")
        self.group_error.setObjectName("group_error")
        self.email_error = QtWidgets.QLabel(Student_health_records)
        self.email_error.setGeometry(QtCore.QRect(49, 235, 211, 16))
        self.email_error.setText("")
        self.email_error.setObjectName("email_error")
        self.phone_number_error = QtWidgets.QLabel(Student_health_records)
        self.phone_number_error.setGeometry(QtCore.QRect(49, 286, 211, 16))
        self.phone_number_error.setText("")
        self.phone_number_error.setObjectName("phone_number_error")
        self.full_name_lineEdit = QtWidgets.QLineEdit(Student_health_records)
        self.full_name_lineEdit.setEnabled(True)
        self.full_name_lineEdit.setGeometry(QtCore.QRect(50, 66, 210, 20))
        self.full_name_lineEdit.setInputMask("")
        self.full_name_lineEdit.setText("")
        self.full_name_lineEdit.setMaxLength(30)
        self.full_name_lineEdit.setFrame(True)
        self.full_name_lineEdit.setDragEnabled(False)
        self.full_name_lineEdit.setClearButtonEnabled(True)
        self.full_name_lineEdit.setObjectName("full_name_lineEdit")
        self.card_number_lineEdit = QtWidgets.QLineEdit(Student_health_records)
        self.card_number_lineEdit.setGeometry(QtCore.QRect(50, 117, 210, 20))
        self.card_number_lineEdit.setText("")
        self.card_number_lineEdit.setMaxLength(8)
        self.card_number_lineEdit.setClearButtonEnabled(True)
        self.card_number_lineEdit.setObjectName("card_number_lineEdit")
        self.group_lineEdit = QtWidgets.QLineEdit(Student_health_records)
        self.group_lineEdit.setGeometry(QtCore.QRect(50, 168, 210, 20))
        self.group_lineEdit.setText("")
        self.group_lineEdit.setMaxLength(6)
        self.group_lineEdit.setClearButtonEnabled(True)
        self.group_lineEdit.setObjectName("group_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(Student_health_records)
        self.email_lineEdit.setGeometry(QtCore.QRect(50, 219, 210, 20))
        self.email_lineEdit.setText("")
        self.email_lineEdit.setMaxLength(30)
        self.email_lineEdit.setClearButtonEnabled(True)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.phone_number_lineEdit = QtWidgets.QLineEdit(Student_health_records)
        self.phone_number_lineEdit.setGeometry(QtCore.QRect(50, 270, 210, 20))
        self.phone_number_lineEdit.setClearButtonEnabled(True)
        self.phone_number_lineEdit.setObjectName("phone_number_lineEdit")
        self.full_name_label = QtWidgets.QLabel(Student_health_records)
        self.full_name_label.setGeometry(QtCore.QRect(50, 50, 141, 16))
        self.full_name_label.setObjectName("full_name_label")
        self.card_number_label = QtWidgets.QLabel(Student_health_records)
        self.card_number_label.setGeometry(QtCore.QRect(50, 100, 121, 16))
        self.card_number_label.setObjectName("card_number_label")
        self.group_label = QtWidgets.QLabel(Student_health_records)
        self.group_label.setGeometry(QtCore.QRect(50, 150, 131, 16))
        self.group_label.setObjectName("group_label")
        self.email_label = QtWidgets.QLabel(Student_health_records)
        self.email_label.setGeometry(QtCore.QRect(50, 200, 141, 16))
        self.email_label.setObjectName("email_label")
        self.phone_number_label = QtWidgets.QLabel(Student_health_records)
        self.phone_number_label.setGeometry(QtCore.QRect(50, 250, 141, 16))
        self.phone_number_label.setObjectName("phone_number_label")
        self.back_to_info_view_pushButton = QtWidgets.QPushButton(Student_health_records)
        self.back_to_info_view_pushButton.setGeometry(QtCore.QRect(50, 390, 211, 23))
        self.back_to_info_view_pushButton.setObjectName("back_to_info_view_pushButton")
        self.confirm_pushButton = QtWidgets.QPushButton(Student_health_records)
        self.confirm_pushButton.setGeometry(QtCore.QRect(50, 310, 211, 23))
        self.confirm_pushButton.setObjectName("confirm_pushButton")

        self.retranslateUi(Student_health_records)
        QtCore.QMetaObject.connectSlotsByName(Student_health_records)

    def retranslateUi(self, Student_health_records):
        _translate = QtCore.QCoreApplication.translate
        Student_health_records.setWindowTitle(_translate("Student_health_records", "Student health records"))
        self.save_button.setText(_translate("Student_health_records", "Save"))
        self.diagnose_label.setText(_translate("Student_health_records", "Diagnoses:"))
        self.add_new_button.setText(_translate("Student_health_records", "Add new"))
        self.diagnose_textEdit.setPlaceholderText(_translate("Student_health_records", "please write diagnose here."))
        self.name_error.setText(_translate("Student_health_records", "<html><head/><body><p><br/></p></body></html>"))
        self.full_name_lineEdit.setPlaceholderText(_translate("Student_health_records", "Rudnyk Taras "))
        self.card_number_lineEdit.setPlaceholderText(_translate("Student_health_records", "12345678"))
        self.group_lineEdit.setPlaceholderText(_translate("Student_health_records", "km23"))
        self.email_lineEdit.setPlaceholderText(_translate("Student_health_records", "tarasrudnyk@gmail.com"))
        self.phone_number_lineEdit.setInputMask(_translate("Student_health_records", "+38\\0(00)-000-00-00"))
        self.phone_number_lineEdit.setText(_translate("Student_health_records", "+380()---"))
        self.phone_number_lineEdit.setPlaceholderText(_translate("Student_health_records", "+380954659168"))
        self.full_name_label.setText(_translate("Student_health_records", "Full name"))
        self.card_number_label.setText(_translate("Student_health_records", "Card number"))
        self.group_label.setText(_translate("Student_health_records", "Group"))
        self.email_label.setText(_translate("Student_health_records", "Email"))
        self.phone_number_label.setText(_translate("Student_health_records", "Phone number"))
        self.back_to_info_view_pushButton.setText(_translate("Student_health_records", "Back to information view"))
        self.confirm_pushButton.setText(_translate("Student_health_records", "Confirm"))

