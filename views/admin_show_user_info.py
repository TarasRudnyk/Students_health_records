# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin2.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminShowUsersMenu(object):
    def setupUi(self, AdminShowUsersMenu):
        AdminShowUsersMenu.setObjectName("AdminShowUsersMenu")
        AdminShowUsersMenu.setEnabled(True)
        AdminShowUsersMenu.resize(772, 526)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("views/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdminShowUsersMenu.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AdminShowUsersMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.add_user_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_user_pushButton.setObjectName("add_user_pushButton")
        self.gridLayout_3.addWidget(self.add_user_pushButton, 3, 0, 1, 1)
        self.delete_selected_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.delete_selected_pushButton.setEnabled(True)
        self.delete_selected_pushButton.setObjectName("delete_selected_pushButton")
        self.gridLayout_3.addWidget(self.delete_selected_pushButton, 3, 1, 1, 1)
        """
        self.user_info_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.user_info_tableWidget.setMinimumSize(QtCore.QSize(754, 412))
        self.user_info_tableWidget.setObjectName("user_info_tableWidget")
        self.user_info_tableWidget.setColumnCount(3)
        self.user_info_tableWidget.setRowCount(13)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.user_info_tableWidget.setHorizontalHeaderItem(2, item)
        self.user_info_tableWidget.horizontalHeader().setVisible(False)
        self.user_info_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.user_info_tableWidget.horizontalHeader().setDefaultSectionSize(235)
        self.user_info_tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.user_info_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.user_info_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.user_info_tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.user_info_tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.user_info_tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.user_info_tableWidget, 2, 0, 1, 3)
        """
        AdminShowUsersMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AdminShowUsersMenu)
        self.statusbar.setObjectName("statusbar")
        AdminShowUsersMenu.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(AdminShowUsersMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setTearOffEnabled(False)
        self.menuAbout.setObjectName("menuAbout")
        AdminShowUsersMenu.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(AdminShowUsersMenu)
        self.actionOpen.setEnabled(False)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(AdminShowUsersMenu)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(AdminShowUsersMenu)
        self.actionSave_as.setEnabled(False)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionLog_out = QtWidgets.QAction(AdminShowUsersMenu)
        self.actionLog_out.setObjectName("actionLog_out")
        self.actionAdd_new_user = QtWidgets.QAction(AdminShowUsersMenu)
        self.actionAdd_new_user.setObjectName("actionAdd_new_user")
        self.Curent_widget_help_action = QtWidgets.QAction(AdminShowUsersMenu)
        self.Curent_widget_help_action.setEnabled(False)
        self.Curent_widget_help_action.setObjectName("Curent_widget_help_action")
        self.Student_health_records_help_action = QtWidgets.QAction(AdminShowUsersMenu)
        self.Student_health_records_help_action.setEnabled(False)
        self.Student_health_records_help_action.setObjectName("Student_health_records_help_action")
        self.About_Student_health_records_action = QtWidgets.QAction(AdminShowUsersMenu)
        self.About_Student_health_records_action.setObjectName("About_Student_health_records_action")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLog_out)
        self.menuAbout.addAction(self.Curent_widget_help_action)
        self.menuAbout.addAction(self.Student_health_records_help_action)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.About_Student_health_records_action)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(AdminShowUsersMenu)
        QtCore.QMetaObject.connectSlotsByName(AdminShowUsersMenu)

    def retranslateUi(self, AdminShowUsersMenu):
        _translate = QtCore.QCoreApplication.translate
        AdminShowUsersMenu.setWindowTitle(_translate("AdminShowUsersMenu", "Students health records User info - Admin"))
        self.add_user_pushButton.setText(_translate("AdminShowUsersMenu", "Add new user"))
        self.delete_selected_pushButton.setText(_translate("AdminShowUsersMenu", "Delete selected user"))
        self.menuFile.setTitle(_translate("AdminShowUsersMenu", "File"))
        self.menuAbout.setTitle(_translate("AdminShowUsersMenu", "Help"))
        self.actionOpen.setText(_translate("AdminShowUsersMenu", "Open"))
        self.actionSave.setText(_translate("AdminShowUsersMenu", "Save"))
        self.actionSave_as.setText(_translate("AdminShowUsersMenu", "Save as..."))
        self.actionLog_out.setText(_translate("AdminShowUsersMenu", "Log out"))
        self.actionAdd_new_user.setText(_translate("AdminShowUsersMenu", "Add new user"))
        self.Curent_widget_help_action.setText(_translate("AdminShowUsersMenu", "Current widget help"))
        self.Student_health_records_help_action.setText(_translate("AdminShowUsersMenu", "Student health records help"))
        self.About_Student_health_records_action.setText(_translate("AdminShowUsersMenu", "About Student health records"))

