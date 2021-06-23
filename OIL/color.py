class Color():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'

    @property
    def rgb(self):
        return (self.r, self.g, self.b)

cRED = Color(255, 0, 0)
cGREEN = Color(0, 255, 0)
cBLUE = Color(0, 0, 255)

# NOTE: Do not use cWHITE and cBLACK in labels, as theese colors will be used to fill the blanks
cWHITE = Color(255, 255, 255)
cBLACK = Color(0, 0, 0)
