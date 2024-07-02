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
        self.ui.compTaskClr.clicked.connect(lambda: self.ui.compTaskList.clear())
        self.ui.newTaskButton.clicked.connect(lambda: self.ui.taskGrid.addWidget(
                                                TaskBox(self.ui.centralwidget)))
    
    ''' Moves task over to completed section
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