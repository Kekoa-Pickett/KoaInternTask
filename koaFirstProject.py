# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'koaFirstProject.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from source.tasks import TaskBox
from gen.koaFirstProjectV1_ui import *
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

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connections()


    def connections(self):
        self.ui.taskGrid.setColumnStretch(2,0)
        # taskGrid = centralWidget.findChild(QWidget, "gridLayoutWidget")
        # vertLayout = centralWidget.findChild(QWidget, "verticalLayoutWidget")
        # compTaskClr = vertLayout.findChild(QPushButton,"compTaskClr")
        
        # compTaskClr.clicked.connect(lambda: centralWidget.compTaskList.clear())
        # print(vertLayout.children())
        # newTaskButton = centralWidget.findChild(QPushButton,"newTaskButton")
        # taskGrid = centralWidget.findChild(QGridLayout, "taskGrid")
        # newTaskButton.clicked.connect(lambda: taskGrid.addWidget(TaskBox(
        #                                    centralWidget)))
        self.ui.compTaskClr.clicked.connect(lambda: self.ui.compTaskList.clear())
        self.ui.newTaskButton.clicked.connect(lambda: self.ui.taskGrid.addWidget(
                                                TaskBox(self.ui.centralwidget)))
    
    ''' Moves task over to completed section'''
    def completedTask(self, centralWidget = None, text = None):
        #if (self.compCheck.isChecked()):                               # Allow user to still have access to it
            vertLayout = centralWidget.findChild(QWidget, name="verticalLayoutWidget")
            compTaskList = vertLayout.findChild(QListWidget, name="compTaskList")
            compTaskList.addItem(QListWidgetItem(text))
            tasksLeftGroup = centralWidget.findChild(QGroupBox, name="tasksLeftGroup")                          
            self.deleteLater()                                          # Remove task altogether
            self.updateTaskLeftGroup(tasksLeftGroup, centralWidget)
    
    def updateTaskLeftGroup(self, tasksLeftGroup = None, centralWidget = None):
        dropdown = tasksLeftGroup.findChild(QComboBox,"dropdownList")
        dropdownNum = tasksLeftGroup.findChild(QSpinBox, "numDisplay")
        dropdownTxt = dropdown.currentText()
        if dropdownTxt == "Total tasks todo:":
            gridLayout = centralWidget.findChild(QWidget,"gridLayoutWidget")
            dropdownNum.setValue(gridLayout.children().__len__() - 2)
        elif dropdownTxt == "Tasks due today:":
            print("Text is not accounted for yet")
        else:
            print("Text is not accounted for yet")
'''
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
        
        self.verticalLayoutWidget = QWidget(self.centralwidget)             #Completed Area
        self.verticalLayoutWidget.setObjectName(u"compTaskBox")
        self.verticalLayoutWidget.setGeometry(QRect(830, 10, 258, 601))
        self.compTaskBox = QVBoxLayout(self.verticalLayoutWidget)
        self.compTaskBox.setObjectName(u"compTaskBox")
        self.compTaskBox.setContentsMargins(0, 0, 0, 0)
        self.compTaskLabel = QLabel(self.verticalLayoutWidget)
        self.compTaskLabel.setObjectName(u"compTaskLabel")
        
        font1 = QFont()                                                     # Completed Task Label
        font1.setFamilies([u"Georgia"])
        font1.setPointSize(12)
        self.compTaskLabel.setFont(font1)
        self.compTaskLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.compTaskBox.addWidget(self.compTaskLabel)

        self.compTaskList = QListWidget(self.verticalLayoutWidget)          # Completed Task List
        self.compTaskList.setObjectName(u"compTaskList")
        self.compTaskList.setSortingEnabled(False)
        self.compTaskBox.addWidget(self.compTaskList)
        #self.compTaskBox.children().__len__

        self.compTaskClr = QPushButton(self.verticalLayoutWidget)           # Completed Clear Button
        self.compTaskClr.setObjectName(u"compTaskClr")
        font2 = QFont()
        font2.setPointSize(10)
        self.compTaskClr.setFont(font2)
        self.compTaskClr.clicked.connect(lambda: self.compTaskList.clear())
        self.compTaskBox.addWidget(self.compTaskClr)
        
        self.gridLayoutWidget = QWidget(self.centralwidget)                 # All tasks list
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 802, 521))
        
        self.taskGrid = QGridLayout(self.gridLayoutWidget)                  # Task area layout
        self.taskGrid.setColumnStretch(2,0)
        self.taskGrid.setObjectName(u"taskGrid")
        self.taskGrid.setSizeConstraint(QLayout.SetFixedSize)
        self.taskGrid.setHorizontalSpacing(7)
        self.taskGrid.setContentsMargins(0, 0, 0, 0)

        self.NewTaskButton = QPushButton(u"NewTaskButton", self.centralwidget)  # Add Task Button
        self.NewTaskButton.setGeometry(QRect(100, 30, 161, 41))
        self.NewTaskButton.setFont(font)
        self.NewTaskButton.setStyleSheet(u"background-color: rgb(80, 220, 255);")
        self.NewTaskButton.clicked.connect(lambda: self.taskGrid.addWidget(TaskBox(
                                           self.centralwidget, self.compTaskList)))
        
        self.tasksLeftGroup = QGroupBox(self.centralwidget)                 # Dropdown Area
        self.tasksLeftGroup.setObjectName(u"tasksLeftGroup")
        self.tasksLeftGroup.setGeometry(QRect(480, 10, 311, 80))

        self.dropdownList = QComboBox(self.tasksLeftGroup)                  # Dropdown list
        self.dropdownList.addItem(u"Total tasks todo:")
        self.dropdownList.addItem(u"Tasks due today :")
        self.dropdownList.addItem(u"Completed tasks :")
        self.dropdownList.setObjectName(u"dropdownList")
        self.dropdownList.setGeometry(QRect(10, 20, 181, 41))
        self.dropdownList.setFont(font2)
        #self.dropdownList.changeEvent

        self.numDisplay = QSpinBox(self.tasksLeftGroup)                     # Dropdown numbers(Spinbox)
        self.numDisplay.setObjectName(u"numDisplay")
        self.numDisplay.setGeometry(QRect(190, 20, 101, 41))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.numDisplay.setFont(font4)
        self.numDisplay.setStyleSheet(u"alternate-background-color: rgb(200,100,100);\n"
                                        "background-color: rgb(100,200,100);\n""\n""")
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
    # retranslateUi '''