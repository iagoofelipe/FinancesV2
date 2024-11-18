from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMainWindow, QWidget

from ..UI.generated.ui_Login import Ui_Login
from ..UI.style import style_global, parserStyle
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

style = parserStyle(style_global + """

QPushButton { %(button)s }

QPushButton::hover { %(button-hover)s }

""")


class ViewLogin(QObject):
    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__()
        self.__win = window
        self.__events = events
        self.__model = model
        
    def setup(self):
        self.__ui = Ui_Login()
        self.__wid = QWidget(self.__win)

        self.__ui.setupUi(self.__wid)
        self.__win.setCentralWidget(self.__wid)
        self.__wid.setStyleSheet(style)

        # signals && slots
        self.__ui.btnAcessar.clicked.connect(self.on_btnAcessar_clicked)

    def on_btnAcessar_clicked(self):
        username = self.__ui.lineUsuario.text()
        password = self.__ui.lineSenha.text()

        if not username or not password:
            # TODO: solicitar preenchimento de todos os campos
            return
        
        self.__events.loginRequired.emit({'username': username, 'password': password})