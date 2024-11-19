from PySide6.QtCore import QObject, Signal

class AppEventHandler(QObject):
    # Authentication
    loginRequired = Signal(dict)
    loginFinished = Signal(dict)
    logoutRequired = Signal()
    logoutFinished = Signal()
    createAccountRequired = Signal(dict)
    createAccountFinished = Signal(dict)

    # Application
    initializationFinished = Signal(dict)
    quitRequired = Signal()

    # UI
    loadingMessageChanged = Signal(str)
    changeUiById = Signal(int)
    showPopup = Signal(str)

    # Data
    userDataUpdated = Signal(dict)

    def __init__(self):
        super().__init__()