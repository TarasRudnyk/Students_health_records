import sys
import re
from PyQt5 import QtWidgets
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


class User(QtWidgets.QMainWindow, user_ui.Ui_Student_health_records):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLog_out.triggered.connect(self.show1)


    def show1(self):
        show_auth()

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
        show_user()
        """
        if login == "admin" and password == "admin":
            show_admin()
        elif login == "user1" and password == "login1":
            show_user()
        else:
            QMessageBox.information(form, 'Failed', "Incorrect login or password!")
            form.show()
        """





def check_for_characters(label):
    if re.match("^[A-Za-z0-9@_-]*$", label):
        return True
    return False


def check_email(email):
    if re.match("^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$", email):
        return True
    return False


show_auth()

sys.exit(app.exec())

"""



        self.log_in_button.clicked.connect(self.sign_in_button_clicked)
        self.show_pass.clicked.connect(self.show_hide_password)

        self.user_form()

    def show_add_dialog(self):
        self.setupUi(admin_edit_users)

        u = authorization_ui.Ui_Students_health_records_authorization()
        dialog = QtWidgets.QDialog()
        u.setupUi(dialog)


        #dialog.setFixedSize(dialog.size())
        #dialog.show()
        result = dialog.exec()
        if result == 1:
            username = dialog.username
            password = dialog.password
            if username == 'admin':
                admin_window = admin_show_users.Ui_Student_health_records()
                admin_dialog = QtWidgets.QMainWindow()
                admin_window.setupUi(admin_dialog)
                admin_dialog.show()
                admin_window.show()

                # print(dir(admin_window))
            elif username == 'user':
                self.show()


    def windows(self):
        self.u = admin_show_users.Ui_Student_health_records()
        self.window = QtWidgets.QMainWindow()
        self.u.setupUi(self.window)
        self.window.show()



#*********************************************** Forms functions ******************************************************#
    def user_form(self):
        self.u = user_ui.Ui_Student_health_records()
        self.window = QtWidgets.QMainWindow()
        self.u.setupUi(self.window)
        self.u.button = QtWidgets.QPushButton(self)
        self.u.button.clicked.connect(self.admin_form)

    def add_user_form(self):
        self.u = add_user_ui.Ui_Student_health_records()
        self.window = QtWidgets.QMainWindow()
        self.u.setupUi(self.window)
        self.u.lineEdit_phone_number.setInputMask("+38000-000-00-00")
        self.u.buttonBox.clicked.connect(self.ok_button_clicked)
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

    def admin_form(self):
        self.u = admin_show_users.Ui_Student_health_records()
        self.window = QtWidgets.QMainWindow()
        self.u.setupUi(self.window)
        self.window.show()

    def edit_user_form(self):
        self.u = admin_edit_users.Ui_Student_health_records()
        self.window = QtWidgets.QMainWindow()
        self.u.setupUi(self.window)
        self.u.lineEdit_name.setPlaceholderText("Full name")
        self.u.lineEdit_card_number.setPlaceholderText("Card number")
        self.u.lineEdit_group.setPlaceholderText("Group")
        self.u.lineEdit_email.setPlaceholderText("Email")
        self.u.lineEdit_phone_number.setPlaceholderText("Phone number")
        self.u.textEdit.setPlaceholderText("Please, input diagnose")
        self.u.lineEdit_phone_number.setInputMask("+38000-000-00-00")
        self.u.pushButton.clicked.connect(self.save_user_info_button_clicked)
        self.window.show()

#****************************************** Button-clicked functions **************************************************#

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
        self.dialog.close()
        self.show()

    def save_user_info_button_clicked(self):
        self.u.name_error.setText("")
        self.u.card_number_error.setText("")
        self.u.group_error.setText("")
        self.u.email_error.setText("")
        self.u.phone_number_error.setText("")
        name = self.u.lineEdit_name.text()
        card_number = self.u.lineEdit_card_number.text()
        group = self.u.lineEdit_group.text()
        email = self.u.lineEdit_email.text()
        if self.verification_editing_user(name, card_number, group, email):
            self.add_user()

    def ok_button_clicked(self):
        self.u.medical_card_error.setText("")
        self.u.fist_name_error.setText("")
        self.u.last_name_error_2.setText("")
        self.u.phone_number_error.setText("")
        self.u.user_name_error.setText("")
        self.u.password_error.setText("")
        self.u.email_error.setText("")

#******************************************** Verification functions **************************************************@

    def verification_editing_user(self, name, card_number, group, email):
        success = True

        if not self.check_for_characters(name):
            self.u.name_error.setText("You may use only symbols or numbers!")
            success = False
        if self.is_set_label(name):
            self.u.name_error.setText("This field cannot be empty!")
            success = False

        if not self.check_for_characters(card_number):
            self.u.card_number_error.setText("You may use only symbols or numbers!")
            success = False
        if self.is_set_label(card_number):
            self.u.card_number_error.setText("This field cannot be empty!")
            success = False

        if not self.check_for_characters(group):
            self.u.group_error.setText("You may use only symbols or numbers!")
            success = False
        if self.is_set_label(group):
            self.u.group_error.setText("This field cannot be empty!")
            success = False

        if not self.check_email(email):
            self.u.email_error.setText("Check your email!")
            success = False
        if self.is_set_label(email):
            self.u.email_error.setText("This field cannot be empty!")
            success = False

        return success



    def verification_adding_user(self, card_number, first_name, last_name, phone, group, email):
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

    def add_user(self):
        QMessageBox.information(self, 'Success', "You have registered successfully")
        self.show()

        """
