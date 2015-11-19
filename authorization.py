import sys

from PyQt5 import QtWidgets

from ui import authorization_ui


class Student_health_records_app(QtWidgets.QMainWindow, authorization_ui.Ui_Students_health_records_authorization):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setFixedSize(self.width(), self.height())
        #self.conf = self.read_app_config()

'''
def show_window():
    app = QApplication(sys.argv)
    authorization_window =QWidget()
    ui = authorization_ui.Ui_Students_health_records_authorization()
    ui.setupUi(authorization_window)
    ui.sign_up_button.clicked.connect(sign_up_form)
    authorization_window.show()
    sys.exit(app.exec_())


def sign_up_form():
    #registration.show_window()
    print("test")
'''