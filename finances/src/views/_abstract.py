from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMainWindow, QWidget
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

class AbstractView(QObject):
    _id = -1
    _style = ''

    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__()
        self._wid:QWidget = None
        self.__win = window
        self._events = events
        self._model = model

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def style(self) -> str:
        return self._style
    
    def setup(self):
        self._wid = QWidget(self.__win)
        self.__win.setCentralWidget(self._wid)