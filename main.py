import sys
import re
import socket
import json

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox

from views import authorization_ui
from views import add_user_ui
from ui import admin_edit_user_info
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
        self.draw_table()

        """
        combobox = QtWidgets.QComboBox()
        combobox.addItem("1")
        combobox.addItem("2")
        self.user_info_tableWidget.setCellWidget(0, 1, combobox)
        self.user_info_tableWidget.setItem(0, 0, QTableWidgetItem("erugi"))
        """

    def draw_table(self):
        try:
            info = get_all_users_info()
            count = len(info["users_card_numbers"])
        except:
            QMessageBox.information(self, 'Failed', "There is some problem with server.\nPlease try later.")
            count = 0

        self.user_info_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.user_info_tableWidget.setMinimumSize(QtCore.QSize(754, 412))
        self.user_info_tableWidget.setObjectName("user_info_tableWidget")
        self.user_info_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.user_info_tableWidget.setColumnCount(3)
        self.user_info_tableWidget.setRowCount(count)
        self.user_info_tableWidget.setSortingEnabled(True)
        self.user_info_tableWidget.horizontalHeader().setVisible(True)
        self.user_info_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.user_info_tableWidget.horizontalHeader().setDefaultSectionSize(235)
        self.user_info_tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.user_info_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.user_info_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.user_info_tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.user_info_tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.user_info_tableWidget.verticalHeader().setStretchLastSection(False)
        self.user_info_tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Card number"))
        self.user_info_tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Full name"))
        self.user_info_tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Group"))

        for i in range(count):
            self.user_info_tableWidget.setItem(i, 0, QTableWidgetItem(str(info["users_card_numbers"][i])))
            self.user_info_tableWidget.setItem(i, 1, QTableWidgetItem(str(info["users_full_names"][i])))
            self.user_info_tableWidget.setItem(i, 2, QTableWidgetItem(str(info["users_groups"][i])))

        self.user_info_tableWidget.cellDoubleClicked.connect(self.show_user_info)
        self.delete_selected_pushButton.clicked.connect(self.delete_user)
        self.gridLayout_3.addWidget(self.user_info_tableWidget, 2, 0, 1, 3)

    def update_table(self):
        try:
            info = get_all_users_info()
            count = len(info["users_card_numbers"])
        except:
            QMessageBox.information(self, 'Failed', "There is some problem with server.\nPlease try later.")
            count = 0
        self.user_info_tableWidget.setColumnCount(3)
        self.user_info_tableWidget.setRowCount(count)
        for i in range(count):
            self.user_info_tableWidget.setItem(i, 0, QTableWidgetItem(str(info["users_card_numbers"][i])))
            self.user_info_tableWidget.setItem(i, 1, QTableWidgetItem(str(info["users_full_names"][i])))
            self.user_info_tableWidget.setItem(i, 2, QTableWidgetItem(str(info["users_groups"][i])))

    def show_user_info(self):
        row = self.user_info_tableWidget.currentItem().row()
        card_number = self.user_info_tableWidget.item(row, 0).text()
        self.editing_user(card_number)

    def delete_user(self):
        global user_login
        set_row = True
        try:
            row = self.user_info_tableWidget.selectedItems()[0].row()
        except:
            QMessageBox.information(self, 'Failed', "Please select any user!")
            set_row = False

        if set_row:
            user_name = self.user_info_tableWidget.item(row, 1).text()
            reply = QMessageBox.question(self, 'Message',
                                         "Are you sure to delete user {0}?".format(user_name),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                user_card_number = self.user_info_tableWidget.item(row, 0).text()
                if delete_user(user_login, user_card_number)["success"]:
                    self.user_info_tableWidget.removeRow(row)
            else:
                QMessageBox.information(self, 'Canceled', "Deleting canceled!")

    def editing_user(self, user_card_number):
        try:
            info = get_all_user_info(user_card_number)
        except:
            QMessageBox.information(self, 'Failed', "There is some problem with server.\nPlease try later.")
            info = {'success': True,
                    'user_full_name': '',
                    'user_group': '',
                    'user_email': '',
                    'user_phone_number': ''}
        self.put_user_info(user_card_number, info)



    def put_user_info(self, user_card_number, info):
        self.edit_user = admin_edit_user_info.Ui_Student_health_records()
        self.dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.edit_user.setupUi(self.dialog)
        self.edit_user.card_number_lineEdit.setEnabled(False)
        self.edit_user.card_number_lineEdit.setText(user_card_number)
        self.edit_user.full_name_lineEdit.setText(info["user_full_name"])
        self.edit_user.group_lineEdit.setText(info["user_group"])
        self.edit_user.email_lineEdit.setText(info["user_email"])
        self.edit_user.phone_number_lineEdit.setText(str(info["user_phone_number"]))
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

        full_name = full_name[0] + " " + full_name[1]
        if success:
            try:
                result = update_user_info(card_number, full_name, group, phone_number, email)

                QMessageBox.information(self, 'Success', "User information has been updated!")
            except:
                pass

    def add_user_data_verification(self):
        global user_login
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
            try:
                adding = add_new_user(card_number, full_name, group, phone_number, user_name, password, email,
                                      user_login)
                success = adding["success"]
                if not success:
                    QMessageBox.information(self, 'Failed', "There is some problem.\nPlease check your data")
            except:
                QMessageBox.information(self, 'Failed', "There is some problem with server.\nPlease try later.")
                success = False
        if success:
            QMessageBox.information(self, 'Success', "User has been added!")
            self.user_info_tableWidget.clear()
            self.update_table()
            self.dialog.close()


class User(QtWidgets.QMainWindow, user_ui.Ui_Student_health_records):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionLog_out.triggered.connect(log_out)
        self.About_Student_health_records_action.triggered.connect(about_information)
        self.draw_table()

    def draw_table(self):
        global user_login
        try:
            diagnoses = get_user_diagnoses(user_login)
            count = len(diagnoses["diagnose_name"])
        except:
            QMessageBox.information(self, 'Failed', "There is some problem with server.\nPlease try later.")
            count = 0

        self.user_info_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.user_info_tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_info_tableWidget.sizePolicy().hasHeightForWidth())
        self.user_info_tableWidget.setSizePolicy(sizePolicy)
        self.user_info_tableWidget.setMinimumSize(QtCore.QSize(686, 578))
        self.user_info_tableWidget.setMouseTracking(False)
        self.user_info_tableWidget.setAcceptDrops(False)
        self.user_info_tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user_info_tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_info_tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.user_info_tableWidget.setLineWidth(1)
        self.user_info_tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.user_info_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.user_info_tableWidget.setAutoScroll(False)
        self.user_info_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.user_info_tableWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.user_info_tableWidget.setShowGrid(True)
        self.user_info_tableWidget.setCornerButtonEnabled(True)
        self.user_info_tableWidget.setRowCount(count)
        self.user_info_tableWidget.setColumnCount(3)
        self.user_info_tableWidget.setObjectName("user_info_tableWidget")
        self.user_info_tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Date"))
        self.user_info_tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Doctor"))
        self.user_info_tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Diagnose"))
        for i in range(count):
            self.user_info_tableWidget.setItem(i, 0, QTableWidgetItem(diagnoses["diagnose_date"][i]))
            self.user_info_tableWidget.setItem(i, 1, QTableWidgetItem(diagnoses["diagnose_doctor"][i]))
            self.user_info_tableWidget.setItem(i, 2, QTableWidgetItem(diagnoses["diagnose_name"][i]))

        self.user_info_tableWidget.setSortingEnabled(True)

        self.user_info_tableWidget.horizontalHeader().setVisible(True)
        self.user_info_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.user_info_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.user_info_tableWidget.horizontalHeader().setHighlightSections(True)
        self.user_info_tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.user_info_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.user_info_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.user_info_tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.user_info_tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.user_info_tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.user_info_tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.user_info_tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.user_info_tableWidget, 0, 0, 1, 1)

app = QtWidgets.QApplication(sys.argv)
form = Authorization()
user_login = ""


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
        try:
            check = check_login_and_password(login, password)
            if not check["success"]:
                QMessageBox.information(form, 'Failed', "Incorrect login or password!")
                success = False
        except Exception:
            QMessageBox.information(form, 'Failed', "There is some problem with server.\nPlease try later.")
            success = False

    if success:
        global user_login
        user_login = login

        if check["role"] == "admin":
            show_admin()
        else:
            show_user()


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


def get_user_diagnoses(login):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "get_my_diagnoses"
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(10000)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


def get_all_users_info():
    global user_login
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": user_login,
                 "action": "get_all_users"
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(10000)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


def add_new_user(card_number, full_name, group, phone_number, username, password, email, login):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "add_new_user",
                 "user_data": {
                     "user_card_number": card_number,
                     "user_full_name": full_name,
                     "user_group": group,
                     "user_phone_number": phone_number,
                     "username": username,
                     "password": password,
                     "user_email": email,
                     "user_role": "user"
                 }
                 }
    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(1024)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


def delete_user(login, card_number):
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": login,
                 "action": "delete_user",
                 "user_card_number": card_number
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(10000)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


def get_all_user_info(card_number):
    global user_login
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {"auth": False,
                 "login": user_login,
                 "action": "get_all_user_info",
                 "user_card_number": card_number
                 }

    sock.sendall(json.dumps(send_data).encode('utf-8'))

    data = sock.recv(10000)
    sock.close()

    data = json.loads(data.decode('utf-8'))
    return data


def update_user_info(card_number, full_name, group, phone_number, email):
    global user_login
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))

    send_data = {
        "auth": False,
        "login": user_login,
        "action": "update_user_info",
        "user_data": {
             "user_card_number": card_number,
             "user_full_name": full_name,
             "user_group": group,
             "user_phone_number": phone_number,
             "user_email": email
        }
    }

    sock.sendall(json.dumps(send_data).encode('utf-8'))
    data = sock.recv(10000)
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
