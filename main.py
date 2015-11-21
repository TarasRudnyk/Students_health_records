import sys
import re
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

from views import authorization_ui
from views import add_user_ui
from views import admin_edit_user_info
from views import admin_show_user_info
from views import user_ui


class Authorization(QtWidgets.QMainWindow, authorization_ui.Ui_AuthorizationWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_pass_button.clicked.connect(self.show_hide_password)

    def show_hide_password(self):
        if self.password_lineEdit.echoMode() == 0:
            self.password_lineEdit.setEchoMode(2)
        else:
            self.password_lineEdit.setEchoMode(0)


class Admin(QtWidgets.QMainWindow, admin_show_user_info.Ui_AdminShowUsersMenu):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLog_out.triggered.connect(log_out)
        self.add_user_pushButton.clicked.connect(self.adding_user)
        self.About_Student_health_records_action.triggered.connect(about_information)
        self.user_info_tableWidget.cellPressed.connect(self.editing_user)

    def editing_user(self):
        self.edit_user = admin_edit_user_info.Ui_Student_health_records()
        self.dialog = QtWidgets.QDialog()
        self.edit_user.setupUi(self.dialog)
        #self.edit_user.ok_cancel_buttonBox.accepted.connect(self.add_user_data_verification)
        #self.edit_user.ok_cancel_buttonBox.rejected.connect(self.close_widget)
        self.close()
        self.dialog.show()
        self.dialog.exec()
        self.show()

    def adding_user(self):
        self.add_user = add_user_ui.Ui_addUserWindow()
        self.dialog = QtWidgets.QDialog()
        self.add_user.setupUi(self.dialog)
        self.add_user.ok_cancel_buttonBox.accepted.connect(self.add_user_data_verification)
        self.add_user.ok_cancel_buttonBox.rejected.connect(self.close_widget)
        self.close()
        self.dialog.show()
        self.dialog.exec()
        self.show()

    def close_widget(self):
        self.dialog.destroy()
        self.show()

    def add_user_data_verification(self):
        success = True
        card_number = self.add_user.card_number_lineEdit.text()
        first_name = self.add_user.first_name_lineEdit.text()
        last_name = self.add_user.last_name_lineEdit.text()
        phone_number = self.add_user.phone_number_lineEdit.text()
        user_name = self.add_user.username_lineEdit.text()
        password = self.add_user.password_lineEdit.text()
        email = self.add_user.email_lineEdit.text()

        self.add_user.card_number_error.setText("")
        self.add_user.first_name_error.setText("")
        self.add_user.last_name_error.setText("")
        self.add_user.phone_number_error.setText("")
        self.add_user.username_error.setText("")
        self.add_user.password_error.setText("")
        self.add_user.email_error.setText("")

        if len(card_number) < 8:
            self.add_user.card_number_error.setText("Card number must have 8 symbols!")
            success = False

        if not check_for_characters(first_name):
            self.add_user.first_name_error.setText("You entered incorrect symbol(s)!")
            success = False
        if len(first_name) < 2:
            self.add_user.first_name_error.setText("Please enter more than 1 symbol!")
            success = False
        if len(first_name) == 0:
            self.add_user.first_name_error.setText("This field cannot be empty!")
            success = False

        if not check_for_characters(last_name):
            self.add_user.last_name_error.setText("You entered incorrect symbol(s)!")
            success = False
        if len(last_name) < 2:
            self.add_user.last_name_error.setText("Please enter more than 1 symbol!")
            success = False
        if len(last_name) == 0:
            self.add_user.last_name_error.setText("This field cannot be empty!")
            success = False

        if not check_for_characters(user_name):
            self.add_user.username_error.setText("You entered incorrect symbol(s)!")
            success = False
        if len(user_name) < 5:
            self.add_user.username_error.setText("Please enter more than 4 symbols!")
            success = False
        if len(user_name) == 0:
            self.add_user.username_error.setText("This field cannot be empty!")
            success = False

        if len(password) < 8:
            self.add_user.password_error.setText("Please enter more than 7 symbols!")
            success = False
        if len(password) == 0:
            self.add_user.password_error.setText("This field cannot be empty!")
            success = False

        if len(email) > 0 and not check_email(email):
            self.add_user.email_error.setText("Incorrect email address!")
            success = False

        if success:
            QMessageBox.information(self, 'Success', "User has been added!!")
            self.show()


class User(QtWidgets.QMainWindow, user_ui.Ui_Student_health_records):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLog_out.triggered.connect(log_out)
        self.About_Student_health_records_action.triggered.connect(about_information)

app = QtWidgets.QApplication(sys.argv)
form = Authorization()


def show_auth():
    global form
    form.close()
    form = Authorization()
    form.log_in_button.clicked.connect(auth_data_verification)
    form.show()


def show_admin():
    global form
    form.close()
    form = Admin()
    form.show()


def show_user():
    global form
    form.close()
    form = User()
    form.show()


def auth_data_verification():
    global form
    success = True

    login = form.username_lineEdit.text()
    password = form.password_lineEdit.text()

    form.username_error_label.setText("")
    form.password_error_label.setText("")

    if len(login) == 0:
        form.username_error_label.setText("This field cannot be empty!")
        success = False

    if len(password) == 0:
        form.password_error_label.setText("This field cannot be empty!")
        success = False

    if success:
        show_admin()
        """
        if login == "admin" and password == "admin":
            show_admin()
        elif login == "user" and password == "user":
            show_user()
        else:
            QMessageBox.information(form, 'Failed', "Incorrect login or password!")
            form.show()
        """


def log_out():
    show_auth()


def check_for_characters(label):
    if re.match("^[A-Za-z0-9@_-]*$", label):
        return True
    return False


def check_email(email):
    if re.match("^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$", email):
        return True
    return False


def about_information():
    global form
    QMessageBox.information(form, 'Student health records', "There will be information about program")
    form.show()


show_auth()
sys.exit(app.exec())
