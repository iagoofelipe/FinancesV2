from .src._app import FinancesApp
from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = FinancesApp()
    app.exec()