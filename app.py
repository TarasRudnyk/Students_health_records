import sys

from PyQt5 import QtWidgets

# import authorization

import main

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = main.Student_health_records_app()
    #form.show()
    sys.exit(app.exec())
