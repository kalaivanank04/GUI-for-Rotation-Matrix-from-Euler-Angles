import sys
import numpy as np
import sympy as sp
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QWidget
#from hvlayout import MyWindow
#from euler_angle import euler_angle

#x= np.array([[1,2,3],[4,5,6],[7,8,9]])

class MyWindow_array(QMainWindow):
    def __init__(self,x): 
        self.x = x
        

        super().__init__()

        self.setWindowTitle("Array Display Example")
        self.resize(600, 400)
        #x = (MyWindow.process_text(self))
        # Create a 3x3 array
        a,b,c=x[0],x[1],x[2]    
        
        RX = sp.Matrix([[1,0,0],[0,sp.cos(a),-sp.sin(a)],[0,sp.sin(a),sp.cos(a)]])
        RY = sp.Matrix([[sp.cos(b),0,sp.sin(b)],[0,1,0],[-(sp.sin(b)),0,sp.cos(b)]])
        RZ = sp.Matrix([[sp.cos(c),-(sp.sin(c)),0],[sp.sin(c),sp.cos(c),0],[0,0,1]])
        D = {'X':RX,'Y':RY,'Z':RZ}
        ang = D[c]@D[b]@D[a]
        ang = np.array(ang)

        # Create a 3x3 NumPy array
        self.ans = ang
        self.array = np.array([[88, 2, 3], [4, 5, 6], [7, 8, 9]])

        # Create a grid layout to hold the labels
        grid_layout = QGridLayout()

        # Create 3x3 labels and display array elements
        for i in range(3):
            for j in range(3):
                label = QLabel(str(self.ans[i][j]))
                grid_layout.addWidget(label, i, j)

        # Create a central widget and set the grid layout
        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = MyWindow_array()
    wind.show()
    sys.exit(app.exec())

#     if window.result:
#         x=window.result
# print(x)