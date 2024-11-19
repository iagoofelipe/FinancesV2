from PySide6.QtWidgets import QMainWindow

from ..UI.style import parserStyle
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel
from ._abstract import AbstractView

from ..UI.generated.ui_CreateAccount import Ui_CreateAccount
from .._consts import WID_ID_CREATE_ACCOUNT, WID_ID_LOGIN, WINDOW_TITLE

style = parserStyle("""
QPushButton { %(button)s }
QPushButton::hover { %(button-hover)s }
""")

class ViewCreateAccount(AbstractView):
    _id = WID_ID_CREATE_ACCOUNT
    _style = style
    _win_title = f'crie sua conta | {WINDOW_TITLE}'

    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__(window, events, model)

    def setup(self):
        super().setup()
        self.__ui = Ui_CreateAccount()
        self.__ui.setupUi(self._wid)

        # widgets que serão bloqueados durante criação do usuário
        # fields_to_block = [self.__ui.linePrimeiroNome, self.__ui.line]

        # signals && slots
        self.__ui.btnAcessar.clicked.connect(lambda: self._events.changeUiById.emit(WID_ID_LOGIN))
        self.__ui.btnCriar.clicked.connect(self.on_btnCriar_clicked)

    def on_btnCriar_clicked(self):
        password = self.__ui.lineSenha.text()
        confirm_password = self.__ui.lineSenhaRepetir.text()

        if password != confirm_password:
            self._events.showPopup.emit("password doesn't match with confirmation")
            return

        data = {
            'first_name': self.__ui.linePrimeiroNome.text(),
            'last_name': self.__ui.lineUltimoNome.text(),
            'username': self.__ui.lineUsuario.text(),
            'email': self.__ui.lineEmail.text(),
            'password': password,
        }

        # verificandos e todos os campos estão preenchidos
        for v in data.values():
            if not v:
                self._events.showPopup.emit("empty field found")
                return
        
        self._events.createAccountRequired.emit(data)

