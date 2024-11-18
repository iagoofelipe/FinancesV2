from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QLabel

from ._abstract import AbstractView
from .._consts import WID_ID_HOME
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

class ViewHome(AbstractView):
    _id = WID_ID_HOME

    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__(window, events, model)
    
    def setup(self):
        super().setup()
        layout = QHBoxLayout(self._wid)
        label = QLabel(self._wid)
        label.setText('Page Home')
        
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)