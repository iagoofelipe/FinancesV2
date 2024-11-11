from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from UI.ui_Login import Ui_Login
from UI.ui_CreateAccount import Ui_CreateAccount

from config import *

def setupUi(ui, window):
    wid = QWidget(window)
    ui.setupUi(wid)
    window.setCentralWidget(wid)

    # configurando style
    wid.setStyleSheet(style_widget)

if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    wid = QWidget()
    ui_login = Ui_Login()
    ui_CreateAccount = Ui_CreateAccount()

    # configurando components
    ui_login.setupUi(wid)
    window.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setCentralWidget(wid)

    # confingurando slots
    ui_login.btnCriar.clicked.connect(lambda: setupUi(ui_CreateAccount, window))

    # configurando style
    wid.setStyleSheet(style_widget)

    window.show()
    app.exec()
