from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow

__all__ = ['MainViewModel']

from _finances.src.models._main import MainModel

class MainViewModel(QObject):
    initializationFinished = Signal()

    def __init__(self, model:MainModel) -> None:
        super().__init__()
        self.__window = QMainWindow()
        self.__model = model

    async def initialize(self):
        self.__window.show()
        print('initializing MainModel...')
        await self.__model.initialize()
        print('initialization of MainModel finished')
        self.initializationFinished.emit()