from PySide6.QtCore import QObject, Signal

class AppEventHandler(QObject):
    initializationFinished = Signal(dict)
    loginRequired = Signal(dict)
    loginFinished = Signal(dict)
    quitRequired = Signal()

    def __init__(self):
        super().__init__()