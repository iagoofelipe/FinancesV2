from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from UI.ui_Home import Ui_Home
from UI.ui_Home_Registros import Ui_Registros

from config import *

style = parserStyle(style_global + """

#widSidebar, #widTopbar, #widDetalhamento, #widNovoLancamento { %(box)s }
                    
#btnLimpar, #btnSalvar { %(button)s }
                    
#btnLimpar::hover, #btnSalvar::hover { %(button-hover)s }

""")


if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    wid = QWidget(window)
    ui = Ui_Home()
    ui_registros = Ui_Registros()

    # configurando components
    window.setMinimumSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setFont(font)
    window.setStyleSheet(style)
    ui.setupUi(wid)
    wid_registros = QWidget(ui.widCentral)
    ui_registros.setupUi(wid_registros)
    window.setCentralWidget(wid)

    # adicionando conteúdo
    old = ui.widContent
    ui.widContent = wid_registros
    ui.layoutCentral.replaceWidget(old, wid_registros)
    old.deleteLater()
    # wid.setFont(font)
    font2 = QFont()
    font2.setFamilies([u"Calibri"])
    font2.setPointSize(15)
    ui_registros.scrollAreaWidgetContents.setFont(font2)

    window.show()
    app.exec()