import sys
import time
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5 import uic

RED = 14
GREEN = 15
BLUE = 18

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = uic.loadUi("btn_led.ui", self)
		self.ui.show()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(RED, GPIO.OUT)
		GPIO.setup(GREEN, GPIO.OUT)
		GPIO.setup(BLUE, GPIO.OUT)

	def btnRed(self):
		self.ledOff()
		GPIO.output(RED, GPIO.LOW)
		self.ui.label.setText("RED ON!")

	def btnGreen(self):
		self.ledOff()
		GPIO.output(GREEN, GPIO.LOW)
		self.ui.label.setText("GREEN ON!")

	def btnBlue(self):
		self.ledOff()
		GPIO.output(BLUE, GPIO.LOW)
		self.ui.label.setText("BLUE ON!")

	def btnOff(self):
		self.ledOff()
		self.ui.label.setText("LED OFF!")

	def ledOff(self):
		GPIO.output(RED, GPIO.HIGH)
		GPIO.output(GREEN, GPIO.HIGH)
		GPIO.output(BLUE, GPIO.HIGH)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()
