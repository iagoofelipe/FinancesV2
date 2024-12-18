# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from . import resource_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1100, 670)
        self.horizontalLayout = QHBoxLayout(Home)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 15, 15, 15)
        self.widSidebar = QWidget(Home)
        self.widSidebar.setObjectName(u"widSidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widSidebar.sizePolicy().hasHeightForWidth())
        self.widSidebar.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.widSidebar)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 15, 10)
        self.btnUserProfile = QPushButton(self.widSidebar)
        self.btnUserProfile.setObjectName(u"btnUserProfile")
        self.btnUserProfile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/root/icons/User.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnUserProfile.setIcon(icon)
        self.btnUserProfile.setIconSize(QSize(20, 20))
        self.btnUserProfile.setFlat(True)

        self.gridLayout.addWidget(self.btnUserProfile, 4, 0, 1, 1)

        self.btnDash = QPushButton(self.widSidebar)
        self.btnDash.setObjectName(u"btnDash")
        self.btnDash.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/root/icons/Trello.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnDash.setIcon(icon1)
        self.btnDash.setIconSize(QSize(20, 20))
        self.btnDash.setFlat(True)

        self.gridLayout.addWidget(self.btnDash, 0, 0, 1, 1)

        self.label = QLabel(self.widSidebar)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widSidebar)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widSidebar)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_3 = QLabel(self.widSidebar)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.btnCards = QPushButton(self.widSidebar)
        self.btnCards.setObjectName(u"btnCards")
        self.btnCards.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/root/icons/Credit card.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnCards.setIcon(icon2)
        self.btnCards.setIconSize(QSize(20, 20))
        self.btnCards.setFlat(True)

        self.gridLayout.addWidget(self.btnCards, 2, 0, 1, 1)

        self.btnRegistry = QPushButton(self.widSidebar)
        self.btnRegistry.setObjectName(u"btnRegistry")
        self.btnRegistry.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/root/icons/Clipboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnRegistry.setIcon(icon3)
        self.btnRegistry.setIconSize(QSize(20, 20))
        self.btnRegistry.setFlat(True)

        self.gridLayout.addWidget(self.btnRegistry, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.btnSettings = QPushButton(self.widSidebar)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/root/icons/Settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnSettings.setIcon(icon4)
        self.btnSettings.setIconSize(QSize(18, 18))
        self.btnSettings.setFlat(True)

        self.gridLayout.addWidget(self.btnSettings, 5, 0, 1, 1)

        self.label_5 = QLabel(self.widSidebar)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widSidebar)

        self.widCentral = QWidget(Home)
        self.widCentral.setObjectName(u"widCentral")
        self.layoutCentral = QVBoxLayout(self.widCentral)
        self.layoutCentral.setSpacing(15)
        self.layoutCentral.setObjectName(u"layoutCentral")
        self.layoutCentral.setContentsMargins(0, 0, 0, 0)
        self.widTopbar = QWidget(self.widCentral)
        self.widTopbar.setObjectName(u"widTopbar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widTopbar.sizePolicy().hasHeightForWidth())
        self.widTopbar.setSizePolicy(sizePolicy1)
        self.widTopbar.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widTopbar)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 5, 10)
        self.label_7 = QLabel(self.widTopbar)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/root/icons/User-topbar.png"))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.widget = QWidget(self.widTopbar)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbUser = QLabel(self.widget)
        self.lbUser.setObjectName(u"lbUser")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbUser.setFont(font)

        self.verticalLayout_2.addWidget(self.lbUser)

        self.lbProfileDateRange = QLabel(self.widget)
        self.lbProfileDateRange.setObjectName(u"lbProfileDateRange")

        self.verticalLayout_2.addWidget(self.lbProfileDateRange)


        self.horizontalLayout_2.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnDateRange = QPushButton(self.widTopbar)
        self.btnDateRange.setObjectName(u"btnDateRange")
        self.btnDateRange.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/root/icons/Calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnDateRange.setIcon(icon5)
        self.btnDateRange.setIconSize(QSize(18, 18))
        self.btnDateRange.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnDateRange)

        self.btnChangeProfile = QPushButton(self.widTopbar)
        self.btnChangeProfile.setObjectName(u"btnChangeProfile")
        self.btnChangeProfile.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/root/icons/Repeat.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnChangeProfile.setIcon(icon6)
        self.btnChangeProfile.setIconSize(QSize(18, 18))
        self.btnChangeProfile.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnChangeProfile)

        self.btnLogout = QPushButton(self.widTopbar)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnLogout.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/root/icons/Log out.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btnLogout.setIcon(icon7)
        self.btnLogout.setIconSize(QSize(18, 18))
        self.btnLogout.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btnLogout)


        self.layoutCentral.addWidget(self.widTopbar)

        self.widContent = QWidget(self.widCentral)
        self.widContent.setObjectName(u"widContent")

        self.layoutCentral.addWidget(self.widContent)


        self.horizontalLayout.addWidget(self.widCentral)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Form", None))
        self.btnUserProfile.setText("")
        self.btnDash.setText("")
        self.label.setText(QCoreApplication.translate("Home", u"dashboards", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"registros", None))
        self.label_4.setText(QCoreApplication.translate("Home", u"perfil e usu\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("Home", u"contas e cart\u00f5es", None))
        self.btnCards.setText("")
        self.btnRegistry.setText("")
        self.btnSettings.setText("")
        self.label_5.setText(QCoreApplication.translate("Home", u"configura\u00e7\u00f5es", None))
        self.label_7.setText("")
        self.lbUser.setText(QCoreApplication.translate("Home", u"<USER>", None))
        self.lbProfileDateRange.setText(QCoreApplication.translate("Home", u"<profile>, <dateRange>", None))
        self.btnDateRange.setText("")
        self.btnChangeProfile.setText("")
        self.btnLogout.setText("")
    # retranslateUi

