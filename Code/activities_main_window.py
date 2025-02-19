from PyQt6 import uic
from PyQt6 import QtCore, QtWidgets, QtGui
import os

FORM_CLASS2, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__dict__), 'C:\Users\maciek\Desktop\Projekty_github\TODO_app\UI\Activities_view.ui'))

class Activities_Dialog(QtWidgets.QDialog, FORM_CLASS2):
    def __init__(self, parent=None):
        super(Activities_Dialog, self).__init__()
        self.setupUI(self)
        self.name = ""
        self.projects_num = 0
        self.face_image = ""
        self.activity_title = ""
        self.tasks_done = 0
        self.all_tasks = 0
        
        self.labelGreeting.setText(f"Hello, {self.name}!")
        self.labelProjectsNum.setText(f"You have {self.projects_num} projects")
        #self.label_Image.set
        
        self.labelActivityTitle.setText(f"{self.activity_title}")
        self.progressBar.setValue(self.tasks_done *10)
        self.labelProgress.setText(f"{self.tasks_done} / {self.all_tasks} tasks completed")
        self.pushButtonMoreInfo.clicked.connect(lambda: self.more_info)
        self.pushButtonAdd.clicked.connect(lambda: self.add_task)
        
    def setupData(self):
        #TODO dodać funkcjonalność zmiany tekstu w labelach i ogólnie dodawanie aktywności
    def more_info(self):
        pass
    def add_task(self):
        pass
        