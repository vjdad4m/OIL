import pygame
from pygame import gfxdraw
from OIL.color import cWHITE
import numpy as np

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
    # Smart maths to center the palette
    x = w // 2 - (len(palette) // 2 + 1) * button_size
    i = 0
    for color in palette:
        buttons.append(Button(screen, color, [x, h-60, button_size, button_size], data=i))
        x += button_size * 1.5
        i += 1
    return buttons

class Canvas:
    def __init__(self, screen, size, resolution=1, color=cWHITE.rgb) -> None:
        self.screen = screen
        self.w, self.h = self.screen.get_size()
        self.size = size
        self.color = color
        self.pixels = np.zeros((self.size, self.size, 3))
        for y in range(self.size):
            for x in range(self.size):
                self.pixels[y][x] = cWHITE.rgb
        self.update()

    def update(self):
        for y in range(self.size):
            for x in range(self.size):
                gfxdraw.pixel(self.screen, x, y, self.pixels[y][x])