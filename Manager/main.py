# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from .database import createConnection
from .views import Window

    # Main function
def main():
        # Create App
    app = QApplication(sys.argv)

        # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)

        # Create Main Window
    win = Window()
    win.show()
    
        # Run event loop
    sys.exit(app.exec())