import sys

from PyQt5 import QtWidgets

from ui import authorization_ui
from ui import registration_ui
from ui import add_user_ui
from ui import admin_ui
from ui import user_ui


class Student_health_records_app(QtWidgets.QMainWindow, authorization_ui.Ui_Students_health_records_authorization):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


        #self.setFixedSize(self.width(), self.height())

        self.sign_up_button.clicked.connect(self.sign_up)

        self.log_in_button.clicked.connect(self.user)


    def sign_up(self):
        self.u = registration_ui.Ui_Students_health_records_registration_ui()
        dialog = QtWidgets.QDialog()
        self.u.setupUi(dialog)
        dialog.show()
        dialog.exec()
        # registration_ui.Ui_Students_health_records_registration_ui.sign_in_button.connect()

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
        pass

    def verification_sign_up(self):
        pass


