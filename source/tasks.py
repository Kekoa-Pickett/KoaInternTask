#from forms.koaFirstProject import 
from PySide6.QtCore import (QCoreApplication, QDateTime, QSize, Qt)
from PySide6.QtWidgets import (QCheckBox, QDateTimeEdit, QGridLayout, QGroupBox, QListWidgetItem, QPushButton, QSizePolicy, QTextEdit)

''' This class creates the task group box that will be added to the task group
    Also deals with buttons and checkboxes that are clicked in the file'''
class TaskBox(QGroupBox):
    def __init__(self, view = None, config={}):
        super().__init__()
        self.setTitle("Todo")

        self.config = config
        self.view = view

        self._configure_ui()
        self._setup_connections()

    def _configure_ui(self):

        self.task = QGroupBox(self.view.taskWidget)
        self.task.setObjectName(self.config.get("object name", "task"))

        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())          #size setting
        self.setSizePolicy(sizePolicy)
        
        self.task.setSizePolicy(self.sizePolicy())
        self.task.setMinimumSize(QSize(131, 60))
        self.task.setMaximumSize(QSize(262, 125))
        self.task.setAutoFillBackground(True)
        self.task.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout = QGridLayout(self.task)
        self.gridLayout.setObjectName(self.config.get("gridlayout name", "gridlayout"))
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.dateTime = QDateTimeEdit(self.task)
        self.dateTime.setObjectName(u"dateTime")
        self.dateTime.setDateTime(QDateTime.currentDateTime())
        self.dateTime.setSizePolicy(self.sizePolicy())
        self.dateTime.setStyleSheet(u"")
        self.dateTime.setCalendarPopup(True)
        self.dateTime.setTimeSpec(Qt.LocalTime)

        self.gridLayout.addWidget(self.dateTime, 0, 1, 1, 1)

        self.taskText = QTextEdit(self.task)
        self.taskText.setObjectName(u"taskText")

        self.gridLayout.addWidget(self.taskText, 2, 0, 2, 2)

        self.compCheck = QCheckBox(self.task)
        self.compCheck.setObjectName(u"compCheck")
        
        self.gridLayout.addWidget(self.compCheck, 4, 0, 1, 1)

        self.deleteButton = QPushButton(self.task)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setSizePolicy(self.sizePolicy())
        self.deleteButton.setMinimumSize(QSize(15, 15))
        self.deleteButton.setMaximumSize(QSize(143, 20))

        self.gridLayout.addWidget(self.deleteButton, 4, 1, 1, 1)

        self.task.setTitle(QCoreApplication.translate("MainWindow", u"Task", None))
        self.taskText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of task...", None))
        self.compCheck.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        
        # Adding UI position to layout
        col = self.config.get("col position", 0)
        row = self.config.get("row position", 0)
        self.view.gridLayout_taskWidget.addWidget(self.task, col, row, 1, 1) #task 1
        
    def _setup_connections(self):
        self.compCheck.stateChanged.connect(lambda: self.completedTask(self.taskText.toPlainText()))
        self.deleteButton.clicked.connect(lambda: self.deleteTask())
        self.updateTaskLeftGroup(True)
    
    def completedTask(self, text = None):
        self.task.deleteLater()
        if text != "":
            self.view.compTaskList.addItem(QListWidgetItem(text))
        self.updateTaskLeftGroup(False)

    def updateTaskLeftGroup(self, add):
        if self.view.dropdownList.currentText() == "Total tasks todo:":
            self.view.numDisplay.setValue(
                    self.view.taskWidget.children().__len__() - 2)
            if add:
                self.view.numDisplay.setValue(self.view.numDisplay.value() + 1)
        else:
            print("Text is not accounted for yet")

    def deleteTask(self):
        self.task.deleteLater()
        self.updateTaskLeftGroup(False)
