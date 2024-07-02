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
    def __init__(self, centralWidget = None):
        super().__init__(centralWidget)
        self.setTitle("Todo")

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicyDate = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())          #size setting
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(262, 125))
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
        self.taskText.setPlaceholderText("Describe task ...")

        self.deleteButton = QPushButton(u"Delete", self)                            # delete button settings
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(180, 100, 61, 20))
        self.deleteButton.clicked.connect(self.deleteLater)

        self.compCheck = QCheckBox("Completed", self)                              # Completed settings
        self.compCheck.setObjectName(u"compCheck1")
        self.compCheck.setGeometry(QRect(10, 100, 91, 20))
        self.compCheck.stateChanged.connect(lambda : self.completedTask(centralWidget, self.taskText.toPlainText()))
        
    ''' Moves task over to completed section '''
    def completedTask(self, centralWidget = None, text = None):
        #if (self.compCheck.isChecked()):                               # Allow user to still have access to it
            vertLayout = centralWidget.findChild(QWidget, name="verticalLayoutWidget")
            compTaskList = vertLayout.findChild(QListWidget, name="compTaskList")
            if (text != ""):
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