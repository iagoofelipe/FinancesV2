import asyncio
from PySide6.QtCore import QObject

from ..views import MainView
from ..models import MainModel

__all__ = ['MainController']

class MainController(QObject):
    def __init__(self, model:MainModel, view:MainView) -> None:
        super().__init__()
        self.__model = model
        self.__view = view

    async def initialize(self):
        self.__view.initialize()

        success, error = await self.__model.initialize()
        print(error)

        print('MainController inicializado')