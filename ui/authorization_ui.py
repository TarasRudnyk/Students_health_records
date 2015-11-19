# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorization.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!
import functools
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Students_health_records_authorization(QtWidgets.QDialog):
    def setupUi(self, Students_health_records_authorization):
        Students_health_records_authorization.setObjectName("Students_health_records_authorization")
        Students_health_records_authorization.resize(382, 161)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Students_health_records/ui/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Students_health_records_authorization.setWindowIcon(icon)
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
        self.log_in_button.setGeometry(QtCore.QRect(132, 112, 201, 23))
        self.log_in_button.setObjectName("log_in_button")
        self.show_pass = QtWidgets.QToolButton(Students_health_records_authorization)
        self.show_pass.setGeometry(QtCore.QRect(315, 69, 20, 20))
        self.show_pass.setText("")
        self.login_error = QtWidgets.QLabel()
        self.login_error.move(135, 47)

        self.password_error = QtWidgets.QLabel()
        self.password_error.move(135, 90)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_pass.setIcon(icon1)
        self.show_pass.setObjectName("show_pass")
        dialog_object = Students_health_records_authorization
        accept = functools.partial(self.sign_in_button_clicked, dialog_object)
        self.log_in_button.clicked.connect(accept)

        #self.log_in_button.clicked.connect(self.accepted)
        self.retranslateUi(Students_health_records_authorization)
        QtCore.QMetaObject.connectSlotsByName(Students_health_records_authorization)

    def retranslateUi(self, Students_health_records_authorization):
        _translate = QtCore.QCoreApplication.translate
        Students_health_records_authorization.setWindowTitle(_translate("Students_health_records_authorization", "Students_health_records_authorization"))
        self.label.setText(_translate("Students_health_records_authorization", "Username"))
        self.label_2.setText(_translate("Students_health_records_authorization", "Password"))
        self.log_in_button.setText(_translate("Students_health_records_authorization", "Log in"))

    def verification_sign_in(self, login, password):
        success = True

        if self.is_set_label(login):
            self.login_error.setText("This label cannot be empty!")
            success = False

        if self.is_set_label(password):
            self.password_error.setText("This label cannot be empty!")
            success = False

        self.login_error.adjustSize()
        self.password_error.adjustSize()

        return success

    def sign_in_button_clicked(self, dialog_object):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.login_error.setText(" ")
        self.password_error.setText(" ")

        if self.verification_sign_in(login, password):
            print('Passed')
            dialog_object.username = 'admin'
            dialog_object.password = 'password'
            #print(dir(self))
            dialog_object.accept()
            """
            self.hide()
            self.add_user_form()
            self.admin_form()
            self.show()
            """
        else:
            print('Error')

    def is_set_label(self, label):
        if len(label) == 0:
            return True
        return False
