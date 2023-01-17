# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from .model import ManagerModel


    # Main Window.
class Window(QMainWindow):

    def __init__(self, parent=None):
            # Initializer
        super().__init__(parent)
        self.setWindowTitle("Password Maganer")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.managerModel = ManagerModel()
        self.setupUI()

    def setupUI(self):
            # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.managerModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
            # Create Buttons
        self.addButton = QPushButton("New")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContent)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearContents)
            # layout
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.managerModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()

    def deleteContent(self):
        """Delete the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.managerModel.deleteContact(row)

    def clearContents(self):
        """Remove all contacts from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your contacts?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.managerModel.clearContacts()
            

class AddDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Add Data")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()
    
    def setupUI(self):
            # Create line edits for data
        self.platformField = QLineEdit()
        self.platformField.setObjectName("platform")
        self.loginField = QLineEdit()
        self.loginField.setObjectName("login")
        self.passwordField = QLineEdit()
        self.passwordField.setObjectName("password")
            # Lay out data fields
        layout = QFormLayout()
        layout.addRow("platform: ", self.platformField)
        layout.addRow("login: ", self.loginField)
        layout.addRow("password: ", self.passwordField)
        self.layout.addLayout(layout)
            # Add buttons to dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):

        self.data = []
        for field in (self.platformField, self.loginField, self.passwordField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "error!",
                    f"you must provide correct information"
                )
                self.data = None
                return
            
            self.data.append(field.text())

        if not self.data:
            return

        super().accept()