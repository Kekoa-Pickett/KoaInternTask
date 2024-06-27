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

''' This class creates the task group box that will be added to the task group'''
class TaskBox(QGroupBox):
    def __init__(self, parent = None, compTaskList = None):
        super().__init__(parent)
        self.setTitle("task")

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicyDate = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth()) #size setting
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(262, 125))
        self.setMaximumSize(QSize(262, 125))
        self.setAutoFillBackground(True)
        self.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.dateTime = QDateTimeEdit(self)                                         # date feature
        self.dateTime.setObjectName(u"dateTime")
        self.dateTime.setGeometry(QRect(100, 10, 141, 22))
        sizePolicyDate.setHeightForWidth(self.dateTime.sizePolicy().hasHeightForWidth())
        self.dateTime.setSizePolicy(sizePolicyDate)
        self.dateTime.setCalendarPopup(True)
        self.dateTime.setTimeSpec(Qt.LocalTime)

        self.taskText = QTextEdit(self)                                             # textbox setting
        self.taskText.setObjectName(u"taskText")
        self.taskText.setGeometry(QRect(10, 40, 231, 51))
        self.taskText.setPlaceholderText("Describe task ...")

        self.deleteButton = QPushButton(u"Delete", self)                            # delete button settings
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(180, 100, 61, 20))
        self.deleteButton.clicked.connect(self.deleteLater)

        self.compCheck = QCheckBox("Completed", self)                              # Completed settings
        self.compCheck.setObjectName(u"compCheck1")
        self.compCheck.setGeometry(QRect(10, 100, 91, 20))
        self.compCheck.stateChanged.connect(self.completedTask(compTaskList, self.taskText.toPlainText()))

    def completedTask(self, parent = None, text = None):
            parent.addItem(QListWidgetItem(text))               # Doesn't work, just adds automatically because stateChanged doesn't work properly
            self.deleteLater

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 675)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.verticalLayoutWidget = QWidget(self.centralwidget)             #Completed Tasks List
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
        self.compTaskLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.compTaskBox.addWidget(self.compTaskLabel)

        self.compTaskList = QListWidget(self.verticalLayoutWidget)
        self.compTaskList.setObjectName(u"compTaskList")
        self.compTaskList.setSortingEnabled(False)

        self.compTaskBox.addWidget(self.compTaskList)
        

        self.compTaskClr = QPushButton(self.verticalLayoutWidget)
        self.compTaskClr.setObjectName(u"compTaskClr")
        font2 = QFont()
        font2.setPointSize(10)
        self.compTaskClr.setFont(font2)

        self.compTaskBox.addWidget(self.compTaskClr)
        
        self.gridLayoutWidget = QWidget(self.centralwidget)                 #All tasks list
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 802, 521))
        self.taskGrid = QGridLayout(self.gridLayoutWidget)
        self.taskGrid.setColumnStretch(2,0)
        self.taskGrid.setObjectName(u"taskGrid")
        self.taskGrid.setSizeConstraint(QLayout.SetFixedSize)
        self.taskGrid.setHorizontalSpacing(7)
        self.taskGrid.setContentsMargins(0, 0, 0, 0)
        self.NewTaskButton = QPushButton(u"NewTaskButton", self.centralwidget)
        self.NewTaskButton.setGeometry(QRect(100, 30, 161, 41))
        self.NewTaskButton.setFont(font)
        self.NewTaskButton.setStyleSheet(u"background-color: rgb(80, 220, 255);")
        # Size needed for the task elements
        #sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        #sizePolicyDate = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        self.NewTaskButton.clicked.connect(lambda: self.taskGrid.addWidget(TaskBox(
                                           self.centralwidget, self.compTaskList)))
        print(self.centralwidget)
        

        self.tasksLeftGroup = QGroupBox(self.centralwidget)
        self.tasksLeftGroup.setObjectName(u"tasksLeftGroup")
        self.tasksLeftGroup.setGeometry(QRect(480, 10, 311, 80))
        self.dropdownList = QComboBox(self.tasksLeftGroup)
        self.dropdownList.addItem(u"Total tasks todo:")
        self.dropdownList.addItem(u"Tasks due today :")
        self.dropdownList.addItem(u"Completed tasks :")
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
        self.compTaskLabel.setText(QCoreApplication.translate("MainWindow", u"Completed Tasks", None))
        self.compTaskClr.setText(QCoreApplication.translate("MainWindow", u"Clear Completed Tasks", None))
        self.tasksLeftGroup.setTitle("")

        self.dropdownList.setCurrentText(QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))
    # retranslateUi

    def completedTask(self, parent = None, text = None):
        #self.compItem = QListWidgetItem("Task", self)
        self.deleteLater

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