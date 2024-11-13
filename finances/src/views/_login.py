from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QMainWindow

from ..UI.generated.ui_Login import Ui_Login
from .._consts import style_global, parserStyle

style = parserStyle(style_global + """

QPushButton { %(button)s }

QPushButton::hover { %(button-hover)s }

#Login {
    background-color: %(fill-background)s;
}

""")

class LoginView(QObject):
    @property
    def widget(self) -> QWidget:
        return self.__wid
        
    def __init__(self, window:QMainWindow) -> None:
        super().__init__()
        self.__window = window
    
    def setup(self):
        self.__ui = Ui_Login()
        self.__wid = QWidget(self.__window)
        
        self.__ui.setupUi(self.__wid)
        self.__wid.setStyleSheet(style)
        self.__window.setCentralWidget(self.__wid)