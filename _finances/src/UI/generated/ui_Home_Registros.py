# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home_Registros.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import resource_rc

class Ui_Registros(object):
    def setupUi(self, Registros):
        if not Registros.objectName():
            Registros.setObjectName(u"Registros")
        Registros.resize(928, 579)
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(11)
        Registros.setFont(font)
        self.verticalLayout = QVBoxLayout(Registros)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Registros)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -279, 911, 858))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widDetalhamento = QWidget(self.scrollAreaWidgetContents)
        self.widDetalhamento.setObjectName(u"widDetalhamento")
        self.verticalLayout_4 = QVBoxLayout(self.widDetalhamento)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.widget_6 = QWidget(self.widDetalhamento)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.pushButton_7 = QPushButton(self.widget_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"p")
        icon = QIcon()
        icon.addFile(u":/root/icons/Trash 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(18, 18))
        self.pushButton_7.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_7)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.line_2 = QFrame(self.widDetalhamento)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.widget_5 = QWidget(self.widDetalhamento)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 500))

        self.verticalLayout_4.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widDetalhamento)

        self.widNovoLancamento = QWidget(self.scrollAreaWidgetContents)
        self.widNovoLancamento.setObjectName(u"widNovoLancamento")
        self.verticalLayout_3 = QVBoxLayout(self.widNovoLancamento)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.widget = QWidget(self.widNovoLancamento)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"p")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(18, 18))
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.widget)

        self.line = QFrame(self.widNovoLancamento)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.widget_2 = QWidget(self.widNovoLancamento)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout.addWidget(self.widget_3, 2, 5, 3, 1)

        self.lineEdit_5 = QLineEdit(self.widget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 5, 1, 1)

        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 0, 5, 1, 1)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.widget_2)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout.addWidget(self.doubleSpinBox, 4, 2, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"Assets/icons/Info.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(18, 18))
        self.pushButton_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(18, 18))
        self.pushButton_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/root/icons/Edit 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(18, 18))
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 4, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnLimpar = QPushButton(self.widget_4)
        self.btnLimpar.setObjectName(u"btnLimpar")
        self.btnLimpar.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.btnLimpar)

        self.btnSalvar = QPushButton(self.widget_4)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setMinimumSize(QSize(90, 0))

        self.horizontalLayout_2.addWidget(self.btnSalvar)


        self.gridLayout.addWidget(self.widget_4, 5, 0, 1, 6)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widNovoLancamento)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Registros)

        self.pushButton_7.setDefault(False)
        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Registros)
    # setupUi

    def retranslateUi(self, Registros):
        Registros.setWindowTitle(QCoreApplication.translate("Registros", u"Form", None))
        self.label_10.setText(QCoreApplication.translate("Registros", u"Detalhamento", None))
        self.pushButton_7.setText("")
        self.label.setText(QCoreApplication.translate("Registros", u"Novo Lan\u00e7amento", None))
        self.pushButton.setText("")
        self.label_5.setText(QCoreApplication.translate("Registros", u"recorr\u00eancia", None))
        self.label_4.setText(QCoreApplication.translate("Registros", u"data/hora", None))
        self.label_7.setText(QCoreApplication.translate("Registros", u"m\u00e9todo", None))
        self.label_6.setText(QCoreApplication.translate("Registros", u"valor", None))
        self.label_8.setText(QCoreApplication.translate("Registros", u"descri\u00e7\u00e3o", None))
        self.label_9.setText(QCoreApplication.translate("Registros", u"categorias", None))
        self.label_2.setText(QCoreApplication.translate("Registros", u"tipo", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_3.setText(QCoreApplication.translate("Registros", u"t\u00edtulo", None))
        self.pushButton_4.setText("")
        self.btnLimpar.setText(QCoreApplication.translate("Registros", u"limpar", None))
        self.btnSalvar.setText(QCoreApplication.translate("Registros", u"salvar", None))
    # retranslateUi

