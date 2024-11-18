from PySide6.QtWidgets import QMainWindow

from ..UI.generated.ui_Login import Ui_Login
from .._consts import WID_ID_LOGIN
from ..UI.style import parserStyle
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel
from ._abstract import AbstractView

style = parserStyle("""
QPushButton { %(button)s }
QPushButton::hover { %(button-hover)s }
""")


class ViewLogin(AbstractView):
    _id = WID_ID_LOGIN
    _style = style
    
    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__(window, events, model)

    def setup(self):
        super().setup()
        self.__ui = Ui_Login()
        self.__ui.setupUi(self._wid)

        # signals && slots
        self.__ui.btnAcessar.clicked.connect(self.on_btnAcessar_clicked)

    def on_btnAcessar_clicked(self):
        username = self.__ui.lineUsuario.text()
        password = self.__ui.lineSenha.text()

        if not username or not password:
            # TODO: solicitar preenchimento de todos os campos
            return
        
        self._model.setRemember(self.__ui.cbMnterConectado.isChecked())
        self._events.loginRequired.emit({'username': username, 'password': password})