import sys
import re
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

        self.sign_up_button.clicked.connect(self.sign_up_form)
        self.log_in_button.clicked.connect(self.sign_in_button_clicked)
        self.show_pass.clicked.connect(self.show_hide_password)

#*********************************************** Forms functions ******************************************************#
    def user_form(self):
        self.u = user_ui.Ui_Student_health_records()
        self.window = QtWidgets.QMainWindow()
        self.u.setupUi(self.window)
        self.window.show()


    def sign_up_form(self):
        self.u = registration_ui.Ui_Students_health_records_registration_ui()
        self.dialog = QtWidgets.QDialog()
        self.u.setupUi(self.dialog)
        self.u.sign_up_button.clicked.connect(self.confirm_button_clicked)
        self.u.sign_in_button.clicked.connect(self.back_button_clicked)
        self.close()
        self.dialog.show()
        self.dialog.exec()
        self.show()

    def admin(self):
        self.admin = admin_ui.Ui_Student_health_records()
        dialog = QtWidgets.QDialog()
        self.admin.setupUi(dialog)
        dialog.show()
        dialog.exec()

    def add_user(self):
        self.new_user = add_user_ui.Ui_Form()
        dialog = QtWidgets.QDialog()
        self.new_user.setupUi(dialog)
        dialog.show()
        dialog.exec()

#****************************************** Button-clicked functions **************************************************#
    def sign_in_button_clicked(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.login_error.setText(" ")
        self.password_error.setText(" ")

        if self.verification_sign_in(login, password):
            self.close()
            self.user_form()
            self.show()

    def confirm_button_clicked(self):
        first_name = self.u.lineEdit_first_name.text()
        last_name = self.u.lineEdit_last_name.text()
        login = self.u.lineEdit_username.text()
        password = self.u.lineEdit_password.text()
        email = self.u.lineEdit_Email.text()

        self.u.First_name_error.setText("")
        self.u.Last_name_error.setText("")
        self.u.User_name_error.setText("")
        self.u.Password_error.setText("")
        self.u.Emai_error.setText("")

        if self.verification_sign_up(first_name, last_name, login, password, email):
            self.register_user()

        def back_button_clicked(self):
            pass

    def back_button_clicked(self):
        pass

#******************************************** Verification functions **************************************************@

    def verification_sign_up(self, first_name, last_name, login, password, email):
        success = True

        if not self.check_for_characters(first_name):
            self.u.First_name_error.setText("You may use only symbols or numbers!")
            success = False
        if self.check_length(first_name) and not self.is_set_label(first_name):
            self.u.First_name_error.setText("Length must be between 5 and 20 symbols")
            success = False

        if not self.check_for_characters(last_name):
            self.u.Last_name_error.setText("You may use only symbols or numbers!")
            success = False
        if self.check_length(last_name) and not self.is_set_label(last_name):
            self.u.Last_name_error.setText("Length must be between 5 and 20 symbols")
            success = False

        if not self.check_for_characters(login):
            self.u.User_name_error.setText("You may use only symbols or numbers!")
            success = False
        if self.check_length(login):
            self.u.User_name_error.setText("Length must be between 5 and 20 symbols")
            success = False
        if self.is_set_label(login):
            self.u.User_name_error.setText("This label cannot be empty!")
            success = False

        if self.check_length(password):
            self.u.Password_error.setText("Length must be between 5 and 20 symbols")
            success = False
        if self.is_set_label(password):
            self.u.Password_error.setText("This label cannot be empty!")
            success = False

        if not self.check_email(email):
            self.u.Emai_error.setText("Check your email!")
            success = False
        if self.is_set_label(email):
            self.u.Emai_error.setText("This label cannot be empty!")
            success = False

        return success

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

#********************************************* Additional functions ***************************************************#
    def check_for_characters(self, label):
        if re.match("^[A-Za-z0-9@_-]*$", label):
            return True
        return False

    def check_email(self, email):
        if re.match("^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$", email):
            return True
        return False

    def is_set_label(self, label):
        if len(label) == 0:
            return True
        return False

    def check_length(self, label):
        if len(label) < 5 or len(label) > 20:
            return True
        return False

    def show_hide_password(self):
        if self.lineEdit_2.echoMode() == 0:
            self.lineEdit_2.setEchoMode(2)
        else:
            self.lineEdit_2.setEchoMode(0)

    def register_user(self):
        QMessageBox.information(self, 'Success', "You have registered successfully")
        self.dialog.close()
        self.show()
