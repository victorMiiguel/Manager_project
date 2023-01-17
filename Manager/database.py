# -*- coding: utf-8 -*-

    # Module providing database connection

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createDataTable():
        # Create the contacts table in the database 
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            platform VARCHAR(40) NOT NULL,
            login VARCHAR(50) NOT NULL,
            password VARCHAR(40) NOT NULL
        )
        """
    )


def createConnection(databaseName):
        # Create and open a database connection
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Password Manager",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createDataTable()
    return True