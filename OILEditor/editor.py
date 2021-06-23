import pygame
import OIL as oil

pygame.init()

width = 720
height = 720

res = (width, height)

screen = pygame.display.set_mode(res)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            print(f'Click at {click_pos}')
