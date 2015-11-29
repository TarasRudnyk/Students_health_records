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
        Student_health_records.resize(704, 637)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Student_health_records.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Student_health_records)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        Student_health_records.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Student_health_records)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Student_health_records.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Student_health_records)
        self.statusbar.setObjectName("statusbar")
        Student_health_records.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Student_health_records)
        self.actionOpen.setEnabled(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Student_health_records)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(Student_health_records)
        self.actionSave_as.setEnabled(False)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLog_out = QtWidgets.QAction(Student_health_records)
        self.actionLog_out.setObjectName("actionLog_out")
        self.Help_Student_health_records_action = QtWidgets.QAction(Student_health_records)
        self.Help_Student_health_records_action.setEnabled(False)
        self.Help_Student_health_records_action.setObjectName("Help_Student_health_records_action")
        self.About_Student_health_records_action = QtWidgets.QAction(Student_health_records)
        self.About_Student_health_records_action.setObjectName("About_Student_health_records_action")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionLog_out)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.Help_Student_health_records_action)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.About_Student_health_records_action)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Student_health_records)
        QtCore.QMetaObject.connectSlotsByName(Student_health_records)

    def retranslateUi(self, Student_health_records):
        _translate = QtCore.QCoreApplication.translate
        Student_health_records.setWindowTitle(_translate("Student_health_records", "Student health records"))
        self.menuFile.setTitle(_translate("Student_health_records", "File"))
        self.menuAbout.setTitle(_translate("Student_health_records", "Help"))
        self.actionOpen.setText(_translate("Student_health_records", "Open"))
        self.actionSave.setText(_translate("Student_health_records", "Save"))
        self.actionSave_as.setText(_translate("Student_health_records", "Save as..."))
        self.actionLog_out.setText(_translate("Student_health_records", "Log out"))
        self.Help_Student_health_records_action.setText(_translate("Student_health_records", "Help Student health records"))
        self.About_Student_health_records_action.setText(_translate("Student_health_records", "About Student health records"))

