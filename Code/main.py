from PyQt6 import uic
from PyQt6 import QtCore, QtWidgets, QtGui
import os
from login_register_dialog import Login_Register
class Main_Window():
    def __init__(self):
        self.login_register_dialog = Login_Register()
        self.login_register_dialog.show()
        

app = QtWidgets.QApplication([])
main_window = Main_Window()
app.exec()