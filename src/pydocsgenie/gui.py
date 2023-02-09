from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from inference import inference
import sys


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
        generate_button = QPushButton("Generate Docstring", self)
        clear_button = QPushButton("Clear", self)
        self.textbox_input = QLineEdit(self)
        self.textbox_output = QTextBrowser(self)
        # setting geometry of button
        generate_button.setGeometry(200, 30, 200, 40)
        clear_button.setGeometry(400, 30, 200, 40)
        self.textbox_input.setGeometry(20, 100, 200, 200)
        self.textbox_output.setGeometry(320, 100, 200, 200)

        # adding action to buttons
        generate_button.clicked.connect(self.generate_docstring)
        clear_button.clicked.connect(self.clear_output)

    # action method for generating docstring
    def generate_docstring(self):
        input_text = self.textbox_input.text()     
        output = inference(input_text)
        self.textbox_output.append(output)

    # action method for clearing output
    def clear_output(self):
        self.textbox_output.clear()

App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())