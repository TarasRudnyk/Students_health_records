# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student_health_records(QtWidgets.QMainWindow):
    def setupUi(self, Student_health_records):
        Student_health_records.setObjectName("Student_health_records")
        Student_health_records.resize(770, 497)
        self.centralwidget = QtWidgets.QWidget(Student_health_records)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 711, 421))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(235)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 22, 240, 31))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "                           Card number")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setEnabled(True)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 22, 235, 31))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(504, 22, 237, 31))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        Student_health_records.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Student_health_records)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Student_health_records.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Student_health_records)
        self.statusbar.setObjectName("statusbar")
        Student_health_records.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Student_health_records)
        QtCore.QMetaObject.connectSlotsByName(Student_health_records)

    def retranslateUi(self, Student_health_records):
        _translate = QtCore.QCoreApplication.translate
        Student_health_records.setWindowTitle(_translate("Student_health_records", "MainWindow"))
        self.comboBox.setCurrentText(_translate("Student_health_records", "                           Card number"))
        self.comboBox_2.setItemText(0, _translate("Student_health_records", "                           Full name"))
        self.comboBox_3.setItemText(0, _translate("Student_health_records", "                              Group"))
        self.menuFile.setTitle(_translate("Student_health_records", "File"))
        self.menuEdit.setTitle(_translate("Student_health_records", "Edit"))
        self.menuHelp.setTitle(_translate("Student_health_records", "Help"))
        self.menuAbout.setTitle(_translate("Student_health_records", "About"))

