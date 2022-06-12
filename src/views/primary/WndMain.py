# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WndMain.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(1000, 560)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border:none;\n"
"")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle = QFrame(self.topBar)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMaximumSize(QSize(60, 40))
        self.toggle.setStyleSheet(u"background-color: rgb(65, 43, 173);")
        self.toggle.setFrameShape(QFrame.StyledPanel)
        self.toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnToggle = QPushButton(self.toggle)
        self.btnToggle.setObjectName(u"btnToggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnToggle.sizePolicy().hasHeightForWidth())
        self.btnToggle.setSizePolicy(sizePolicy)
        self.btnToggle.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-color: rgb(122, 100, 189);\n"
"background-image: url(:/icons/toggleIcon.png);\n"
"background-repeat:none;\n"
"background-position: center center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.btnToggle)


        self.horizontalLayout.addWidget(self.toggle)

        self.description = QFrame(self.topBar)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"border:none;\n"
"")
        self.description.setFrameShape(QFrame.StyledPanel)
        self.description.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.description)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frName = QFrame(self.description)
        self.frName.setObjectName(u"frName")
        self.frName.setFrameShape(QFrame.StyledPanel)
        self.frName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frName)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbName = QLabel(self.frName)
        self.lbName.setObjectName(u"lbName")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbName.setFont(font)

        self.horizontalLayout_6.addWidget(self.lbName)


        self.horizontalLayout_5.addWidget(self.frName)

        self.frDate = QFrame(self.description)
        self.frDate.setObjectName(u"frDate")
        self.frDate.setFrameShape(QFrame.StyledPanel)
        self.frDate.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frDate)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbDate = QLabel(self.frDate)
        self.lbDate.setObjectName(u"lbDate")
        self.lbDate.setFont(font)
        self.lbDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbDate)


        self.horizontalLayout_5.addWidget(self.frDate)

        self.frPageDescription = QFrame(self.description)
        self.frPageDescription.setObjectName(u"frPageDescription")
        self.frPageDescription.setFrameShape(QFrame.StyledPanel)
        self.frPageDescription.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frPageDescription)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbPageDescription = QLabel(self.frPageDescription)
        self.lbPageDescription.setObjectName(u"lbPageDescription")
        self.lbPageDescription.setFont(font)
        self.lbPageDescription.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbPageDescription.setMargin(5)

        self.horizontalLayout_8.addWidget(self.lbPageDescription)


        self.horizontalLayout_5.addWidget(self.frPageDescription)


        self.horizontalLayout.addWidget(self.description)


        self.verticalLayout.addWidget(self.topBar)

        self.mainWidget = QFrame(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setFrameShape(QFrame.NoFrame)
        self.mainWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.mainWidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(60, 0))
        self.leftMenu.setMaximumSize(QSize(60, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border:none\n"
"")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.leftMenu)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.StyledPanel)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topMenus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.topMenus)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy1)
        self.btnHome.setMinimumSize(QSize(60, 40))
        self.btnHome.setFont(font)
        self.btnHome.setLayoutDirection(Qt.LeftToRight)
        self.btnHome.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/homeIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}\n"
"\n"
"")
        self.btnHome.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnHome)

        self.btnFood = QPushButton(self.topMenus)
        self.btnFood.setObjectName(u"btnFood")
        self.btnFood.setMinimumSize(QSize(0, 40))
        self.btnFood.setFont(font)
        self.btnFood.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/food.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnFood.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnFood)

        self.btnStatistic = QPushButton(self.topMenus)
        self.btnStatistic.setObjectName(u"btnStatistic")
        self.btnStatistic.setMinimumSize(QSize(0, 40))
        self.btnStatistic.setFont(font)
        self.btnStatistic.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/statisticIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnStatistic.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnStatistic)

        self.btnSettings = QPushButton(self.topMenus)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(0, 40))
        self.btnSettings.setFont(font)
        self.btnSettings.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/settingsIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnSettings.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnSettings)


        self.verticalLayout_2.addWidget(self.topMenus, 0, Qt.AlignTop)

        self.bottonMenus = QFrame(self.leftMenu)
        self.bottonMenus.setObjectName(u"bottonMenus")
        self.bottonMenus.setFrameShape(QFrame.StyledPanel)
        self.bottonMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bottonMenus)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnLogout = QPushButton(self.bottonMenus)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(0, 40))
        self.btnLogout.setFont(font)
        self.btnLogout.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/logoutIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnLogout.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.btnLogout)


        self.verticalLayout_2.addWidget(self.bottonMenus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.content = QFrame(self.mainWidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.content)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.pageHome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.pageHome)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topContent = QFrame(self.pageHome)
        self.topContent.setObjectName(u"topContent")
        self.topContent.setMaximumSize(QSize(16777215, 260))
        self.topContent.setFrameShape(QFrame.StyledPanel)
        self.topContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.topContent)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.topContent)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame)

        self.frmProgressBar = QFrame(self.topContent)
        self.frmProgressBar.setObjectName(u"frmProgressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frmProgressBar.sizePolicy().hasHeightForWidth())
        self.frmProgressBar.setSizePolicy(sizePolicy2)
        self.frmProgressBar.setMinimumSize(QSize(260, 0))
        self.frmProgressBar.setMaximumSize(QSize(16777215, 260))
        font1 = QFont()
        font1.setFamilies([u"Script"])
        self.frmProgressBar.setFont(font1)
        self.frmProgressBar.setFrameShape(QFrame.StyledPanel)
        self.frmProgressBar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frmProgressBar)

        self.frame_3 = QFrame(self.topContent)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.topContent)

        self.bottemContent = QFrame(self.pageHome)
        self.bottemContent.setObjectName(u"bottemContent")
        self.bottemContent.setFrameShape(QFrame.StyledPanel)
        self.bottemContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.bottemContent)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.trackContent = QFrame(self.bottemContent)
        self.trackContent.setObjectName(u"trackContent")
        self.trackContent.setFrameShape(QFrame.StyledPanel)
        self.trackContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.trackContent)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.weightContent = QFrame(self.trackContent)
        self.weightContent.setObjectName(u"weightContent")
        self.weightContent.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.weightContent.setFrameShape(QFrame.StyledPanel)
        self.weightContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.weightContent)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbWeight = QLabel(self.weightContent)
        self.lbWeight.setObjectName(u"lbWeight")
        self.lbWeight.setFont(font)

        self.horizontalLayout_4.addWidget(self.lbWeight)

        self.leWeight = QLineEdit(self.weightContent)
        self.leWeight.setObjectName(u"leWeight")
        self.leWeight.setMaximumSize(QSize(200, 16777215))
        self.leWeight.setFont(font)
        self.leWeight.setStyleSheet(u"border-bottom: 2px solid rgb(143, 126, 230);;\n"
"")
        self.leWeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.leWeight)


        self.verticalLayout_9.addWidget(self.weightContent)

        self.stepContent = QFrame(self.trackContent)
        self.stepContent.setObjectName(u"stepContent")
        self.stepContent.setFont(font)
        self.stepContent.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.stepContent.setFrameShape(QFrame.StyledPanel)
        self.stepContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.stepContent)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbSteps = QLabel(self.stepContent)
        self.lbSteps.setObjectName(u"lbSteps")
        self.lbSteps.setFont(font)
        self.lbSteps.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.lbSteps)

        self.leSteps = QLineEdit(self.stepContent)
        self.leSteps.setObjectName(u"leSteps")
        self.leSteps.setMaximumSize(QSize(200, 16777215))
        self.leSteps.setFont(font)
        self.leSteps.setStyleSheet(u"border-bottom: 2px solid rgb(143, 126, 230);;\n"
"")
        self.leSteps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.leSteps)


        self.verticalLayout_9.addWidget(self.stepContent)

        self.bpContent = QFrame(self.trackContent)
        self.bpContent.setObjectName(u"bpContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bpContent.sizePolicy().hasHeightForWidth())
        self.bpContent.setSizePolicy(sizePolicy3)
        self.bpContent.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.bpContent.setFrameShape(QFrame.StyledPanel)
        self.bpContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.bpContent)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbBP = QLabel(self.bpContent)
        self.lbBP.setObjectName(u"lbBP")
        self.lbBP.setFont(font)

        self.horizontalLayout_10.addWidget(self.lbBP)

        self.leBPLow = QLineEdit(self.bpContent)
        self.leBPLow.setObjectName(u"leBPLow")
        self.leBPLow.setMaximumSize(QSize(94, 16777215))
        self.leBPLow.setFont(font)
        self.leBPLow.setStyleSheet(u"border-bottom: 2px solid rgb(143, 126, 230);;\n"
"")
        self.leBPLow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.leBPLow)

        self.leBPHigh = QLineEdit(self.bpContent)
        self.leBPHigh.setObjectName(u"leBPHigh")
        self.leBPHigh.setMaximumSize(QSize(100, 16777215))
        self.leBPHigh.setFont(font)
        self.leBPHigh.setStyleSheet(u"border-bottom: 2px solid rgb(143, 126, 230);;\n"
"")
        self.leBPHigh.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.leBPHigh)


        self.verticalLayout_9.addWidget(self.bpContent)


        self.verticalLayout_7.addWidget(self.trackContent)

        self.frmButtonSubmit = QFrame(self.bottemContent)
        self.frmButtonSubmit.setObjectName(u"frmButtonSubmit")
        self.frmButtonSubmit.setMaximumSize(QSize(16777215, 40))
        self.frmButtonSubmit.setFrameShape(QFrame.StyledPanel)
        self.frmButtonSubmit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frmButtonSubmit)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bufferLeft = QFrame(self.frmButtonSubmit)
        self.bufferLeft.setObjectName(u"bufferLeft")
        self.bufferLeft.setMinimumSize(QSize(400, 0))
        self.bufferLeft.setFrameShape(QFrame.StyledPanel)
        self.bufferLeft.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.bufferLeft)

        self.frmBtn = QFrame(self.frmButtonSubmit)
        self.frmBtn.setObjectName(u"frmBtn")
        self.frmBtn.setFrameShape(QFrame.StyledPanel)
        self.frmBtn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frmBtn)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnSubmit = QPushButton(self.frmBtn)
        self.btnSubmit.setObjectName(u"btnSubmit")
        sizePolicy1.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy1)
        self.btnSubmit.setMinimumSize(QSize(140, 40))
        self.btnSubmit.setMaximumSize(QSize(16777215, 140))
        self.btnSubmit.setFont(font)
        self.btnSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btnSubmit)


        self.horizontalLayout_11.addWidget(self.frmBtn)

        self.bufferRight = QFrame(self.frmButtonSubmit)
        self.bufferRight.setObjectName(u"bufferRight")
        self.bufferRight.setMinimumSize(QSize(400, 0))
        self.bufferRight.setFrameShape(QFrame.StyledPanel)
        self.bufferRight.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.bufferRight)


        self.verticalLayout_7.addWidget(self.frmButtonSubmit)


        self.verticalLayout_5.addWidget(self.bottemContent)

        self.pages.addWidget(self.pageHome)
        self.pageFood = QWidget()
        self.pageFood.setObjectName(u"pageFood")
        self.pages.addWidget(self.pageFood)
        self.pageStatKcal = QWidget()
        self.pageStatKcal.setObjectName(u"pageStatKcal")
        self.verticalLayout_13 = QVBoxLayout(self.pageStatKcal)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentKcal = QFrame(self.pageStatKcal)
        self.frmTopContentKcal.setObjectName(u"frmTopContentKcal")
        self.frmTopContentKcal.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frmTopContentKcal)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat1 = QFrame(self.frmTopContentKcal)
        self.frmTopLeftStat1.setObjectName(u"frmTopLeftStat1")
        self.frmTopLeftStat1.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frmTopLeftStat1)

        self.frmTopBtnKcal = QFrame(self.frmTopContentKcal)
        self.frmTopBtnKcal.setObjectName(u"frmTopBtnKcal")
        self.frmTopBtnKcal.setMinimumSize(QSize(500, 0))
        self.frmTopBtnKcal.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frmTopBtnKcal)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btnKcal1 = QPushButton(self.frmTopBtnKcal)
        self.btnKcal1.setObjectName(u"btnKcal1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnKcal1.sizePolicy().hasHeightForWidth())
        self.btnKcal1.setSizePolicy(sizePolicy4)
        self.btnKcal1.setFont(font)
        self.btnKcal1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnKcal1)

        self.btnSteps1 = QPushButton(self.frmTopBtnKcal)
        self.btnSteps1.setObjectName(u"btnSteps1")
        sizePolicy4.setHeightForWidth(self.btnSteps1.sizePolicy().hasHeightForWidth())
        self.btnSteps1.setSizePolicy(sizePolicy4)
        self.btnSteps1.setFont(font)
        self.btnSteps1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnSteps1)

        self.btnBP1 = QPushButton(self.frmTopBtnKcal)
        self.btnBP1.setObjectName(u"btnBP1")
        sizePolicy4.setHeightForWidth(self.btnBP1.sizePolicy().hasHeightForWidth())
        self.btnBP1.setSizePolicy(sizePolicy4)
        self.btnBP1.setFont(font)
        self.btnBP1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnBP1)


        self.horizontalLayout_14.addWidget(self.frmTopBtnKcal)

        self.frmTopRightStat1 = QFrame(self.frmTopContentKcal)
        self.frmTopRightStat1.setObjectName(u"frmTopRightStat1")
        self.frmTopRightStat1.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frmTopRightStat1)


        self.verticalLayout_13.addWidget(self.frmTopContentKcal)

        self.frmContentKcal = QFrame(self.pageStatKcal)
        self.frmContentKcal.setObjectName(u"frmContentKcal")
        self.frmContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmContentKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frmContentKcal)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentKcal = QFrame(self.frmContentKcal)
        self.frmLeftContentKcal.setObjectName(u"frmLeftContentKcal")
        self.frmLeftContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentKcal.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frmLeftContentKcal)

        self.frmRightContentKcal = QFrame(self.frmContentKcal)
        self.frmRightContentKcal.setObjectName(u"frmRightContentKcal")
        self.frmRightContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentKcal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frmRightContentKcal)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.kcalChart = QFrame(self.frmRightContentKcal)
        self.kcalChart.setObjectName(u"kcalChart")
        self.kcalChart.setFrameShape(QFrame.StyledPanel)
        self.kcalChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.kcalChart)

        self.frmChartSelectionKcal = QFrame(self.frmRightContentKcal)
        self.frmChartSelectionKcal.setObjectName(u"frmChartSelectionKcal")
        self.frmChartSelectionKcal.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionKcal.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frmChartSelectionKcal)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, 0)
        self.frame_4 = QFrame(self.frmChartSelectionKcal)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(100, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_4)

        self.frmSelectionBtnKcal = QFrame(self.frmChartSelectionKcal)
        self.frmSelectionBtnKcal.setObjectName(u"frmSelectionBtnKcal")
        self.frmSelectionBtnKcal.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnKcal.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnKcal.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frmSelectionBtnKcal)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lbSelectionKcal = QLabel(self.frmSelectionBtnKcal)
        self.lbSelectionKcal.setObjectName(u"lbSelectionKcal")
        self.lbSelectionKcal.setFont(font)

        self.horizontalLayout_22.addWidget(self.lbSelectionKcal)

        self.cbKcal = QComboBox(self.frmSelectionBtnKcal)
        self.cbKcal.addItem("")
        self.cbKcal.addItem("")
        self.cbKcal.addItem("")
        self.cbKcal.addItem("")
        self.cbKcal.setObjectName(u"cbKcal")
        self.cbKcal.setMinimumSize(QSize(120, 0))
        self.cbKcal.setMaximumSize(QSize(120, 16777215))
        self.cbKcal.setFont(font)
        self.cbKcal.setStyleSheet(u"")
        self.cbKcal.setEditable(False)
        self.cbKcal.setMaxCount(2147483645)

        self.horizontalLayout_22.addWidget(self.cbKcal)


        self.horizontalLayout_17.addWidget(self.frmSelectionBtnKcal)

        self.frame_5 = QFrame(self.frmChartSelectionKcal)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_5)


        self.verticalLayout_16.addWidget(self.frmChartSelectionKcal)


        self.horizontalLayout_16.addWidget(self.frmRightContentKcal)


        self.verticalLayout_13.addWidget(self.frmContentKcal)

        self.pages.addWidget(self.pageStatKcal)
        self.pageStatSteps = QWidget()
        self.pageStatSteps.setObjectName(u"pageStatSteps")
        self.verticalLayout_15 = QVBoxLayout(self.pageStatSteps)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentSteps = QFrame(self.pageStatSteps)
        self.frmTopContentSteps.setObjectName(u"frmTopContentSteps")
        self.frmTopContentSteps.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frmTopContentSteps)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat2 = QFrame(self.frmTopContentSteps)
        self.frmTopLeftStat2.setObjectName(u"frmTopLeftStat2")
        self.frmTopLeftStat2.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frmTopLeftStat2)

        self.frmTopBtnSteps = QFrame(self.frmTopContentSteps)
        self.frmTopBtnSteps.setObjectName(u"frmTopBtnSteps")
        self.frmTopBtnSteps.setMinimumSize(QSize(500, 0))
        self.frmTopBtnSteps.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frmTopBtnSteps)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btnKcal2 = QPushButton(self.frmTopBtnSteps)
        self.btnKcal2.setObjectName(u"btnKcal2")
        sizePolicy4.setHeightForWidth(self.btnKcal2.sizePolicy().hasHeightForWidth())
        self.btnKcal2.setSizePolicy(sizePolicy4)
        self.btnKcal2.setFont(font)
        self.btnKcal2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnKcal2)

        self.btnSteps2 = QPushButton(self.frmTopBtnSteps)
        self.btnSteps2.setObjectName(u"btnSteps2")
        sizePolicy4.setHeightForWidth(self.btnSteps2.sizePolicy().hasHeightForWidth())
        self.btnSteps2.setSizePolicy(sizePolicy4)
        self.btnSteps2.setFont(font)
        self.btnSteps2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnSteps2)

        self.btnBP2 = QPushButton(self.frmTopBtnSteps)
        self.btnBP2.setObjectName(u"btnBP2")
        sizePolicy4.setHeightForWidth(self.btnBP2.sizePolicy().hasHeightForWidth())
        self.btnBP2.setSizePolicy(sizePolicy4)
        self.btnBP2.setFont(font)
        self.btnBP2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnBP2)


        self.horizontalLayout_20.addWidget(self.frmTopBtnSteps)

        self.frmTopRightStat2 = QFrame(self.frmTopContentSteps)
        self.frmTopRightStat2.setObjectName(u"frmTopRightStat2")
        self.frmTopRightStat2.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frmTopRightStat2)


        self.verticalLayout_15.addWidget(self.frmTopContentSteps)

        self.frmContentSteps = QFrame(self.pageStatSteps)
        self.frmContentSteps.setObjectName(u"frmContentSteps")
        self.frmContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmContentSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frmContentSteps)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentSteps = QFrame(self.frmContentSteps)
        self.frmLeftContentSteps.setObjectName(u"frmLeftContentSteps")
        self.frmLeftContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentSteps.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_26.addWidget(self.frmLeftContentSteps)

        self.frmRightContentSteps = QFrame(self.frmContentSteps)
        self.frmRightContentSteps.setObjectName(u"frmRightContentSteps")
        self.frmRightContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentSteps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frmRightContentSteps)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.chartSteps = QFrame(self.frmRightContentSteps)
        self.chartSteps.setObjectName(u"chartSteps")
        self.chartSteps.setFrameShape(QFrame.StyledPanel)
        self.chartSteps.setFrameShadow(QFrame.Raised)

        self.verticalLayout_18.addWidget(self.chartSteps)

        self.frmChartSelectionSteps = QFrame(self.frmRightContentSteps)
        self.frmChartSelectionSteps.setObjectName(u"frmChartSelectionSteps")
        self.frmChartSelectionSteps.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionSteps.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frmChartSelectionSteps)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 9, 0)
        self.frame_15 = QFrame(self.frmChartSelectionSteps)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(100, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_28.addWidget(self.frame_15)

        self.frmSelectionBtnSteps = QFrame(self.frmChartSelectionSteps)
        self.frmSelectionBtnSteps.setObjectName(u"frmSelectionBtnSteps")
        self.frmSelectionBtnSteps.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnSteps.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnSteps.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frmSelectionBtnSteps)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lbSelectionSteps = QLabel(self.frmSelectionBtnSteps)
        self.lbSelectionSteps.setObjectName(u"lbSelectionSteps")
        self.lbSelectionSteps.setFont(font)

        self.horizontalLayout_27.addWidget(self.lbSelectionSteps)

        self.cbSteps = QComboBox(self.frmSelectionBtnSteps)
        self.cbSteps.addItem("")
        self.cbSteps.addItem("")
        self.cbSteps.addItem("")
        self.cbSteps.addItem("")
        self.cbSteps.setObjectName(u"cbSteps")
        self.cbSteps.setMinimumSize(QSize(120, 0))
        self.cbSteps.setMaximumSize(QSize(120, 16777215))
        self.cbSteps.setFont(font)
        self.cbSteps.setStyleSheet(u"")
        self.cbSteps.setEditable(False)
        self.cbSteps.setMaxCount(2147483645)

        self.horizontalLayout_27.addWidget(self.cbSteps)


        self.horizontalLayout_28.addWidget(self.frmSelectionBtnSteps)

        self.frame_17 = QFrame(self.frmChartSelectionSteps)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(100, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_28.addWidget(self.frame_17)


        self.verticalLayout_18.addWidget(self.frmChartSelectionSteps)


        self.horizontalLayout_26.addWidget(self.frmRightContentSteps)


        self.verticalLayout_15.addWidget(self.frmContentSteps)

        self.pages.addWidget(self.pageStatSteps)
        self.pageStatBP = QWidget()
        self.pageStatBP.setObjectName(u"pageStatBP")
        self.verticalLayout_14 = QVBoxLayout(self.pageStatBP)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentBP = QFrame(self.pageStatBP)
        self.frmTopContentBP.setObjectName(u"frmTopContentBP")
        self.frmTopContentBP.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frmTopContentBP)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat3 = QFrame(self.frmTopContentBP)
        self.frmTopLeftStat3.setObjectName(u"frmTopLeftStat3")
        self.frmTopLeftStat3.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frmTopLeftStat3)

        self.frmTopBtnBP = QFrame(self.frmTopContentBP)
        self.frmTopBtnBP.setObjectName(u"frmTopBtnBP")
        self.frmTopBtnBP.setMinimumSize(QSize(500, 0))
        self.frmTopBtnBP.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frmTopBtnBP)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btnKcal3 = QPushButton(self.frmTopBtnBP)
        self.btnKcal3.setObjectName(u"btnKcal3")
        sizePolicy4.setHeightForWidth(self.btnKcal3.sizePolicy().hasHeightForWidth())
        self.btnKcal3.setSizePolicy(sizePolicy4)
        self.btnKcal3.setFont(font)
        self.btnKcal3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnKcal3)

        self.btnSteps3 = QPushButton(self.frmTopBtnBP)
        self.btnSteps3.setObjectName(u"btnSteps3")
        sizePolicy4.setHeightForWidth(self.btnSteps3.sizePolicy().hasHeightForWidth())
        self.btnSteps3.setSizePolicy(sizePolicy4)
        self.btnSteps3.setFont(font)
        self.btnSteps3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnSteps3)

        self.btnBP3 = QPushButton(self.frmTopBtnBP)
        self.btnBP3.setObjectName(u"btnBP3")
        sizePolicy4.setHeightForWidth(self.btnBP3.sizePolicy().hasHeightForWidth())
        self.btnBP3.setSizePolicy(sizePolicy4)
        self.btnBP3.setFont(font)
        self.btnBP3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnBP3)


        self.horizontalLayout_18.addWidget(self.frmTopBtnBP)

        self.frmTopRightStat3 = QFrame(self.frmTopContentBP)
        self.frmTopRightStat3.setObjectName(u"frmTopRightStat3")
        self.frmTopRightStat3.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frmTopRightStat3)


        self.verticalLayout_14.addWidget(self.frmTopContentBP)

        self.frmContentBP = QFrame(self.pageStatBP)
        self.frmContentBP.setObjectName(u"frmContentBP")
        self.frmContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmContentBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frmContentBP)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentBP = QFrame(self.frmContentBP)
        self.frmLeftContentBP.setObjectName(u"frmLeftContentBP")
        self.frmLeftContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentBP.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frmLeftContentBP)

        self.frmRightContentBP = QFrame(self.frmContentBP)
        self.frmRightContentBP.setObjectName(u"frmRightContentBP")
        self.frmRightContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentBP.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frmRightContentBP)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.bpChart = QFrame(self.frmRightContentBP)
        self.bpChart.setObjectName(u"bpChart")
        self.bpChart.setFrameShape(QFrame.StyledPanel)
        self.bpChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.bpChart)

        self.frmChartSelectionBP = QFrame(self.frmRightContentBP)
        self.frmChartSelectionBP.setObjectName(u"frmChartSelectionBP")
        self.frmChartSelectionBP.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionBP.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frmChartSelectionBP)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 9, 0)
        self.frame_22 = QFrame(self.frmChartSelectionBP)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(100, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_22)

        self.frmSelectionBtnBP = QFrame(self.frmChartSelectionBP)
        self.frmSelectionBtnBP.setObjectName(u"frmSelectionBtnBP")
        self.frmSelectionBtnBP.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnBP.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnBP.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frmSelectionBtnBP)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lbSelectionBP = QLabel(self.frmSelectionBtnBP)
        self.lbSelectionBP.setObjectName(u"lbSelectionBP")
        self.lbSelectionBP.setFont(font)

        self.horizontalLayout_30.addWidget(self.lbSelectionBP)

        self.cbBP = QComboBox(self.frmSelectionBtnBP)
        self.cbBP.addItem("")
        self.cbBP.addItem("")
        self.cbBP.addItem("")
        self.cbBP.addItem("")
        self.cbBP.setObjectName(u"cbBP")
        self.cbBP.setMinimumSize(QSize(120, 0))
        self.cbBP.setMaximumSize(QSize(120, 16777215))
        self.cbBP.setFont(font)
        self.cbBP.setStyleSheet(u"")
        self.cbBP.setEditable(False)
        self.cbBP.setMaxCount(2147483645)

        self.horizontalLayout_30.addWidget(self.cbBP)


        self.horizontalLayout_31.addWidget(self.frmSelectionBtnBP)

        self.frame_23 = QFrame(self.frmChartSelectionBP)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(100, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_23)


        self.verticalLayout_19.addWidget(self.frmChartSelectionBP)


        self.horizontalLayout_29.addWidget(self.frmRightContentBP)


        self.verticalLayout_14.addWidget(self.frmContentBP)

        self.pages.addWidget(self.pageStatBP)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.pages.addWidget(self.pageSettings)
        self.pageAdmin = QWidget()
        self.pageAdmin.setObjectName(u"pageAdmin")
        self.horizontalLayout_13 = QHBoxLayout(self.pageAdmin)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frmContentAdmin = QFrame(self.pageAdmin)
        self.frmContentAdmin.setObjectName(u"frmContentAdmin")
        self.frmContentAdmin.setFrameShape(QFrame.StyledPanel)
        self.frmContentAdmin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frmContentAdmin)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frmSearchbar = QFrame(self.frmContentAdmin)
        self.frmSearchbar.setObjectName(u"frmSearchbar")
        self.frmSearchbar.setMinimumSize(QSize(0, 50))
        self.frmSearchbar.setMaximumSize(QSize(16777215, 50))
        self.frmSearchbar.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmSearchbar.setFrameShape(QFrame.StyledPanel)
        self.frmSearchbar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frmSearchbar)

        self.frmUserTbl = QFrame(self.frmContentAdmin)
        self.frmUserTbl.setObjectName(u"frmUserTbl")
        self.frmUserTbl.setMaximumSize(QSize(16777215, 16777215))
        self.frmUserTbl.setFrameShape(QFrame.StyledPanel)
        self.frmUserTbl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frmUserTbl)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tblUser = QTableWidget(self.frmUserTbl)
        self.tblUser.setObjectName(u"tblUser")
        font2 = QFont()
        font2.setPointSize(12)
        self.tblUser.setFont(font2)
        self.tblUser.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")

        self.verticalLayout_12.addWidget(self.tblUser)


        self.verticalLayout_10.addWidget(self.frmUserTbl)


        self.horizontalLayout_13.addWidget(self.frmContentAdmin)

        self.frmContorlAdmin = QFrame(self.pageAdmin)
        self.frmContorlAdmin.setObjectName(u"frmContorlAdmin")
        self.frmContorlAdmin.setMinimumSize(QSize(250, 0))
        self.frmContorlAdmin.setMaximumSize(QSize(250, 16777215))
        self.frmContorlAdmin.setFrameShape(QFrame.StyledPanel)
        self.frmContorlAdmin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frmContorlAdmin)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.bufferTop = QFrame(self.frmContorlAdmin)
        self.bufferTop.setObjectName(u"bufferTop")
        self.bufferTop.setFrameShape(QFrame.StyledPanel)
        self.bufferTop.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.bufferTop)

        self.frmControlBtns = QFrame(self.frmContorlAdmin)
        self.frmControlBtns.setObjectName(u"frmControlBtns")
        self.frmControlBtns.setFrameShape(QFrame.StyledPanel)
        self.frmControlBtns.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frmControlBtns)

        self.bufferBottom = QFrame(self.frmContorlAdmin)
        self.bufferBottom.setObjectName(u"bufferBottom")
        self.bufferBottom.setFrameShape(QFrame.StyledPanel)
        self.bufferBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.bufferBottom)


        self.horizontalLayout_13.addWidget(self.frmContorlAdmin)

        self.pages.addWidget(self.pageAdmin)

        self.verticalLayout_4.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.mainWidget)

        WndMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(WndMain)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"MainWindow", None))
        self.btnToggle.setText("")
        self.lbName.setText(QCoreApplication.translate("WndMain", u" Max Mustermann", None))
        self.lbDate.setText(QCoreApplication.translate("WndMain", u"09.06.2022", None))
        self.lbPageDescription.setText(QCoreApplication.translate("WndMain", u"Home", None))
        self.btnHome.setText(QCoreApplication.translate("WndMain", u"Home", None))
        self.btnFood.setText(QCoreApplication.translate("WndMain", u"Food", None))
        self.btnStatistic.setText(QCoreApplication.translate("WndMain", u"Statistics", None))
        self.btnSettings.setText(QCoreApplication.translate("WndMain", u"Settings", None))
        self.btnLogout.setText(QCoreApplication.translate("WndMain", u"Logout", None))
        self.lbWeight.setText(QCoreApplication.translate("WndMain", u"Weight:", None))
        self.lbSteps.setText(QCoreApplication.translate("WndMain", u"Steps:", None))
        self.lbBP.setText(QCoreApplication.translate("WndMain", u"Blood Pressure:", None))
        self.leBPLow.setPlaceholderText(QCoreApplication.translate("WndMain", u"Low", None))
        self.leBPHigh.setPlaceholderText(QCoreApplication.translate("WndMain", u"High", None))
        self.btnSubmit.setText(QCoreApplication.translate("WndMain", u"Submit", None))
        self.btnKcal1.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps1.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP1.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.lbSelectionKcal.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbKcal.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbKcal.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbKcal.setItemText(2, QCoreApplication.translate("WndMain", u"3 month", None))
        self.cbKcal.setItemText(3, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbKcal.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
        self.btnKcal2.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps2.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP2.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.lbSelectionSteps.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbSteps.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbSteps.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbSteps.setItemText(2, QCoreApplication.translate("WndMain", u"3 month", None))
        self.cbSteps.setItemText(3, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbSteps.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
        self.btnKcal3.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps3.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP3.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.lbSelectionBP.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbBP.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbBP.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbBP.setItemText(2, QCoreApplication.translate("WndMain", u"3 month", None))
        self.cbBP.setItemText(3, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbBP.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
    # retranslateUi

