from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from UI.ui_Login import Ui_Login
from UI.ui_CreateAccount import Ui_CreateAccount

from config import *

style = parserStyle(style_global + """

QPushButton { %(button)s }

QPushButton::hover { %(button-hover)s }

#Login {
    background-color: %(fill-background)s;
}

""")

def setupCreate(window:QMainWindow):
    wid = QWidget(window)
    ui = Ui_CreateAccount()
    ui.setupUi(wid)
    window.setCentralWidget(wid)

    wid.setStyleSheet(style)
    ui.btnAcessar.clicked.connect(lambda: setupLogin(window))


def setupLogin(window:QMainWindow):
    wid = QWidget(window)
    ui = Ui_Login()
    ui.setupUi(wid)
    window.setCentralWidget(wid)

    wid.setStyleSheet(style)
    ui.btnCriar.clicked.connect(lambda: setupCreate(window))

if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    window.setFont(font)

    # configurando components
    window.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    setupLogin(window)

    window.show()
    app.exec()
