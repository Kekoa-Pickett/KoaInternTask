# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'koaFirstProject.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from source.tasks import TaskBox
#from gen.taskTrackerUI_ui import *
#from gen.koaFirstProjectV1_ui import *
from gen.taskTrackerQT_ui import *

from PySide6.QtWidgets import (QMainWindow)

import math

class MainWindow(QMainWindow):

    NUM_OF_COL = 4

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._task_index = 0

        self.connections()


    def connections(self):
        # self.ui.taskGrid.setColumnStretch(2,0)
        self.ui.compTaskClr.clicked.connect(lambda: self.ui.compTaskList.clear())
        self.ui.newTaskButton.clicked.connect(lambda: self.newTask())

    def newTask(self):
        config = {
            "object name" : f"task {self._task_index}",
            "gridlayout name" : f"gridlayout name {self._task_index}",
            "col position" : math.floor(self._task_index/self.NUM_OF_COL),
            "row position" : self._task_index % self.NUM_OF_COL,
        }
        newTask = TaskBox(self.ui, config)
        self._task_index += 1