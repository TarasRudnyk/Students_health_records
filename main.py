import sys

from PyQt5 import QtWidgets

from ui import authorization_ui
from ui import registration_ui


class Student_health_records_app(QtWidgets.QMainWindow, authorization_ui.Ui_Students_health_records_authorization):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setFixedSize(self.width(), self.height())

        self.sign_up_button.clicked.connect(self.go_to_sign_up)

        # self.log_in_button.clicked.connect()


    def go_to_sign_up(self):
        self.u = registration_ui.Ui_Students_health_records_registration_ui()
        dialog = QtWidgets.QDialog()
        self.u.setupUi(dialog)
        dialog.show()
        dialog.exec()


