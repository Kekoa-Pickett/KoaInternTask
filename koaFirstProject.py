# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'koaFirstProject.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QFrame, QGridLayout, QGroupBox,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 675)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.NewTaskButton = QPushButton(self.centralwidget)
        self.NewTaskButton.setObjectName(u"NewTaskButton")
        self.NewTaskButton.setGeometry(QRect(100, 30, 161, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.NewTaskButton.setFont(font)
        self.NewTaskButton.setStyleSheet(u"background-color: rgb(80, 220, 255);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 802, 521))
        self.taskGrid = QGridLayout(self.gridLayoutWidget)
        self.taskGrid.setObjectName(u"taskGrid")
        self.taskGrid.setSizeConstraint(QLayout.SetFixedSize)
        self.taskGrid.setHorizontalSpacing(7)
        self.taskGrid.setContentsMargins(0, 0, 0, 0)
        self.task2 = QGroupBox(self.gridLayoutWidget)
        self.task2.setObjectName(u"task2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.task2.sizePolicy().hasHeightForWidth())
        self.task2.setSizePolicy(sizePolicy)
        self.task2.setMinimumSize(QSize(262, 125))
        self.task2.setMaximumSize(QSize(262, 125))
        self.task2.setAutoFillBackground(True)
        self.dateTime2 = QDateTimeEdit(self.task2)
        self.dateTime2.setObjectName(u"dateTime2")
        self.dateTime2.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dateTime2.sizePolicy().hasHeightForWidth())
        self.dateTime2.setSizePolicy(sizePolicy1)
        #self.dateTime2.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTime2.setCalendarPopup(True)
        self.taskText2 = QTextEdit(self.task2)
        self.taskText2.setObjectName(u"taskText2")
        self.taskText2.setGeometry(QRect(10, 40, 231, 51))
        self.deleteButton2 = QPushButton(self.task2)
        self.deleteButton2.setObjectName(u"deleteButton2")
        self.deleteButton2.setGeometry(QRect(180, 100, 61, 20))
        self.compCheck2 = QCheckBox(self.task2)
        self.compCheck2.setObjectName(u"compCheck2")
        self.compCheck2.setGeometry(QRect(20, 100, 91, 20))

        self.taskGrid.addWidget(self.task2, 0, 1, 1, 1)

        self.task3 = QGroupBox(self.gridLayoutWidget)
        self.task3.setObjectName(u"task3")
        sizePolicy.setHeightForWidth(self.task3.sizePolicy().hasHeightForWidth())
        self.task3.setSizePolicy(sizePolicy)
        self.task3.setMinimumSize(QSize(262, 125))
        self.task3.setMaximumSize(QSize(262, 125))
        self.task3.setAutoFillBackground(True)
        self.task3.setCheckable(True)
        self.task3.setChecked(True)
        self.dateTime3 = QDateTimeEdit(self.task3)
        self.dateTime3.setObjectName(u"dateTime3")
        self.dateTime3.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1.setHeightForWidth(self.dateTime3.sizePolicy().hasHeightForWidth())
        self.dateTime3.setSizePolicy(sizePolicy1)
        #self.dateTime3.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTime3.setCalendarPopup(True)
        self.taskText3 = QTextEdit(self.task3)
        self.taskText3.setObjectName(u"taskText3")
        self.taskText3.setGeometry(QRect(10, 40, 231, 51))
        self.deleteButton3 = QPushButton(self.task3)
        self.deleteButton3.setObjectName(u"deleteButton3")
        self.deleteButton3.setGeometry(QRect(180, 100, 61, 20))
        self.compCheck3 = QCheckBox(self.task3)
        self.compCheck3.setObjectName(u"compCheck3")
        self.compCheck3.setGeometry(QRect(20, 100, 91, 20))

        self.taskGrid.addWidget(self.task3, 0, 2, 1, 1)

        self.task4 = QGroupBox(self.gridLayoutWidget)
        self.task4.setObjectName(u"task4")
        sizePolicy.setHeightForWidth(self.task4.sizePolicy().hasHeightForWidth())
        self.task4.setSizePolicy(sizePolicy)
        self.task4.setMinimumSize(QSize(262, 125))
        self.task4.setMaximumSize(QSize(262, 125))
        self.task4.setAutoFillBackground(True)
        self.dateTime4 = QDateTimeEdit(self.task4)
        self.dateTime4.setObjectName(u"dateTime4")
        self.dateTime4.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1.setHeightForWidth(self.dateTime4.sizePolicy().hasHeightForWidth())
        self.dateTime4.setSizePolicy(sizePolicy1)
        #self.dateTime4.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTime4.setCalendarPopup(True)
        self.taskText4 = QTextEdit(self.task4)
        self.taskText4.setObjectName(u"taskText4")
        self.taskText4.setGeometry(QRect(10, 40, 231, 51))
        self.deleteButton4 = QPushButton(self.task4)
        self.deleteButton4.setObjectName(u"deleteButton4")
        self.deleteButton4.setGeometry(QRect(180, 100, 61, 20))
        self.compCheck4 = QCheckBox(self.task4)
        self.compCheck4.setObjectName(u"compCheck4")
        self.compCheck4.setGeometry(QRect(20, 100, 91, 20))

        self.taskGrid.addWidget(self.task4, 1, 0, 1, 1)

        self.task1 = QGroupBox(self.gridLayoutWidget)
        self.task1.setObjectName(u"task1")
        sizePolicy.setHeightForWidth(self.task1.sizePolicy().hasHeightForWidth())
        self.task1.setSizePolicy(sizePolicy)
        self.task1.setMinimumSize(QSize(262, 125))
        self.task1.setMaximumSize(QSize(262, 125))
        self.task1.setAutoFillBackground(True)
        self.task1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.dateTime1 = QDateTimeEdit(self.task1)
        self.dateTime1.setObjectName(u"dateTime1")
        self.dateTime1.setGeometry(QRect(100, 10, 141, 22))
        sizePolicy1.setHeightForWidth(self.dateTime1.sizePolicy().hasHeightForWidth())
        self.dateTime1.setSizePolicy(sizePolicy1)
        #self.dateTime1.setStyleSheet(u"text-color: rgb(170, 170, 255)")
        self.dateTime1.setCalendarPopup(True)
        self.dateTime1.setTimeSpec(Qt.LocalTime)
        self.taskText1 = QTextEdit(self.task1)
        self.taskText1.setObjectName(u"taskText1")
        self.taskText1.setGeometry(QRect(10, 40, 231, 51))
        self.deleteButton1 = QPushButton(self.task1)
        self.deleteButton1.setObjectName(u"deleteButton1")
        self.deleteButton1.setGeometry(QRect(180, 100, 61, 20))
        self.compCheck1 = QCheckBox(self.task1)
        self.compCheck1.setObjectName(u"compCheck1")
        self.compCheck1.setGeometry(QRect(10, 100, 91, 20))

        self.taskGrid.addWidget(self.task1, 0, 0, 1, 1)

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
        self.compTaskList.setSortingEnabled(False)

        self.compTaskBox.addWidget(self.compTaskList)

        self.compTaskClr = QPushButton(self.verticalLayoutWidget)
        self.compTaskClr.setObjectName(u"compTaskClr")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setUnderline(False)
        self.compTaskClr.setFont(font2)

        self.compTaskBox.addWidget(self.compTaskClr)

        self.tasksLeftGroup = QGroupBox(self.centralwidget)
        self.tasksLeftGroup.setObjectName(u"tasksLeftGroup")
        self.tasksLeftGroup.setGeometry(QRect(480, 10, 311, 80))
        self.dropdownList = QComboBox(self.tasksLeftGroup)
        self.dropdownList.addItem("")
        self.dropdownList.addItem("")
        self.dropdownList.addItem("")
        self.dropdownList.setObjectName(u"dropdownList")
        self.dropdownList.setGeometry(QRect(10, 20, 181, 41))
        font3 = QFont()
        font3.setPointSize(9)
        self.dropdownList.setFont(font3)
        self.numDisplay = QSpinBox(self.tasksLeftGroup)
        self.numDisplay.setObjectName(u"numDisplay")
        self.numDisplay.setGeometry(QRect(190, 20, 101, 41))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.numDisplay.setFont(font4)
        self.numDisplay.setStyleSheet(u"alternate-background-color: rgb(200,100,100);\n"
"background-color: rgb(100,200,100);\n"
"\n"
"")
        self.numDisplay.setAlignment(Qt.AlignCenter)
        self.numDisplay.setReadOnly(True)
        self.numDisplay.setButtonSymbols(QAbstractSpinBox.NoButtons)
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
        self.NewTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add new task", None))
        self.task2.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.deleteButton2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compCheck2.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.task3.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.deleteButton3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compCheck3.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.task4.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.deleteButton4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compCheck4.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.task1.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Describe task...", None))
        self.deleteButton1.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compCheck1.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.compTaskLabel.setText(QCoreApplication.translate("MainWindow", u"Completed Tasks", None))
        self.compTaskClr.setText(QCoreApplication.translate("MainWindow", u"Clear Completed Tasks", None))
        self.tasksLeftGroup.setTitle("")
        self.dropdownList.setItemText(0, QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))
        self.dropdownList.setItemText(1, QCoreApplication.translate("MainWindow", u"Tasks due today :", None))
        self.dropdownList.setItemText(2, QCoreApplication.translate("MainWindow", u"Completed tasks :", None))

        self.dropdownList.setCurrentText(QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))
    # retranslateUi

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from koaFirstProject import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())