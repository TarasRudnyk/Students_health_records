import sys
import re
import socket
import json

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
        self.username_lineEdit.returnPressed.connect(self.log_in_button.click)
        self.password_lineEdit.returnPressed.connect(self.log_in_button.click)



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
        self.user_info_tableWidget.cellDoubleClicked.connect(self.editing_user)

    def editing_user(self):
        self.edit_user = admin_edit_user_info.Ui_Student_health_records()
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.edit_user.setupUi(self.dialog)
        self.edit_user.confirm_pushButton.clicked.connect(self.edit_user_data_verification)
        self.edit_user.back_to_info_view_pushButton.clicked.connect(self.close_widget)
        self.edit_user.card_number_lineEdit.returnPressed.connect(self.edit_user.confirm_pushButton.click)
        self.edit_user.full_name_lineEdit.returnPressed.connect(self.edit_user.confirm_pushButton.click)
        self.edit_user.group_lineEdit.returnPressed.connect(self.edit_user.confirm_pushButton.click)
        self.edit_user.email_lineEdit.returnPressed.connect(self.edit_user.confirm_pushButton.click)
        self.edit_user.phone_number_lineEdit.returnPressed.connect(self.edit_user.confirm_pushButton.click)
        self.close()
        self.dialog.show()
        self.dialog.exec()
        self.show()

    def adding_user(self):
        self.add_user = add_user_ui.Ui_addUserWindow()
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
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

    def edit_user_data_verification(self):
        success = True
        full_name = self.edit_user.full_name_lineEdit.text().split(" ")
        try:
            full_name[1]
        except Exception:
            full_name.append("")
        card_number = self.edit_user.card_number_lineEdit.text()
        group = self.edit_user.group_lineEdit.text()
        email = self.edit_user.email_lineEdit.text()
        phone_number = self.edit_user.phone_number_lineEdit.text()

        self.edit_user.name_error.setText("")
        self.edit_user.card_number_error.setText("")
        self.edit_user.group_error.setText("")
        self.edit_user.email_error.setText("")
        self.edit_user.phone_number_error.setText("")

        try:
            if not full_name[0].isalpha() or not full_name[1].isalpha():
                self.edit_user.name_error.setText("Please enter only alphabetic symbols!")
                success = False
        except:
            pass
        if len(full_name[0]) + len(full_name[1]) < 4:
            self.edit_user.name_error.setText("Please enter 5 or more symbols!")
            success = False
        if len(full_name[1]) == 0:
            self.edit_user.name_error.setText("Please enter first and last name!")
            success = False
        if len(full_name[0]) == 0:
            self.edit_user.name_error.setText("This field cannot be empty!")
            success = False

        if not card_number.isdigit():
            self.edit_user.card_number_error.setText("Please enter only digits!")
            success = False
        if len(card_number) < 8:
            self.edit_user.card_number_error.setText("Card number must have 8 digits!")
            success = False

        if not re.match("^[a-zA-Z]{2}[0-9]{2}", group):
            self.edit_user.group_error.setText("Incorrect group name!")
            success = False
        if len(group) == 0:
            self.edit_user.group_error.setText("This field cannot be empty!")
            success = False

        if len(email) > 0 and not check_email(email):
            self.edit_user.email_error.setText("Incorrect email address!")
            success = False

        if success:
            QMessageBox.information(self, 'Success', "User information has been updated!")

    def add_user_data_verification(self):
        success = True
        card_number = self.add_user.card_number_lineEdit.text()
        full_name = self.add_user.full_name_lineEdit.text().split(" ")
        try:
            full_name[1]
        except Exception:
            full_name.append("")
        group = self.add_user.group_lineEdit.text()
        phone_number = self.add_user.phone_number_lineEdit.text()
        user_name = self.add_user.username_lineEdit.text()
        password = self.add_user.password_lineEdit.text()
        email = self.add_user.email_lineEdit.text()

        self.add_user.card_number_error.setText("")
        self.add_user.full_name_error.setText("")
        self.add_user.group_error.setText("")
        self.add_user.phone_number_error.setText("")
        self.add_user.username_error.setText("")
        self.add_user.password_error.setText("")
        self.add_user.email_error.setText("")

        if not card_number.isdigit():
            self.add_user.card_number_error.setText("Please enter only digits!")
            success = False
        if len(card_number) < 8:
            self.add_user.card_number_error.setText("Card number must have 8 digits!")
            success = False

        if not full_name[0].isalpha() or not full_name[1].isalpha():
            self.add_user.full_name_error.setText("Please enter only alphabetic symbols!")
            success = False
        if len(full_name[0]) + len(full_name[1]) < 4:
            self.add_user.full_name_error.setText("Please enter 5 or more symbols!")
            success = False
        if len(full_name[1]) == 0:
            self.add_user.full_name_error.setText("Please enter first and last name!")
            success = False
        if len(full_name[0]) == 0:
            self.add_user.full_name_error.setText("This field cannot be empty!")
            success = False

        if not re.match("^[a-zA-Z]{2}[0-9]{2}", group):
            self.add_user.group_error.setText("Incorrect group name!")
            success = False
        if len(group) == 0:
            self.add_user.group_error.setText("This field cannot be empty!")
            success = False

        if not check_for_characters(user_name):
            self.add_user.username_error.setText("You entered incorrect symbol(s)!")
            success = False
        if len(user_name) < 5:
            self.add_user.username_error.setText("Please enter 5 or more symbols!")
            success = False
        if len(user_name) == 0:
            self.add_user.username_error.setText("This field cannot be empty!")
            success = False

        if len(password) < 8:
            self.add_user.password_error.setText("Please enter 8 or more symbols!")
            success = False
        if len(password) == 0:
            self.add_user.password_error.setText("This field cannot be empty!")
            success = False

        if len(email) > 0 and not check_email(email):
            self.add_user.email_error.setText("Incorrect email address!")
            success = False

        if success:
            QMessageBox.information(self, 'Success', "User has been added!")
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

    check = check_login_and_password(login, password)
    if not check["success"]:
        QMessageBox.information(form, 'Failed', "Incorrect login or password!")
        success = False

    if success:
        if login == "admin" and password == "admin":
            show_admin()
        elif login == "limar" and password == "limar":
            show_user()
        else:
            #QMessageBox.information(form, 'Failed', "Incorrect login or password!")
            form.show()


def check_login_and_password(login, password):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": True,
                 "login": login,
                 "password": password,
                 "action": "authorization"
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


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
    QMessageBox.information(form, 'Student health records', "Version 1.0\n"
                                                            "Student health records is a "
                                                            "program which manage user health.\n"
                                                            "Copyright \u00A9 2015 Rudnyk Taras")
    form.show()


show_auth()
sys.exit(app.exec())
