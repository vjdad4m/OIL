import pygame

class Button:
    def __init__(self, screen, color, dimension, data="") -> None:
        self.screen = screen
        self.color = color
        self.position = dimension
        self.data = data
        pygame.draw.rect(screen, color, dimension)
    
    def isClicked(self, mouseClickPosition):
        if self.position[0] < mouseClickPosition[0] < self.position[0] + self.position[2] and self.position[1] < mouseClickPosition[1] < self.position[1] + self.position[3]:
            return True
        return False

def GeneratePalette(screen, palette, button_size):
    # Screen: pygame screen
    # Palette: list of colors
    # Button_size: int size of square button
    buttons = []
    w, h = screen.get_size()
    # Smart maths to center the paletter
    x = w // 2 - (len(palette) // 2 + 1) * button_size
    i = 0
    for color in palette:
        buttons.append(Button(screen, color, [x, h-60, button_size, button_size], data=i))
        x += button_size * 1.5
        i += 1
    return buttons