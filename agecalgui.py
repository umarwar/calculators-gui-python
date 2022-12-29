"""
Assignment # 1 (Age Calculator Gui)

Created on tue Dec 13,2022

@author: MUHAMMAD UMAR (20021519-139)

"""

from datetime import date 
import sys
from PyQt6.QtWidgets import QPushButton, QLabel, QApplication, QWidget, QLineEdit, QDateEdit,QVBoxLayout
from PyQt6.QtCore import *

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Calculator")
        self.setFixedSize(250,230)
        self.body()
        self.show()
        
    def body(self):
        #creating layout and button
        layout = QVBoxLayout()
        self.data = QDateEdit()
        calculate = QPushButton("Calculate Age", clicked= self.cal_Action)
        calculate.setFixedSize(QSize(100, 30))
        calculate.setStyleSheet("background-color: green; color:white; font-weight:Bold")
        self.display = QLineEdit()
        self.display.setStyleSheet("color:blue;font-weight: bold; font-size:15px;")
        msg = QLabel("Enter in mm/dd/yy", self.setStyleSheet("font-size: 15px"))
        space = QLabel()
        msg_Output = QLabel("Age:")
        clear = QPushButton("Clear Field", clicked= self.clr_Action)
        clear.setFixedSize(QSize(100, 30))
        clear.setStyleSheet("background-color: red; color:white; font-weight:Bold")
        #Adding layout to window
        layout.addWidget(msg)
        layout.addWidget(self.data)
        layout.addWidget(calculate, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(space)
        layout.addWidget(msg_Output)
        layout.addWidget(self.display)
        layout.addWidget(clear, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(layout)
        
    def cal_Action(self):
        self.today = date.today()
        self.getInput = self.data.text()
        self.mon,self.date,self.year = self.getInput.split("/")
        if int(self.year) > int(self.today.year):
            self.display.setText("Invalid year")   
        else:
            self.age = int(self.today.year) - int(self.year)
            self.result = str(self.age) +" years" 
            self.display.setText(self.result)
            
    def clr_Action(self):
        self.display.setText("")        
            
         
        
app = QApplication(sys.argv)
window = mainWindow()
sys.exit(app.exec()) 