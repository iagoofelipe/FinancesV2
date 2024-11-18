from PySide6.QtCore import QObject, Signal

from ._appevents import AppEventHandler
from ._appmodel import AppModel
from ..views._appview import AppView
from .._consts import WID_ID_LOGIN, WID_ID_HOME

class AppController(QObject):
    def __init__(self, events:AppEventHandler, model:AppModel, view:AppView):
        super().__init__()
        self.__events = events
        self.__model = model
        self.__view = view

        self.__model.initializationFinished.connect(self.on_initializationFinished)
        self.__events.loginFinished.connect(self.on_loginFinished)

    def initialize(self):
        self.__view.initialize()
        self.__model.initialize()

    def on_initializationFinished(self, result:dict):
        self.__events.initializationFinished.emit(result)

        if not result['success']:
            self.__view.setLoadingMessage(f'Error: {result['error']}')
            return 
        
        # verificando se o login deve ser feito
        if self.__model.remember():
            self.__view.setLoadingMessage('checking credentials...')
            self.__events.loginRequired.emit(self.__model.savedCredentials())
            return
        
        self.__view.setup(WID_ID_LOGIN)

    def on_loginFinished(self, result:dict):
        success = result['success']
        msg = result['error'] if not success else 'login finished'

        # alterando UI, caso necessário
        if not self.__view.checkCurrentUiById(WID_ID_LOGIN) and not success:
            self.__view.setup(WID_ID_LOGIN)

        self.__view.showMessage(msg)

        if success:
            self.__view.setup(WID_ID_HOME)