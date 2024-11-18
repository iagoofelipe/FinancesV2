from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow

from ._login import ViewLogin
from ._loading import ViewLoading
from ._abstract import AbstractView
from ._home import ViewHome

from ..UI.style import style_global
from .._consts import *

from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

class AppView(QObject):
    initializationFinished = Signal()
    
    def __init__(self, events:AppEventHandler, model:AppModel):
        super().__init__()
        self.__events = events
        self.__model = model
        self.__currentUiId = -1
        self.__win = QMainWindow()
        self.__uis:dict[int, AbstractView] = {
            WID_ID_LOADING: ViewLoading(self.__win, self.__events, self.__model),
            WID_ID_LOGIN: ViewLogin(self.__win, self.__events, self.__model),
            WID_ID_HOME: ViewHome(self.__win, self.__events, self.__model),
        }
    
    def setup(self, uiId:int):
        if uiId not in self.__uis:
            raise ValueError(f'undefined ui by id "{uiId}"')

        ui = self.__uis[uiId]
        ui.setup()
        self.__currentUiId = uiId
        self.__win.setStyleSheet(style_global + ui.style)

    def checkCurrentUiById(self, uiId:int) -> bool:
        return self.__currentUiId == uiId

    def setLoadingMessage(self, text:str, setup=False):
        if self.__currentUiId != WID_ID_LOADING and setup:
            self.setup(WID_ID_LOADING)

        if self.__currentUiId == WID_ID_LOADING:
            self.__events.loadingMessageChanged.emit(text)

    def initialize(self):
        self.__win.setMinimumSize(1100, 670)
        self.setup(WID_ID_LOADING)
        self.__win.show()
        self.initializationFinished.emit()

    def showMessage(self, msg:str):
        #TODO: adicionar a UI
        print('Message:', msg)