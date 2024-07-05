#from forms.koaFirstProject import 
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QFrame, QGridLayout, QGroupBox, 
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextEdit, QVBoxLayout, QWidget)

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

        '''sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicyDate = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())          #size setting
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(131, 60))
        self.setMaximumSize(QSize(262, 125))
        self.setAutoFillBackground(True)
        self.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.dateTime = QDateTimeEdit(self)                                         # date feature
        self.dateTime.setDateTime(QDateTime.currentDateTime())
        self.dateTime.setObjectName(u"dateTime")
        self.dateTime.setGeometry(QRect(100, 10, 141, 22))
        sizePolicyDate.setHeightForWidth(self.dateTime.sizePolicy().hasHeightForWidth())
        self.dateTime.setSizePolicy(sizePolicyDate)
        self.dateTime.setCalendarPopup(True)
        self.dateTime.setTimeSpec(Qt.LocalTime)

        self.taskText = QTextEdit(self)                                             # textbox setting
        self.taskText.setObjectName(u"taskText")
        self.taskText.setGeometry(QRect(10, 40, 231, 51))
        self.taskText.setPlaceholderText("Name of task ...")

        self.deleteButton = QPushButton(u"Delete", self)                            # delete button settings
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(180, 100, 61, 20))

        self.compCheck = QCheckBox("Completed", self)                              # Completed settings
        self.compCheck.setObjectName(u"compCheck1")
        self.compCheck.setGeometry(QRect(10, 100, 91, 20))



        self.gridLayout_2 = QGridLayout(self)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.taskText1 = QTextEdit(self)
        self.taskText1.setObjectName(u"taskText1")

        self.gridLayout_2.addWidget(self.taskText1, 2, 0, 2, 2)

        self.compCheck1 = QCheckBox(self)
        self.compCheck1.setObjectName(u"compCheck1")

        self.gridLayout_2.addWidget(self.compCheck1, 4, 0, 1, 1)

        self.deleteButton1 = QPushButton(self)
        self.deleteButton1.setObjectName(u"deleteButton1")

        self.gridLayout_2.addWidget(self.deleteButton1, 4, 1, 1, 1)

        self.dateTime1 = QDateTimeEdit(self)
        self.dateTime1.setObjectName(u"dateTime1")
        sizePolicy1.setHeightForWidth(self.dateTime1.sizePolicy().hasHeightForWidth())
        self.dateTime1.setSizePolicy(sizePolicy1)
        self.dateTime1.setStyleSheet(u"")
        self.dateTime1.setCalendarPopup(True)
        self.dateTime1.setTimeSpec(Qt.LocalTime)

        self.gridLayout_2.addWidget(self.dateTime1, 0, 1, 1, 1)'''

        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())          #size setting
        self.setObjectName(u"task1")
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(131, 60))
        self.setMaximumSize(QSize(262, 125))
        self.setAutoFillBackground(True)
        self.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayout_2 = QGridLayout(self)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.taskText1 = QTextEdit(self)
        self.taskText1.setObjectName(u"taskText1")

        self.gridLayout_2.addWidget(self.taskText1, 2, 0, 2, 2)

        self.compCheck = QCheckBox(self)
        self.compCheck.setObjectName(u"compCheck1")

        self.gridLayout_2.addWidget(self.compCheck, 4, 0, 1, 1)

        self.deleteButton = QPushButton(u"Delete", self)

        self.gridLayout_2.addWidget(self.deleteButton, 4, 1, 1, 1)

        self.dateTime = QDateTimeEdit(self)
        self.dateTime.setObjectName(u"dateTime1")
        sizePolicy.setHeightForWidth(self.dateTime.sizePolicy().hasHeightForWidth())
        self.dateTime.setSizePolicy(sizePolicy)
        self.dateTime.setStyleSheet(u"")
        self.dateTime.setCalendarPopup(True)
        self.dateTime.setTimeSpec(Qt.LocalTime)

        self.gridLayout_2.addWidget(self.dateTime, 0, 1, 1, 1)

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
        #self.view.sizePolicy1.setHeightForWidth(self.dateTime.sizePolicy().hasHeightForWidth())
        #self.sizePolicy1().setHeightForWidth(self.dateTime.sizePolicy().hasHeightForWidth())
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
        #self.sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        #self.deleteButton.setSizePolicy(self.sizePolicy)
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
        self.view.compTaskList.addItem(QListWidgetItem(text))
        #self.ui.taskGrid.removeItem(QGroupBox(taskBox))
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
        #self.ui.taskGrid.removeWidget(taskBox)
        self.task.deleteLater()
        self.updateTaskLeftGroup(False)
