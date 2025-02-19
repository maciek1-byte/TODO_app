from PyQt6 import uic
from PyQt6 import QtCore, QtWidgets, QtGui
import os
from functions import email_validator, password_check, convert_to_binary_data
import sqlite3
import cv2
#from activities_main_window import Activities_Dialog

FORM_CLASS1, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'C:/Users/maciek/Desktop/Projekty_github/TODO_app/UI/login_dialog.ui'))


class Login_Register(QtWidgets.QDialog,FORM_CLASS1):
    def __init__(self):
        super(Login_Register, self).__init__()
        self.setupUi(self)
        
        self.reg_email = self.lineEditEmail_Reg.text()
        self.reg_password = self.lineEditPassword_Reg.text()
        self.reg_name = self.lineEditFirstName_Reg.text()
        
        self.log_email = self.lineEditEmail_Sign.text()
        self.log_password = self.lineEditPassword_Sign.text()
        
        self.error_message = ""    
            
        self.pushButtonImage.clicked.connect(lambda: self.SelectImage())
        self.pushButtonRegister.clicked.connect(lambda: self.Register())
        self.pushButtonLogin.clicked.connect(lambda: self.Login())
        
    def SelectImage(self):
        #try:
            self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', '', 'JPG files (*.jpg)')
            print(self.file_path)
            self.empPhoto = convert_to_binary_data(self.file_path)
            self.color_image = cv2.imread(self.file_path)
            if self.file_path:
                QtWidgets.QMessageBox.information(self,"Information","Image chosen successfully",buttons=QtWidgets.QMessageBox.StandardButton.Ok, defaultButton=QtWidgets.QMessageBox.StandardButton.NoButton)
            #self.fi = QtCore.QFileInfo(self.file_path)
            #self.file_name = self.fi.fileName()
            self.image = cv2.cvtColor(self.color_image, cv2.COLOR_RGB2LAB)
        #except Exception as e:
            #QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {e}")
    def Register(self):

        print(self.lineEditEmail_Reg.text() ,self.lineEditPassword_Reg.text(), self.lineEditFirstName_Reg.text())
        # Check if all fields have data
        #if self.reg_email=="" or self.reg_password=="" or self.reg_name=="":
        #    self.error_message = "Please enter all data"
        #    self.labelError_Reg.setText(self.error_message)
        valueret = email_validator(self.reg_email)
        if valueret== False:
            self.error_message = "Invalid email address"
            self.labelError_Reg.setText(self.error_message)
        elif not password_check(self.reg_password):
            self.error_message = (
                "Password should be at least 6 characters long, contain at least one uppercase letter, "
                "one lowercase letter, one number, and one of the symbols $@#%."
            )
            self.labelError_Reg.setText(self.error_message)
        elif not self.checkBoxAgreement_Reg.isChecked():
            self.error_message = "Please agree to the terms and conditions"
            self.labelError_Reg.setText(self.error_message)
        elif self.image == "":
            self.error_message = "Please select an image"
            self.labelError_Reg.setText(self.error_message)
            self.lineEditEmail_Reg.setText("")
            self.lineEditPassword_Reg.setText("")
            self.lineEditFirstName_Reg.setText("")
        else:
            self.error_message = ""
            self.labelError_Reg.setText("")
            try:
                self.connection = sqlite3.connect("data.db")
                self.cursor = self.connection.cursor()

                self.cursor.execute("SELECT * FROM Users")
                selected_data = self.cursor.fetchall()
                for row in selected_data:
                    if row[1] == self.reg_email:
                        self.error_message = "Email already exists"
                        self.labelError_Reg.setText(self.error_message)
                        return 
                    elif row[2] == self.reg_password:
                        self.error_message = "Password already exists"
                        self.labelError_Reg.setText(self.error_message)
                        return

                # Insert the new user
                insert_query = "INSERT INTO Users(email, password, name, profile_image) VALUES(?,?,?,?)"
                self.cursor.execute(insert_query, (self.reg_email, self.reg_password, self.reg_name, self.image))
                self.connection.commit()
                self.labelError_Reg.setText("Registration successful")
            except sqlite3.Error as e:
                self.error_message = f"Database error: {e}"
                self.labelError_Reg.setText(self.error_message)
            finally:
                if hasattr(self, "connection"):
                    self.connection.close()

    def Login(self):
        #try:
            if not self.log_email or not self.log_password:
                self.error_message = "Please enter email and password"
                self.labelError_Sign.setText(self.error_message)
            else:
                self.error_message = ""
                self.labelError_Sign.setText("")
                select = """SELECT email, password, name, profile_image"""
                selected_data = self.cursor.fetchall()
                for row in selected_data:
                    if row[0] == self.self.log_email and row[1] == self.log_password:
                        self.error_message = "Login successful"
                        self.labelError_Log.setText(self.error_message)
                        self.hide()
                        #self.activitiesDialog = Activities_Dialog()
                        #self.activitiesDialog.show()
                    else:
                        self.error_message = "Invalid email or password"
                        self.labelError_Log.setText(self.error_message)
                self.connection.close()
        #except Exception as e:
            #QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {e}")        
