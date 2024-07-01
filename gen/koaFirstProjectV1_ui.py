# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'koaFirstProjectV1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 675)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.newTaskButton = QPushButton(self.centralwidget)
        self.newTaskButton.setObjectName(u"newTaskButton")
        self.newTaskButton.setGeometry(QRect(100, 30, 161, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.newTaskButton.setFont(font)
        self.newTaskButton.setStyleSheet(u"background-color: rgb(80, 220, 255);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 802, 521))
        self.taskGrid = QGridLayout(self.gridLayoutWidget)
        self.taskGrid.setObjectName(u"taskGrid")
        self.taskGrid.setSizeConstraint(QLayout.SetMinimumSize)
        self.taskGrid.setHorizontalSpacing(7)
        self.taskGrid.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(830, 10, 258, 601))
        self.compTaskBox = QVBoxLayout(self.verticalLayoutWidget)
        self.compTaskBox.setObjectName(u"compTaskBox")
        self.compTaskBox.setContentsMargins(0, 0, 0, 0)
        self.compTaskLabel = QLabel(self.verticalLayoutWidget)
        self.compTaskLabel.setObjectName(u"compTaskLabel")
        font1 = QFont()
        font1.setFamilies([u"Georgia"])
        font1.setPointSize(12)
        self.compTaskLabel.setFont(font1)
        self.compTaskLabel.setFrameShape(QFrame.NoFrame)
        self.compTaskLabel.setTextFormat(Qt.PlainText)
        self.compTaskLabel.setScaledContents(False)
        self.compTaskLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.compTaskLabel.setMargin(0)

        self.compTaskBox.addWidget(self.compTaskLabel)

        self.compTaskList = QListWidget(self.verticalLayoutWidget)
        self.compTaskList.setObjectName(u"compTaskList")
        font2 = QFont()
        font2.setFamilies([u"Georgia"])
        font2.setPointSize(12)
        font2.setKerning(True)
        self.compTaskList.setFont(font2)
        self.compTaskList.setAlternatingRowColors(False)
        self.compTaskList.setSortingEnabled(False)

        self.compTaskBox.addWidget(self.compTaskList)

        self.compTaskClr = QPushButton(self.verticalLayoutWidget)
        self.compTaskClr.setObjectName(u"compTaskClr")
        font3 = QFont()
        font3.setFamilies([u"Georgia"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setUnderline(False)
        self.compTaskClr.setFont(font3)

        self.compTaskBox.addWidget(self.compTaskClr)

        self.tasksLeftGroup = QGroupBox(self.centralwidget)
        self.tasksLeftGroup.setObjectName(u"tasksLeftGroup")
        self.tasksLeftGroup.setGeometry(QRect(480, 10, 311, 80))
        self.dropdownList = QComboBox(self.tasksLeftGroup)
        self.dropdownList.addItem("")
        self.dropdownList.setObjectName(u"dropdownList")
        self.dropdownList.setGeometry(QRect(10, 20, 181, 41))
        font4 = QFont()
        font4.setPointSize(10)
        self.dropdownList.setFont(font4)
        self.numDisplay = QSpinBox(self.tasksLeftGroup)
        self.numDisplay.setObjectName(u"numDisplay")
        self.numDisplay.setGeometry(QRect(190, 20, 101, 41))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.numDisplay.setFont(font5)
        self.numDisplay.setStyleSheet(u"alternate-background-color: rgb(200,100,100);\n"
"background-color: rgb(100,200,100);\n"
"\n"
"")
        self.numDisplay.setAlignment(Qt.AlignCenter)
        self.numDisplay.setReadOnly(True)
        self.numDisplay.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.numDisplay.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1104, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.newTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add new task", None))
        self.compTaskLabel.setText(QCoreApplication.translate("MainWindow", u"Completed Tasks", None))
        self.compTaskClr.setText(QCoreApplication.translate("MainWindow", u"Clear Completed Tasks", None))
        self.tasksLeftGroup.setTitle("")
        self.dropdownList.setItemText(0, QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))

        self.dropdownList.setCurrentText(QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))
    # retranslateUi

