import sys

from pydocsgenie.inference import inference
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Python ")
 
        # setting geometry
        self.setGeometry(100, 100, 1300, 800)
 
        # calling method
        self.UiComponents()
 
        # showing all the widgets
        self.show()


    # method for widgets
    def UiComponents(self):

        # creating a push button
        generate_button = QPushButton("Generate Docstring", self)
        clear_button = QPushButton("Clear", self)
        self.textbox_input = QTextEdit(self)
        self.textbox_output = QTextBrowser(self)
        copy_button = QPushButton("Copy", self)
        copy_button.setIcon(QIcon("copy.png"))
        # setting geometry of buttons
        generate_button.setGeometry(200, 30, 200, 40)
        clear_button.setGeometry(400, 30, 200, 40)
        copy_button.setGeometry(600, 30, 200, 40)
        self.textbox_input.setGeometry(20, 100, 600, 600)
        self.textbox_output.setGeometry(650, 100, 600, 600)

        input_label = QLabel("Input", self)
        input_label.setGeometry(20, 80, 100, 20)
        output_label = QLabel("Output", self)
        output_label.setGeometry(650, 80, 100, 20)

        # adding action to buttons
        generate_button.clicked.connect(self.generate_docstring)
        clear_button.clicked.connect(self.clear_output)
        copy_button.clicked.connect(self.copy_text)

    # action method for generating docstring
    def generate_docstring(self):
        input_text = self.textbox_input.toPlainText()     
        output = inference(input_text)
        self.textbox_output.setPlainText(output)
    
    # action method for clearing output
    def clear_output(self):
        self.textbox_input.clear()
        self.textbox_output.clear()
    
    # action method for copying text
    def copy_text(self):
        """Copy the text from the output textbox.

        This method copies the text from the output textbox to the clipboard.

        Parameters
        ----------
        self : QWidget
            The instance of the QWidget class.

        Returns
        -------
        None

        Examples
        --------
        >>> copy_text(self)
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(self.textbox_output.toPlainText())
    

def run_app():
    App = QApplication(sys.argv)

    # create the instance of our Window
    Window()

    # start the app
    sys.exit(App.exec())
