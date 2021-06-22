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