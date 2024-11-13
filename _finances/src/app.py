from PySide6.QtWidgets import QApplication
from .vmodels import MainViewModel
from .models import MainModel
import asyncio

class FinancesApp(QApplication):
    def __init__(self):
        super().__init__()
        self.__model = MainModel()
        self.__vmodel = MainViewModel(self.__model)

    def exec(self) -> int:
        asyncio.run(self.__vmodel.initialize())
        return super().exec()
