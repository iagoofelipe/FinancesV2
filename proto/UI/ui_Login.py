# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1100, 670)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        Login.setFont(font)
        self.horizontalLayout = QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(354, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(Login)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(40)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineUsuario = QLineEdit(self.widget_3)
        self.lineUsuario.setObjectName(u"lineUsuario")

        self.verticalLayout.addWidget(self.lineUsuario)

        self.lineSenha = QLineEdit(self.widget_3)
        self.lineSenha.setObjectName(u"lineSenha")

        self.verticalLayout.addWidget(self.lineSenha)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.cbMnterConectado = QCheckBox(self.widget_2)
        self.cbMnterConectado.setObjectName(u"cbMnterConectado")

        self.horizontalLayout_3.addWidget(self.cbMnterConectado)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.widget_2)

        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btnAcessar = QPushButton(self.widget_3)
        self.btnAcessar.setObjectName(u"btnAcessar")
        self.btnAcessar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnAcessar)

        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btnCriar = QPushButton(self.widget)
        self.btnCriar.setObjectName(u"btnCriar")
        font2 = QFont()
        font2.setUnderline(True)
        self.btnCriar.setFont(font2)
        self.btnCriar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCriar.setStyleSheet(u"padding: 0; background-color: transparent;")
        self.btnCriar.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnCriar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 171, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalSpacer_2 = QSpacerItem(354, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        QWidget.setTabOrder(self.lineUsuario, self.lineSenha)
        QWidget.setTabOrder(self.lineSenha, self.cbMnterConectado)
        QWidget.setTabOrder(self.cbMnterConectado, self.btnAcessar)
        QWidget.setTabOrder(self.btnAcessar, self.btnCriar)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText(QCoreApplication.translate("Login", u"Finances", None))
        self.lineUsuario.setPlaceholderText(QCoreApplication.translate("Login", u"usu\u00e1rio", None))
        self.lineSenha.setPlaceholderText(QCoreApplication.translate("Login", u"senha", None))
        self.cbMnterConectado.setText(QCoreApplication.translate("Login", u"manter conectado", None))
        self.btnAcessar.setText(QCoreApplication.translate("Login", u"acessar conta", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"n\u00e3o possui uma conta? ", None))
        self.btnCriar.setText(QCoreApplication.translate("Login", u"crie agora", None))
    # retranslateUi

