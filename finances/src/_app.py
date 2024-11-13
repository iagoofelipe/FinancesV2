import asyncio
from PySide6.QtWidgets import QApplication
import PySide6.QtAsyncio as QtAsyncio

from .views import MainView
from .controllers import MainController
from .models import MainModel

class FinancesApp:
    @property
    def qapp(self) -> QApplication:
        return self.__app
    
    def __init__(self):
        self.__app = QApplication()
        self.__model = MainModel()
        self.__view = MainView(self.__model)
        self.__controller = MainController(self.__model, self.__view)

    def exec(self):
        QtAsyncio.run(self.__controller.initialize(), handle_sigint=True)