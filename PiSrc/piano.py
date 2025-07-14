import sys
import time
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt

BUZZPIN = 27
Melody = [261.63, 277.18, 293.66, 311.13, 
          329.63, 349.23, 369.99, 392.00, 
          415.30, 440.00, 466.16, 493.88, 523.25]

class Windowclass(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = uic.loadUi("Piano.ui", self)
        self.create_keys()
        self.ui.show()
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BUZZPIN, GPIO.OUT)
    
    def create_keys(self):
        layout = self.ui.pianoKey

        Keys = [
            ('C(도)', 0, 0), ('C#(도#)', 0, 1), ('D(레)', 0, 2), ('D#(레#)', 0, 3),
            ('E(미)', 0, 4), ('F(파)', 0, 5), ('F#(파#)', 0, 6), ('G(솔)', 0, 7),
            ('G#(솔#)', 0, 8), ('A(라)', 0, 9), ('A#(라#)', 0, 10), ('B(시)', 0, 11), ('C(도)', 0, 12)
        ]

        for idx, (key, row, col) in enumerate(Keys):
            if '#' in key:
                button = QPushButton(key)
                button.setStyleSheet("background-color: black; border: 1px solid black;")
                button.setFixedSize(60, 180)
                layout.addWidget(button, row, col, 1, 1, Qt.AlignTop)
            else:
                button = QPushButton(key)
                button.setStyleSheet("background-color: white; border: 1px solid black;")
                button.setFixedSize(100, 300)
                layout.addWidget(button, row, col, 1, 1)

            button.setProperty('index', idx)
            button.clicked.connect(self.btn_click)

    def btn_click(self):
        button = self.sender()
        index = button.property('index')
        sound = GPIO.PWM(BUZZPIN, 440)
        self.ui.label.setText(f"{button.text()}")

        try:
            sound.start(50)
            sound.ChangeFrequency(Melody[index])
            time.sleep(0.2)
            sound.stop()
            
        except KeyboardInterrupt:
            GPIO.cleanup()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Windowclass()
    app.exec_()