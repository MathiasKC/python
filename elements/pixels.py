import pygame, sys
import math
import random
size = width, height = 500, 500
cols = height
rows = width

black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
FPS = 30
fpsClock = pygame.time.Clock()


class Pixel:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.color = white

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.i, self.j, 1, 1))


pixel_array = []


for i in range(cols):
    pixel_rows = []
    for j in range(rows):
        pixel_rows.append(Pixel(i, j))
    pixel_array.append(pixel_rows)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #mouse click

    screen.fill(black)
    for i in range(cols):
        for j in range(rows):
            pixel_array[i][j].draw()
    pygame.display.flip()
    fpsClock.tick(FPS)
