# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 420)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.logText = QPlainTextEdit(self.centralwidget)
        self.logText.setObjectName(u"logText")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.logText.setFont(font)

        self.gridLayout_2.addWidget(self.logText, 1, 0, 1, 1)

        self.sensingText = QPlainTextEdit(self.centralwidget)
        self.sensingText.setObjectName(u"sensingText")
        self.sensingText.setFont(font)

        self.gridLayout_2.addWidget(self.sensingText, 1, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setObjectName(u"goButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy)
        self.goButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.goButton, 0, 1, 1, 1)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.stopButton, 1, 5, 1, 1)

        self.leftButton = QPushButton(self.centralwidget)
        self.leftButton.setObjectName(u"leftButton")
        sizePolicy.setHeightForWidth(self.leftButton.sizePolicy().hasHeightForWidth())
        self.leftButton.setSizePolicy(sizePolicy)
        self.leftButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.backBbutton = QPushButton(self.centralwidget)
        self.backBbutton.setObjectName(u"backBbutton")
        sizePolicy.setHeightForWidth(self.backBbutton.sizePolicy().hasHeightForWidth())
        self.backBbutton.setSizePolicy(sizePolicy)
        self.backBbutton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.backBbutton, 2, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 0, 4, 3, 1)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.startButton, 0, 5, 1, 1)

        self.rightButton = QPushButton(self.centralwidget)
        self.rightButton.setObjectName(u"rightButton")
        sizePolicy.setHeightForWidth(self.rightButton.sizePolicy().hasHeightForWidth())
        self.rightButton.setSizePolicy(sizePolicy)
        self.rightButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 0, 3, 3, 1)

        self.midButton = QPushButton(self.centralwidget)
        self.midButton.setObjectName(u"midButton")
        sizePolicy.setHeightForWidth(self.midButton.sizePolicy().hasHeightForWidth())
        self.midButton.setSizePolicy(sizePolicy)
        self.midButton.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.midButton, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.start)
        self.goButton.clicked.connect(MainWindow.go)
        self.leftButton.clicked.connect(MainWindow.left)
        self.rightButton.clicked.connect(MainWindow.right)
        self.midButton.clicked.connect(MainWindow.mid)
        self.backBbutton.clicked.connect(MainWindow.back)
        self.stopButton.clicked.connect(MainWindow.stop)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"command Table", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"sensing Table", None))
        self.goButton.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.leftButton.setText(QCoreApplication.translate("MainWindow", u"LEFT", None))
        self.backBbutton.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.rightButton.setText(QCoreApplication.translate("MainWindow", u"RIGHT", None))
        self.midButton.setText(QCoreApplication.translate("MainWindow", u"MID", None))
    # retranslateUi

