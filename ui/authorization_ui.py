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
        Students_health_records_authorization.resize(382, 161)
        Students_health_records_authorization.setAccessibleName("")
        self.label = QtWidgets.QLabel(Students_health_records_authorization)
        self.label.setGeometry(QtCore.QRect(9, 26, 48, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Students_health_records_authorization)
        self.lineEdit.setGeometry(QtCore.QRect(132, 26, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Students_health_records_authorization)
        self.label_2.setGeometry(QtCore.QRect(9, 69, 46, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Students_health_records_authorization)
        self.lineEdit_2.setGeometry(QtCore.QRect(132, 69, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.log_in_button = QtWidgets.QPushButton(Students_health_records_authorization)
        self.log_in_button.setGeometry(QtCore.QRect(132, 112, 75, 23))
        self.log_in_button.setObjectName("log_in_button")
        self.sign_up_button = QtWidgets.QPushButton(Students_health_records_authorization)
        self.sign_up_button.setGeometry(QtCore.QRect(256, 112, 75, 23))
        self.sign_up_button.setObjectName("sign_up_button")
        self.show_pass = QtWidgets.QToolButton(Students_health_records_authorization)
        self.show_pass.setGeometry(QtCore.QRect(315, 69, 20, 20))
        self.show_pass.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"D:\PyCharm\workspace\DB\Students_health_records\ui\eye.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.show_pass.setIcon(icon)
        self.show_pass.setObjectName("show_pass")

        self.retranslateUi(Students_health_records_authorization)
        QtCore.QMetaObject.connectSlotsByName(Students_health_records_authorization)

    def retranslateUi(self, Students_health_records_authorization):
        _translate = QtCore.QCoreApplication.translate
        Students_health_records_authorization.setWindowTitle(_translate("Students_health_records_authorization", "Students_health_records_authorization"))
        self.label.setText(_translate("Students_health_records_authorization", "Username"))
        self.label_2.setText(_translate("Students_health_records_authorization", "Password"))
        self.log_in_button.setText(_translate("Students_health_records_authorization", "Log in"))
        self.sign_up_button.setText(_translate("Students_health_records_authorization", "Sign up"))

#import eye_qrc
