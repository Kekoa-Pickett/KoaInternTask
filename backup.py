# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskTrackerQT.ui'
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
    QHBoxLayout, QLabel, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(925, 517)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tasksLeftGroup = QGroupBox(self.centralwidget)
        self.tasksLeftGroup.setObjectName(u"tasksLeftGroup")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasksLeftGroup.sizePolicy().hasHeightForWidth())
        self.tasksLeftGroup.setSizePolicy(sizePolicy)
        self.tasksLeftGroup.setMinimumSize(QSize(100, 39))
        self.tasksLeftGroup.setMaximumSize(QSize(370, 54))
        self.tasksLeftGroup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.horizontalLayout_3 = QHBoxLayout(self.tasksLeftGroup)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.newTaskButton = QPushButton(self.tasksLeftGroup)
        self.newTaskButton.setObjectName(u"newTaskButton")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.newTaskButton.setFont(font)
        self.newTaskButton.setStyleSheet(u"background-color: rgb(80, 220, 255);")

        self.horizontalLayout_3.addWidget(self.newTaskButton)

        self.dropdownList = QComboBox(self.tasksLeftGroup)
        self.dropdownList.addItem("")
        self.dropdownList.setObjectName(u"dropdownList")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dropdownList.sizePolicy().hasHeightForWidth())
        self.dropdownList.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(10)
        self.dropdownList.setFont(font1)
        self.dropdownList.setFrame(True)

        self.horizontalLayout_3.addWidget(self.dropdownList)

        self.numDisplay = QSpinBox(self.tasksLeftGroup)
        self.numDisplay.setObjectName(u"numDisplay")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.numDisplay.setFont(font2)
        self.numDisplay.setStyleSheet(u"alternate-background-color: rgb(200,100,100);\n"
"background-color: rgb(100,200,100);\n"
"\n"
"")
        self.numDisplay.setAlignment(Qt.AlignCenter)
        self.numDisplay.setReadOnly(True)
        self.numDisplay.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.numDisplay.setValue(0)

        self.horizontalLayout_3.addWidget(self.numDisplay)


        self.verticalLayout.addWidget(self.tasksLeftGroup)

        self.taskGrid = QGridLayout()
        self.taskGrid.setObjectName(u"taskGrid")
        self.taskGrid.setSizeConstraint(QLayout.SetMinimumSize)
        self.taskGrid.setHorizontalSpacing(7)
        self.taskGrid.setContentsMargins(0, 0, -1, -1)
        self.taskWidget = QWidget(self.centralwidget)
        self.taskWidget.setObjectName(u"taskWidget")
        sizePolicy.setHeightForWidth(self.taskWidget.sizePolicy().hasHeightForWidth())
        self.taskWidget.setSizePolicy(sizePolicy)
        self.taskWidget.setMinimumSize(QSize(153, 82))
        self.gridLayout_taskWidget = QGridLayout(self.taskWidget)
        self.gridLayout_taskWidget.setObjectName(u"gridLayout_taskWidget")
        self.gridLayout_taskWidget.setVerticalSpacing(2)
        self.gridLayout_taskWidget.setContentsMargins(-1, 2, -1, 2)
        self.task_1 = QGroupBox(self.taskWidget)
        self.task_1.setObjectName(u"task_1")
        sizePolicy.setHeightForWidth(self.task_1.sizePolicy().hasHeightForWidth())
        self.task_1.setSizePolicy(sizePolicy)
        self.task_1.setMinimumSize(QSize(131, 60))
        self.task_1.setMaximumSize(QSize(262, 125))
        self.task_1.setAutoFillBackground(True)
        self.task_1.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_1 = QGridLayout(self.task_1)
        self.gridLayout_1.setObjectName(u"gridLayout_1")
        self.gridLayout_1.setContentsMargins(-1, 0, -1, -1)
        self.dateTime_1 = QDateTimeEdit(self.task_1)
        self.dateTime_1.setObjectName(u"dateTime_1")
        sizePolicy1.setHeightForWidth(self.dateTime_1.sizePolicy().hasHeightForWidth())
        self.dateTime_1.setSizePolicy(sizePolicy1)
        self.dateTime_1.setStyleSheet(u"")
        self.dateTime_1.setCalendarPopup(True)
        self.dateTime_1.setTimeSpec(Qt.LocalTime)

        self.gridLayout_1.addWidget(self.dateTime_1, 0, 1, 1, 1)

        self.taskText_1 = QTextEdit(self.task_1)
        self.taskText_1.setObjectName(u"taskText_1")

        self.gridLayout_1.addWidget(self.taskText_1, 2, 0, 2, 2)

        self.compCheck_1 = QCheckBox(self.task_1)
        self.compCheck_1.setObjectName(u"compCheck_1")

        self.gridLayout_1.addWidget(self.compCheck_1, 4, 0, 1, 1)

        self.deleteButton_1 = QPushButton(self.task_1)
        self.deleteButton_1.setObjectName(u"deleteButton_1")
        sizePolicy.setHeightForWidth(self.deleteButton_1.sizePolicy().hasHeightForWidth())
        self.deleteButton_1.setSizePolicy(sizePolicy)
        self.deleteButton_1.setMinimumSize(QSize(15, 15))
        self.deleteButton_1.setMaximumSize(QSize(143, 20))

        self.gridLayout_1.addWidget(self.deleteButton_1, 4, 1, 1, 1)


        self.gridLayout_taskWidget.addWidget(self.task_1, 0, 0, 1, 1)

        self.task_4 = QGroupBox(self.taskWidget)
        self.task_4.setObjectName(u"task_4")
        sizePolicy.setHeightForWidth(self.task_4.sizePolicy().hasHeightForWidth())
        self.task_4.setSizePolicy(sizePolicy)
        self.task_4.setMinimumSize(QSize(131, 60))
        self.task_4.setMaximumSize(QSize(262, 125))
        self.task_4.setAutoFillBackground(True)
        self.task_4.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_4 = QGridLayout(self.task_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.taskText_4 = QTextEdit(self.task_4)
        self.taskText_4.setObjectName(u"taskText_4")

        self.gridLayout_4.addWidget(self.taskText_4, 2, 0, 2, 2)

        self.compCheck_4 = QCheckBox(self.task_4)
        self.compCheck_4.setObjectName(u"compCheck_4")

        self.gridLayout_4.addWidget(self.compCheck_4, 4, 0, 1, 1)

        self.deleteButton_4 = QPushButton(self.task_4)
        self.deleteButton_4.setObjectName(u"deleteButton_4")
        sizePolicy.setHeightForWidth(self.deleteButton_4.sizePolicy().hasHeightForWidth())
        self.deleteButton_4.setSizePolicy(sizePolicy)
        self.deleteButton_4.setMinimumSize(QSize(15, 15))
        self.deleteButton_4.setMaximumSize(QSize(143, 20))

        self.gridLayout_4.addWidget(self.deleteButton_4, 4, 1, 1, 1)

        self.dateTime_4 = QDateTimeEdit(self.task_4)
        self.dateTime_4.setObjectName(u"dateTime_4")
        sizePolicy1.setHeightForWidth(self.dateTime_4.sizePolicy().hasHeightForWidth())
        self.dateTime_4.setSizePolicy(sizePolicy1)
        self.dateTime_4.setStyleSheet(u"")
        self.dateTime_4.setCalendarPopup(True)
        self.dateTime_4.setTimeSpec(Qt.LocalTime)

        self.gridLayout_4.addWidget(self.dateTime_4, 0, 1, 1, 1)


        self.gridLayout_taskWidget.addWidget(self.task_4, 0, 6, 1, 1)

        self.task_5 = QGroupBox(self.taskWidget)
        self.task_5.setObjectName(u"task_5")
        sizePolicy.setHeightForWidth(self.task_5.sizePolicy().hasHeightForWidth())
        self.task_5.setSizePolicy(sizePolicy)
        self.task_5.setMinimumSize(QSize(131, 60))
        self.task_5.setMaximumSize(QSize(262, 125))
        self.task_5.setAutoFillBackground(True)
        self.task_5.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_5 = QGridLayout(self.task_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.taskText_5 = QTextEdit(self.task_5)
        self.taskText_5.setObjectName(u"taskText_5")

        self.gridLayout_5.addWidget(self.taskText_5, 2, 0, 2, 2)

        self.compCheck_5 = QCheckBox(self.task_5)
        self.compCheck_5.setObjectName(u"compCheck_5")

        self.gridLayout_5.addWidget(self.compCheck_5, 4, 0, 1, 1)

        self.deleteButton_5 = QPushButton(self.task_5)
        self.deleteButton_5.setObjectName(u"deleteButton_5")
        sizePolicy.setHeightForWidth(self.deleteButton_5.sizePolicy().hasHeightForWidth())
        self.deleteButton_5.setSizePolicy(sizePolicy)
        self.deleteButton_5.setMinimumSize(QSize(15, 15))
        self.deleteButton_5.setMaximumSize(QSize(143, 20))

        self.gridLayout_5.addWidget(self.deleteButton_5, 4, 1, 1, 1)

        self.dateTime_5 = QDateTimeEdit(self.task_5)
        self.dateTime_5.setObjectName(u"dateTime_5")
        sizePolicy1.setHeightForWidth(self.dateTime_5.sizePolicy().hasHeightForWidth())
        self.dateTime_5.setSizePolicy(sizePolicy1)
        self.dateTime_5.setStyleSheet(u"")
        self.dateTime_5.setCalendarPopup(True)
        self.dateTime_5.setTimeSpec(Qt.LocalTime)

        self.gridLayout_5.addWidget(self.dateTime_5, 0, 1, 1, 1)


        self.gridLayout_taskWidget.addWidget(self.task_5, 1, 0, 1, 1)

        self.task_3 = QGroupBox(self.taskWidget)
        self.task_3.setObjectName(u"task_3")
        sizePolicy.setHeightForWidth(self.task_3.sizePolicy().hasHeightForWidth())
        self.task_3.setSizePolicy(sizePolicy)
        self.task_3.setMinimumSize(QSize(131, 60))
        self.task_3.setMaximumSize(QSize(262, 125))
        self.task_3.setAutoFillBackground(True)
        self.task_3.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.task_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.taskText_3 = QTextEdit(self.task_3)
        self.taskText_3.setObjectName(u"taskText_3")

        self.gridLayout_3.addWidget(self.taskText_3, 2, 0, 2, 2)

        self.compCheck_3 = QCheckBox(self.task_3)
        self.compCheck_3.setObjectName(u"compCheck_3")

        self.gridLayout_3.addWidget(self.compCheck_3, 4, 0, 1, 1)

        self.deleteButton_3 = QPushButton(self.task_3)
        self.deleteButton_3.setObjectName(u"deleteButton_3")
        sizePolicy.setHeightForWidth(self.deleteButton_3.sizePolicy().hasHeightForWidth())
        self.deleteButton_3.setSizePolicy(sizePolicy)
        self.deleteButton_3.setMinimumSize(QSize(15, 15))
        self.deleteButton_3.setMaximumSize(QSize(143, 20))

        self.gridLayout_3.addWidget(self.deleteButton_3, 4, 1, 1, 1)

        self.dateTime_3 = QDateTimeEdit(self.task_3)
        self.dateTime_3.setObjectName(u"dateTime_3")
        sizePolicy1.setHeightForWidth(self.dateTime_3.sizePolicy().hasHeightForWidth())
        self.dateTime_3.setSizePolicy(sizePolicy1)
        self.dateTime_3.setStyleSheet(u"")
        self.dateTime_3.setCalendarPopup(True)
        self.dateTime_3.setTimeSpec(Qt.LocalTime)

        self.gridLayout_3.addWidget(self.dateTime_3, 0, 1, 1, 1)


        self.gridLayout_taskWidget.addWidget(self.task_3, 0, 4, 1, 1)

        self.task_2 = QGroupBox(self.taskWidget)
        self.task_2.setObjectName(u"task_2")
        sizePolicy.setHeightForWidth(self.task_2.sizePolicy().hasHeightForWidth())
        self.task_2.setSizePolicy(sizePolicy)
        self.task_2.setMinimumSize(QSize(131, 60))
        self.task_2.setMaximumSize(QSize(262, 125))
        self.task_2.setAutoFillBackground(True)
        self.task_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_2 = QGridLayout(self.task_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.taskText_2 = QTextEdit(self.task_2)
        self.taskText_2.setObjectName(u"taskText_2")

        self.gridLayout_2.addWidget(self.taskText_2, 2, 0, 2, 2)

        self.compCheck_2 = QCheckBox(self.task_2)
        self.compCheck_2.setObjectName(u"compCheck_2")

        self.gridLayout_2.addWidget(self.compCheck_2, 4, 0, 1, 1)

        self.deleteButton_2 = QPushButton(self.task_2)
        self.deleteButton_2.setObjectName(u"deleteButton_2")
        sizePolicy.setHeightForWidth(self.deleteButton_2.sizePolicy().hasHeightForWidth())
        self.deleteButton_2.setSizePolicy(sizePolicy)
        self.deleteButton_2.setMinimumSize(QSize(15, 15))
        self.deleteButton_2.setMaximumSize(QSize(143, 20))

        self.gridLayout_2.addWidget(self.deleteButton_2, 4, 1, 1, 1)

        self.dateTime_2 = QDateTimeEdit(self.task_2)
        self.dateTime_2.setObjectName(u"dateTime_2")
        sizePolicy1.setHeightForWidth(self.dateTime_2.sizePolicy().hasHeightForWidth())
        self.dateTime_2.setSizePolicy(sizePolicy1)
        self.dateTime_2.setStyleSheet(u"")
        self.dateTime_2.setCalendarPopup(True)
        self.dateTime_2.setTimeSpec(Qt.LocalTime)

        self.gridLayout_2.addWidget(self.dateTime_2, 0, 1, 1, 1)


        self.gridLayout_taskWidget.addWidget(self.task_2, 0, 1, 1, 1)

        self.task_6 = QGroupBox(self.taskWidget)
        self.task_6.setObjectName(u"task_6")
        sizePolicy.setHeightForWidth(self.task_6.sizePolicy().hasHeightForWidth())
        self.task_6.setSizePolicy(sizePolicy)
        self.task_6.setMinimumSize(QSize(131, 60))
        self.task_6.setMaximumSize(QSize(262, 125))
        self.task_6.setAutoFillBackground(True)
        self.task_6.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_6 = QGridLayout(self.task_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.taskText_6 = QTextEdit(self.task_6)
        self.taskText_6.setObjectName(u"taskText_6")

        self.gridLayout_6.addWidget(self.taskText_6, 2, 0, 2, 2)

        self.compCheck_6 = QCheckBox(self.task_6)
        self.compCheck_6.setObjectName(u"compCheck_6")

        self.gridLayout_6.addWidget(self.compCheck_6, 4, 0, 1, 1)

        self.deleteButton_6 = QPushButton(self.task_6)
        self.deleteButton_6.setObjectName(u"deleteButton_6")
        sizePolicy.setHeightForWidth(self.deleteButton_6.sizePolicy().hasHeightForWidth())
        self.deleteButton_6.setSizePolicy(sizePolicy)
        self.deleteButton_6.setMinimumSize(QSize(15, 15))
        self.deleteButton_6.setMaximumSize(QSize(143, 20))

        self.gridLayout_6.addWidget(self.deleteButton_6, 4, 1, 1, 1)

        self.dateTime_6 = QDateTimeEdit(self.task_6)
        self.dateTime_6.setObjectName(u"dateTime_6")
        sizePolicy1.setHeightForWidth(self.dateTime_6.sizePolicy().hasHeightForWidth())
        self.dateTime_6.setSizePolicy(sizePolicy1)
        self.dateTime_6.setStyleSheet(u"")
        self.dateTime_6.setCalendarPopup(True)
        self.dateTime_6.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateTime_6, 0, 1, 1, 1)


        self.gridLayout_taskWidget.addWidget(self.task_6, 1, 1, 1, 1)


        self.taskGrid.addWidget(self.taskWidget, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.taskGrid)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.compTaskBox = QVBoxLayout()
        self.compTaskBox.setSpacing(4)
        self.compTaskBox.setObjectName(u"compTaskBox")
        self.compTaskLabel = QLabel(self.centralwidget)
        self.compTaskLabel.setObjectName(u"compTaskLabel")
        self.compTaskLabel.setMinimumSize(QSize(50, 0))
        self.compTaskLabel.setMaximumSize(QSize(256, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Georgia"])
        font3.setPointSize(12)
        self.compTaskLabel.setFont(font3)
        self.compTaskLabel.setFrameShape(QFrame.NoFrame)
        self.compTaskLabel.setTextFormat(Qt.PlainText)
        self.compTaskLabel.setScaledContents(False)
        self.compTaskLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.compTaskLabel.setMargin(0)

        self.compTaskBox.addWidget(self.compTaskLabel)

        self.compTaskList = QListWidget(self.centralwidget)
        self.compTaskList.setObjectName(u"compTaskList")
        sizePolicy.setHeightForWidth(self.compTaskList.sizePolicy().hasHeightForWidth())
        self.compTaskList.setSizePolicy(sizePolicy)
        self.compTaskList.setMinimumSize(QSize(50, 50))
        self.compTaskList.setMaximumSize(QSize(256, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Georgia"])
        font4.setPointSize(12)
        font4.setKerning(True)
        self.compTaskList.setFont(font4)
        self.compTaskList.setAlternatingRowColors(False)
        self.compTaskList.setSortingEnabled(False)

        self.compTaskBox.addWidget(self.compTaskList)

        self.compTaskClr = QPushButton(self.centralwidget)
        self.compTaskClr.setObjectName(u"compTaskClr")
        self.compTaskClr.setMinimumSize(QSize(50, 0))
        self.compTaskClr.setMaximumSize(QSize(256, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Georgia"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setUnderline(False)
        self.compTaskClr.setFont(font5)

        self.compTaskBox.addWidget(self.compTaskClr)


        self.horizontalLayout_2.addLayout(self.compTaskBox)

        self.horizontalLayout_2.setStretch(0, 1)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 925, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tasksLeftGroup.setTitle("")
        self.newTaskButton.setText(QCoreApplication.translate("MainWindow", u"Add new task", None))
        self.dropdownList.setItemText(0, QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))

        self.dropdownList.setCurrentText(QCoreApplication.translate("MainWindow", u"Total tasks todo:", None))
        self.task_1.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck_1.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton_1.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.task_4.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck_4.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton_4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.task_5.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck_5.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton_5.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.task_3.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck_3.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton_3.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.task_2.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck_2.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.task_6.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck_6.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton_6.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.compTaskLabel.setText(QCoreApplication.translate("MainWindow", u"Completed Tasks", None))
        self.compTaskClr.setText(QCoreApplication.translate("MainWindow", u"Clear Completed Tasks", None))
    # retranslateUi

