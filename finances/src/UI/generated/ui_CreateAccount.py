# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateAccount.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CreateAccount(object):
    def setupUi(self, CreateAccount):
        if not CreateAccount.objectName():
            CreateAccount.setObjectName(u"CreateAccount")
        CreateAccount.resize(1100, 670)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        CreateAccount.setFont(font)
        self.horizontalLayout = QHBoxLayout(CreateAccount)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(354, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(CreateAccount)
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

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.linePrimeiroNome = QLineEdit(self.widget_4)
        self.linePrimeiroNome.setObjectName(u"linePrimeiroNome")

        self.horizontalLayout_4.addWidget(self.linePrimeiroNome)

        self.lineUltimoNome = QLineEdit(self.widget_4)
        self.lineUltimoNome.setObjectName(u"lineUltimoNome")

        self.horizontalLayout_4.addWidget(self.lineUltimoNome)


        self.verticalLayout.addWidget(self.widget_4)

        self.lineSenha = QLineEdit(self.widget_3)
        self.lineSenha.setObjectName(u"lineSenha")

        self.verticalLayout.addWidget(self.lineSenha)

        self.lineSenhaRepetir = QLineEdit(self.widget_3)
        self.lineSenhaRepetir.setObjectName(u"lineSenhaRepetir")

        self.verticalLayout.addWidget(self.lineSenhaRepetir)

        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.btnCriar = QPushButton(self.widget_3)
        self.btnCriar.setObjectName(u"btnCriar")
        self.btnCriar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnCriar)

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

        self.btnAcessar = QPushButton(self.widget)
        self.btnAcessar.setObjectName(u"btnAcessar")
        font2 = QFont()
        font2.setUnderline(True)
        self.btnAcessar.setFont(font2)
        self.btnAcessar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAcessar.setStyleSheet(u"padding: 0; background-color: transparent;")
        self.btnAcessar.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnAcessar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 171, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalSpacer_2 = QSpacerItem(354, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        QWidget.setTabOrder(self.linePrimeiroNome, self.lineUltimoNome)
        QWidget.setTabOrder(self.lineUltimoNome, self.lineSenha)
        QWidget.setTabOrder(self.lineSenha, self.lineSenhaRepetir)
        QWidget.setTabOrder(self.lineSenhaRepetir, self.btnCriar)
        QWidget.setTabOrder(self.btnCriar, self.btnAcessar)

        self.retranslateUi(CreateAccount)

        QMetaObject.connectSlotsByName(CreateAccount)
    # setupUi

    def retranslateUi(self, CreateAccount):
        CreateAccount.setWindowTitle(QCoreApplication.translate("CreateAccount", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateAccount", u"Finances", None))
        self.linePrimeiroNome.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"Primeiro Nome", None))
        self.lineUltimoNome.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"\u00daltimo Nome", None))
        self.lineSenha.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"Senha", None))
        self.lineSenhaRepetir.setPlaceholderText(QCoreApplication.translate("CreateAccount", u"digite sua senha novamente", None))
        self.btnCriar.setText(QCoreApplication.translate("CreateAccount", u"criar conta", None))
        self.label_2.setText(QCoreApplication.translate("CreateAccount", u"j\u00e1 possui uma conta? ", None))
        self.btnAcessar.setText(QCoreApplication.translate("CreateAccount", u"acesse agora", None))
    # retranslateUi

