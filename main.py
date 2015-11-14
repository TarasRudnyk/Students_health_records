import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ui import authorization_ui
from ui import registration_ui
from ui import add_user_ui
from ui import admin_ui
from ui import user_ui


class Student_health_records_app(QtWidgets.QMainWindow, authorization_ui.Ui_Students_health_records_authorization):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())


        self.login_error = QtWidgets.QLabel(self)
        self.login_error.move(135, 47)

        self.password_error = QtWidgets.QLabel(self)
        self.password_error.move(135, 90)

        self.sign_up_button.clicked.connect(self.sign_up)
        self.log_in_button.clicked.connect(self.log_in)


    def sign_up(self):
        self.u = registration_ui.Ui_Students_health_records_registration_ui()
        dialog = QtWidgets.QDialog()
        self.u.setupUi(dialog)
        dialog.show()
        dialog.exec()


    def log_in(self):

        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.login_error.setText(self.is_set_label(login))
        self.login_error.adjustSize()

        self.password_error.setText(self.is_set_label(password))
        self.password_error.adjustSize()



    def user(self):
        self.u = user_ui.Ui_Student_health_records()
        dialog = QtWidgets.QDialog()
        self.u.setupUi(dialog)
        dialog.show()
        dialog.exec()

    def admin(self):
        self.u = admin_ui.Ui_Student_health_records()
        dialog = QtWidgets.QDialog()
        self.u.setupUi(dialog)
        dialog.show()
        dialog.exec()

    def add_user(self):
        self.u = add_user_ui.Ui_Form()
        dialog = QtWidgets.QDialog()
        self.u.setupUi(dialog)
        dialog.show()
        dialog.exec()

    def verification_sign_in(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(login, password)

    def verification_sign_up(self):
        pass

    def is_set_label(self, label):
        if len(label) == 0:
            return "This label cannot be empty!"
        return " "
