import pygame
from OILEditor.ui import *
import OIL as oil

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()

width = 720
height = 720

res = (width, height)
wasClick = False

screen = pygame.display.set_mode(res)

# x = Button(screen, oil.color.cRED.rgb, [0,0,100,100])
p = [oil.color.cGREEN.rgb, oil.color.cGREEN.rgb,oil.color.cGREEN.rgb, oil.color.cRED.rgb, oil.color.cWHITE.rgb]
palette_btns = GeneratePalette(screen, p, 40)

wasClick = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            wasClick = True
            click_pos = pygame.mouse.get_pos()
    if wasClick:
        for button in palette_btns:
            if button.isClicked(click_pos):
                print(f'Button id:{button.data} was clicked.')
        wasClick = False
    pygame.display.update()
    fpsClock.tick(FPS)