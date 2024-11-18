from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette, QColor

from .views._appview import AppView
from .UI.style import style_settings
from .backend._appevents import AppEventHandler
from .backend._appmodel import AppModel
from .backend._appcontroller import AppController

__all__ = ['FinancesApp']

class FinancesApp(QApplication):
    def __init__(self):
        super().__init__()
        self.__events = AppEventHandler()
        self.__model = AppModel(self.__events)
        self.__view = AppView(self.__events, self.__model)
        self.__controller = AppController(self.__events, self.__model, self.__view)

        self.setPalette(QPalette(QColor(style_settings['fill-background']))) # dark theme
        self.aboutToQuit.connect(lambda: self.__events.quitRequired.emit())

    def exec(self) -> int:
        self.__controller.initialize()
        return QApplication.exec()