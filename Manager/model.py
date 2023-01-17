# -*- coding: utf-8 -*-

"""Module providing a model to manage table"""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class ManagerModel:
    def __init__(self):
        self.model = self._createModel()

    @staticmethod
    def _createModel():
        # Create and set up model
        tableModel = QSqlTableModel()
        tableModel.setTable("accounts")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ("ID", "platform", "login", "password")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel

    def addContact(self, data):
            # Add new content to database
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()
        self.model.select()
        
    def deleteContact(self, row):
        """Remove a contact from the database."""
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clearContacts(self):
        """Remove all contacts in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()