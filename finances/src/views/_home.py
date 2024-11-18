from PySide6.QtWidgets import QMainWindow, QWidget

from ._abstract import AbstractView
from .._consts import *
from ..UI.style import parserStyle
from ..UI.generated.ui_Home import Ui_Home
from ..UI.generated.ui_Home_Registros import Ui_Registros
from ..backend._appevents import AppEventHandler
from ..backend._appmodel import AppModel

style = parserStyle("""

#widSidebar, #widTopbar, #widDetalhamento, #widNovoLancamento { %(box)s }
                    
#btnLimpar, #btnSalvar { %(button)s }
                    
#btnLimpar::hover, #btnSalvar::hover { %(button-hover)s }

""")

class ViewHome(AbstractView):
    _id = WID_ID_HOME
    _style = style
    _components = COMPONENTS_HOME

    def __init__(self, window:QMainWindow, events:AppEventHandler, model:AppModel):
        super().__init__(window, events, model)
        self.__user_name = 'Usuário'
        self.__setupFinished = False

        self._events.userDataUpdated.connect(self.updateUserFields)
    
    def setup(self):
        self.__setupFinished = False
        self.__ui = Ui_Home()

        super().setup()
        self.__ui.setupUi(self._wid)
        self.__widComponent = self.__ui.widContent
        self.setupComponent()

        self.__setupFinished = True
        self.updateUserFields()

    def setupComponent(self, compId:int=COMPONENT_HOME_REGISTRY):
        if compId not in self._components:
            raise ValueError(f'component with id {compId} not implemented')
        
        old = self.__widComponent
        new = QWidget(self.__ui.widCentral)

        if compId == COMPONENT_HOME_DASHBOARD:
            pass
        
        elif compId == COMPONENT_HOME_REGISTRY:
            self.__ui_registros = Ui_Registros()
            self.__ui_registros.setupUi(new)

        elif compId == COMPONENT_HOME_CARD:
            pass

        self.__widComponent = new
        self.__ui.layoutCentral.replaceWidget(old, new)
        old.deleteLater()

    def updateUserFields(self, data:dict=None):
        if data is not None:
            self.__user_name = f'{data.get('first_name', 'Usuário')} {data.get('last_name', '')}'
            
        if self.__setupFinished:
            self.__ui.lbUser.setText(self.__user_name)