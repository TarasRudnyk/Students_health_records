# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student_health_records(object):
    def setupUi(self, Student_health_records):
        Student_health_records.setObjectName("Student_health_records")
        Student_health_records.resize(584, 427)
        self.pushButton_2 = QtWidgets.QPushButton(Student_health_records)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 12, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(Student_health_records)
        self.tableView.setGeometry(QtCore.QRect(180, 10, 361, 401))
        self.tableView.setObjectName("tableView")
        self.pushButton_3 = QtWidgets.QPushButton(Student_health_records)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 390, 81, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Student_health_records)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 41, 81, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Student_health_records)
        self.comboBox.setGeometry(QtCore.QRect(30, 70, 81, 21))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Student_health_records)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 16, 21))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Student_health_records)
        QtCore.QMetaObject.connectSlotsByName(Student_health_records)

    def retranslateUi(self, Student_health_records):
        _translate = QtCore.QCoreApplication.translate
        Student_health_records.setWindowTitle(_translate("Student_health_records", "Student_health_records"))
        self.pushButton_2.setText(_translate("Student_health_records", "Show_my_info"))
        self.pushButton_3.setText(_translate("Student_health_records", "Show_diseases"))
        self.pushButton_4.setText(_translate("Student_health_records", "Add simptome"))
        self.pushButton.setText(_translate("Student_health_records", "X"))

