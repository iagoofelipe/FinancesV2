from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QLabel

from ._abstract import AbstractView
from .._consts import WID_ID_LOADING, LOADING_MESSAGE
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

class ViewLoading(AbstractView):
    _id = WID_ID_LOADING

    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__(window, events, model)
        self.__loadingLabel:QLabel = None

        events.loadingMessageChanged.connect(self.setMessage)

    def setup(self):
        super().setup()
        layout = QHBoxLayout(self._wid)
        self.__loadingLabel = QLabel(self._wid)
        self.__loadingLabel.setText(LOADING_MESSAGE)
        
        self.__loadingLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.__loadingLabel)

    def setMessage(self, msg:str):
        if self.__loadingLabel is None:
            print('setup required!')
        else:
            self.__loadingLabel.setText(msg)