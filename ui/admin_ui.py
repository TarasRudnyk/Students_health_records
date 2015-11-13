# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student_health_records(object):
    def setupUi(self, Student_health_records):
        Student_health_records.setObjectName("Student_health_records")
        Student_health_records.resize(646, 375)
        self.gridLayout = QtWidgets.QGridLayout(Student_health_records)
        self.gridLayout.setObjectName("gridLayout")
        self.select_user_2 = QtWidgets.QPushButton(Student_health_records)
        self.select_user_2.setObjectName("select_user_2")
        self.gridLayout.addWidget(self.select_user_2, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(Student_health_records)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 1, 6, 1)
        self.comboBox = QtWidgets.QComboBox(Student_health_records)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Student_health_records)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.add_diagnose = QtWidgets.QPushButton(Student_health_records)
        self.add_diagnose.setObjectName("add_diagnose")
        self.gridLayout.addWidget(self.add_diagnose, 3, 0, 1, 1)
        self.add_diagnose_2 = QtWidgets.QPushButton(Student_health_records)
        self.add_diagnose_2.setObjectName("add_diagnose_2")
        self.gridLayout.addWidget(self.add_diagnose_2, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Student_health_records)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)

        self.retranslateUi(Student_health_records)
        QtCore.QMetaObject.connectSlotsByName(Student_health_records)

    def retranslateUi(self, Student_health_records):
        _translate = QtCore.QCoreApplication.translate
        Student_health_records.setWindowTitle(_translate("Student_health_records", "Student_health_records"))
        self.select_user_2.setText(_translate("Student_health_records", "Add user"))
        self.comboBox.setItemText(0, _translate("Student_health_records", "Select user"))
        self.pushButton_2.setText(_translate("Student_health_records", "Show_info_about_user"))
        self.add_diagnose.setText(_translate("Student_health_records", "Add diagnose"))
        self.add_diagnose_2.setText(_translate("Student_health_records", "Remove diagnose"))
        self.pushButton_5.setText(_translate("Student_health_records", "Remove user"))

