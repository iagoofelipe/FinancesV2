from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QLabel

from ._login import ViewLogin
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

class AppView(QObject):
    initializationFinished = Signal()
    
    def __init__(self, events:AppEventHandler, model:AppModel):
        super().__init__()
        self.__events = events
        self.__model = model
        self.__loadingLabel:QLabel = None
        self.__currentUiName = ''
        self.__win = QMainWindow()
        self.__login = ViewLogin(self.__win, self.__events, self.__model)
    
    def __setupLoading(self):
        wid = QWidget(self.__win)
        layout = QHBoxLayout(wid)
        self.__loadingLabel = QLabel(wid)
        
        self.__loadingLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.__loadingLabel)
        self.__win.setCentralWidget(wid)
    
    def setup(self, uiName:str):
        self.__loadingLabel = None
        self.__currentUiName = uiName

        match uiName:
            case 'Login':
                self.__login.setup()
            case 'Loading':
                self.__setupLoading()
            case 'Home':
                self.setLoadingMessage('Page Home', True)
            case _:
                raise ValueError(f'undefined ui "{uiName}"')

    def checkCurrentUiByName(self, uiName:str) -> bool:
        return self.__currentUiName == uiName

    def setLoadingMessage(self, text:str, setup=False):
        if self.__currentUiName != 'Loading' and setup:
            self.setup('Loading')

        if self.__loadingLabel is not None:
            self.__loadingLabel.setText(text)

    def initialize(self):
        self.__win.setMinimumSize(1100, 670)
        self.setLoadingMessage('inicializando componentes...', True)
        self.__win.show()
        self.initializationFinished.emit()

    def showMessage(self, msg:str):
        #TODO: adicionar a UI
        print('Message:', msg)