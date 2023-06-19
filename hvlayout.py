import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from array_disp import MyWindow_array
import sympy as sp
import numpy as np


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Input Example")
        self.resize(300, 150)

        self.text_label = QLabel("Enter Text:")
        self.line_edit = QLineEdit()
        
        self.button = QPushButton("Process Text")
        self.button.clicked.connect(self.process_text)
        self.button_1 = QPushButton("Show rotation matrix")   
        self.button_1.clicked.connect(self.openwindow)

        layout = QVBoxLayout()
        layout.addWidget(self.text_label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.button_1)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create an attribute to store the result
        self.result = None

    def openwindow(self):
        x=str(MyWindow.process_text(self))
        print(x)
        self.win = MyWindow_array(x)
        self.ui = MyWindow_array(x)
        window.hide()
        #self.ui.setupUi(self.window)
        self.win.show()

    def process_text(self):
        text = self.line_edit.text()
        self.result = text

        if window.result:
            x=window.result
            # print(f"Processed Result: {window.result}")
            #print(x)
            x= x.upper()
            # a,b,c=x[0],x[1],x[2]
            # print(a,b,c)
        return(x)
        #self.close()

    # def my_function(self, text):
    #     # Implement your custom function here that takes the text as input
    #     # and returns the result based on your programming logic
    #     # Example: Capitalize the text
    #     return text.capitalize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()

    # Use the result after the GUI is closed

        
        



    # Continue with the rest of your program...
