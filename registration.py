import sys

from ui import registration_ui

from PyQt5.QtWidgets import QApplication, QWidget

def show_window():
    app = QApplication(sys.argv)
    registration_window =QWidget()
    ui = registration_ui.Ui_Students_health_records_registration_ui()
    ui.setupUi(registration_window)
    #QObject.connect(ui.btnQuit, QtCore.SIGNAL("clicked"),
    #                       QtGui.qApp.quit)

    registration_window.show()
    sys.exit(app.exec_())
