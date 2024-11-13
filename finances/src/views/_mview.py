import asyncio
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject

from ..models import MainModel
from ._login import LoginView
from .._consts import WINDOW_HEIGHT, WINDOW_WIDTH

__all__ = ['MainView']

class MainView(QObject):
    def __init__(self, model:MainModel) -> None:
        super().__init__()

        self.__model = model
        self.__window = QMainWindow()
        self.__login = LoginView(self.__window)
        self.__window.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    def initialize(self):
        self.__window.show()
        self.__login.setup()
        print('MainView inicializado')