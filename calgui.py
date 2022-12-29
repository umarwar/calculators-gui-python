import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from PyQt6.QtGui import *
from PyQt6.QtCore import *

numeric_style = ("background-color: grey; color: white; font-size: 16px; font-weight: bold; border-radius: 20px")
operator_style = ("background-color: orange; color: white; font-size: 16px; font-weight: bold; border-radius: 20px")
clear_style = ("background-color: darkgrey; color: black; font-size: 16px; border-radius: 20px")
b_height = 40
b_width = 80

class Calwindow(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("OP Calculator")
		self.setStyleSheet("background-color: black")
		self.setFixedSize(365,350)
		self.calbody()

	def calbody(self):
		self.label = QLabel(self)
		self.label.setGeometry(5, 5, 350, 70)
		self.label.setWordWrap(True)
		self.label.setStyleSheet("QLabel""{""border : 4px solid black; background : black; color: white; font-size: 26px""}")
		self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
		
		num1 = QPushButton("1", self)
		num1.setStyleSheet(numeric_style)
		num1.setGeometry(5, 150, b_width, b_height)
		num2 = QPushButton("2", self)
		num2.setStyleSheet(numeric_style)
		num2.setGeometry(95, 150, 80, 40)
		num3 = QPushButton("3", self)
		num3.setStyleSheet(numeric_style)
		num3.setGeometry(185, 150, 80, 40)
		num4 = QPushButton("4", self)
		num4.setStyleSheet(numeric_style)
		num4.setGeometry(5, 200, 80, 40)
		num5 = QPushButton("5", self)
		num5.setStyleSheet(numeric_style)
		num5.setGeometry(95, 200, 80, 40)
		num6 = QPushButton("6", self)
		num6.setStyleSheet(numeric_style)
		num6.setGeometry(185, 200, 80, 40)
		num7 = QPushButton("7", self)
		num7.setStyleSheet(numeric_style)
		num7.setGeometry(5, 250, 80, 40)
		num8 = QPushButton("8", self)
		num8.setStyleSheet(numeric_style)
		num8.setGeometry(95, 250, 80, 40)
		num9 = QPushButton("9", self)
		num9.setStyleSheet(numeric_style)
		num9.setGeometry(185, 250, 80, 40)
		num0 = QPushButton("0", self)
		num0.setStyleSheet(numeric_style)
		num0.setGeometry(5, 300, 170, 40)

		equal = QPushButton("=", self)
		equal.setGeometry(275, 300, 80, 40)
		equal.setStyleSheet(operator_style)
  
		plus = QPushButton("+", self)
		plus.setGeometry(275, 250, 80, 40)
		plus.setStyleSheet(operator_style)

		minus = QPushButton("-", self)
		minus.setGeometry(275, 200, 80, 40)
		minus.setStyleSheet(operator_style)
  
		mul = QPushButton("*", self)
		mul.setGeometry(275, 150, 80, 40)
		mul.setStyleSheet(operator_style)

		div = QPushButton("/", self)
		div.setGeometry(275, 100, 80, 40)
		div.setStyleSheet(operator_style)

		dot = QPushButton(".", self)
		dot.setGeometry(185, 300, 80, 40)
		dot.setStyleSheet(numeric_style)

		clear = QPushButton("Clear", self)
		clear.setGeometry(5, 100, 170, 40)
		clear.setStyleSheet(clear_style)

		dele = QPushButton("Del", self)
		dele.setGeometry(185, 100, 80, 40)
		dele.setStyleSheet(clear_style)

		minus.clicked.connect(self.action_minus)
		equal.clicked.connect(self.action_equal)
		num0.clicked.connect(self.action0)
		num1.clicked.connect(self.action1)
		num2.clicked.connect(self.action2)
		num3.clicked.connect(self.action3)
		num4.clicked.connect(self.action4)
		num5.clicked.connect(self.action5)
		num6.clicked.connect(self.action6)
		num7.clicked.connect(self.action7)
		num8.clicked.connect(self.action8)
		num9.clicked.connect(self.action9)
		div.clicked.connect(self.action_div)
		mul.clicked.connect(self.action_mul)
		plus.clicked.connect(self.action_plus)
		dot.clicked.connect(self.action_dot)
		clear.clicked.connect(self.action_clear)
		dele.clicked.connect(self.action_del)

	def action_equal(self):

		expression = self.label.text()
		try:
			ans = eval(expression)
			self.label.setText(str(ans))
		except:
			self.label.setText("ERROR")

	def action_plus(self):
		text = self.label.text()
		self.label.setText(text + " + ")

	def action_minus(self):
		text = self.label.text()
		self.label.setText(text + " - ")

	def action_div(self):
		text = self.label.text()
		self.label.setText(text + " / ")

	def action_mul(self):
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_dot(self):
		text = self.label.text()
		self.label.setText(text + ".")

	def action0(self):
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		text = self.label.text()
		self.label.setText(text + "9")

	def action_clear(self):
		self.label.setText("")

	def action_del(self):
		text = self.label.text()
		# print(text[:-1])
		self.label.setText(text[:-1])

App = QApplication(sys.argv)
window = Calwindow()
window.show()

sys.exit(App.exec())