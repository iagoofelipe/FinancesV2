import asyncio
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton
from threading import Thread
import PySide6.QtAsyncio as QtAsyncio

async def btnClicked():
    print('await iniciado')
    await asyncio.sleep(3)
    print('await finalizado')

if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    wid = QWidget()
    layout = QHBoxLayout(wid)
    btn = QPushButton('clicar', wid)
    
    layout.addWidget(btn)
    btn.clicked.connect(lambda: asyncio.ensure_future(btnClicked()))
    window.setCentralWidget(wid)
    window.setMinimumSize(1100, 670)
    window.show()
    
    QtAsyncio.run(handle_sigint=True)