
# importing libraries
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from inference import inference


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()
 
    # method for widgets
    def UiComponents(self):
 
        # creating a push button
        button = QPushButton("Get Docstrings", self)
        self.textbox_input = QLineEdit(self)
        self.textbox_output = QTextBrowser(self)
        # setting geometry of button
        button.setGeometry(200, 30, 200, 40)
        self.textbox_input.setGeometry(20, 100, 200, 200)
        self.textbox_output.setGeometry(320, 100, 200, 200)

        # adding action to a button
        button.clicked.connect(self.clickme)

    # action method
    def clickme(self):
        input_text = self.textbox_input.text()     
        output = inference(input_text)
        self.textbox_output.append(output)