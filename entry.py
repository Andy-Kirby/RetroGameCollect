from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QMainWindow,
    QAction,
    qApp,
    QLabel,
    QPushButton,
    QComboBox,
    QListView,
    QGroupBox,
    QRadioButton,
    QTableWidget,
    QTableView,
    QLineEdit,
    QDoubleSpinBox,
    QAbstractSpinBox,
)
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QFont
import sqlite3


class MyQDoubleSpinBox(QDoubleSpinBox):
    def focusInEvent(self, event):
        if not self.value():
            self.clear()
            super().focusInEvent(event)


class Entry(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Create New Entry")
        self.setFixedSize(500, 330)
        # Header
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/header.png"))
        self.label.setGeometry(0, 0, 500, 50)
        # Main Logo
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/create.png"))
        self.label.setGeometry(15, 15, 204, 34)
        # (Title:)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Title:")
        self.group_box_settings.setGeometry(15, 50, 320, 65)
        self.tableTitle = QLineEdit(self)
        self.tableTitle.setGeometry(30, 80, 290, 20)

        # (ProductID:)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Product ID:")
        self.group_box_settings.setGeometry(345, 50, 130, 65)
        self.tableProduct = QLineEdit(self)
        self.tableProduct.setGeometry(360, 80, 100, 20)

        # (Format:)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Format:")
        self.group_box_settings.setGeometry(15, 120, 320, 65)
        # Combo Box
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QRect(25, 145, 300, 31))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem("Please Select...")
        self.comboBox.addItem("Sega Master System")
        self.comboBox.addItem("Sega Megadrive")
        self.comboBox.addItem("Sega Saturn")
        self.comboBox.addItem("Sega Dreamcast")
        self.comboBox.addItem("Sega Game Gear")
        self.comboBox.addItem("Nintendo NES")
        self.comboBox.addItem("Super Nintendo")
        self.comboBox.addItem("Nintendo64")
        self.comboBox.addItem("Nintendo Game Cube")
        self.comboBox.addItem("Nintendo Game Boy")
        self.comboBox.addItem("PlayStation 1")
        self.comboBox.addItem("PSOne")
        self.comboBox.addItem("Microsoft XBOX")

        # (Price Paid:)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Price Paid:")
        self.group_box_settings.setGeometry(345, 120, 130, 65)
        self.tableTotal = MyQDoubleSpinBox(self)
        self.tableTotal.setDecimals(2)
        self.tableTotal.setMinimum(0.00)
        self.tableTotal.setMaximum(500.00)
        self.tableTotal.setSingleStep(0.01)
        self.tableTotal.setPrefix("£")
        self.tableTotal.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.tableTotal.setButtonSymbols(QDoubleSpinBox.NoButtons)
        self.tableTotal.setGeometry(360, 150, 100, 20)

        # (Type:)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Type:")
        self.group_box_settings.setGeometry(15, 190, 155, 65)
        # Combo Box
        self.comboFormat = QComboBox(self)
        self.comboFormat.setGeometry(QRect(25, 215, 135, 31))
        self.comboFormat.setObjectName(("comboBox"))
        self.comboFormat.addItem("Please Select...")
        self.comboFormat.addItem("Hardware")
        self.comboFormat.addItem("Software")

        # (Grade:)
        self.group_box_settings = QGroupBox(self)
        self.group_box_settings.setTitle("Grade:")
        self.group_box_settings.setGeometry(180, 190, 155, 65)
        # Combo Box
        self.comboGrade = QComboBox(self)
        self.comboGrade.setGeometry(QRect(190, 215, 135, 31))
        self.comboGrade.setObjectName(("comboBox"))
        self.comboGrade.addItem("Please Select...")
        self.comboGrade.addItem("Low")
        self.comboGrade.addItem("Medium")
        self.comboGrade.addItem("High")

        # Create Button
        self.add_button = QPushButton("Create Entry", self)
        self.add_button.resize(130, 50)
        self.add_button.move(345, 205)
        self.add_button.setToolTip("Create Entry")
        # self.add_button.clicked.connect(self.entryWindow)

        # Footer
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./img/footer.png"))
        self.label.setGeometry(0, 290, 500, 45)

        self.show()
        self.tableTitle.setFocus()
