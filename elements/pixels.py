import pygame, sys
import math
import random
size = width, height = 150, 150
cols = height
rows = width

black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
FPS = 60
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
    pixel_array[int(cols/2)][0].color = black

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #mouse click

    screen.fill(black)
    for x in range(cols):
        for y in range(rows):
            pixel_array[x][y].draw()
    for x in range(cols):
        for y in range(rows):
            if y < cols - 1:
                if pixel_array[x][y].color == black and pixel_array[x][y + 1].color == white:
                    pixel_array[x][y + 1].color = black
                    pixel_array[x][y].color = white

                if x < rows - 1:
                    if pixel_array[x][y].color == black and pixel_array[x][y + 1].color == black and pixel_array[x - 1][y + 1].color == white:
                        pixel_array[x - 1][y + 1].color = black
                        pixel_array[x][y].color = white
                    if pixel_array[x][y].color == black and pixel_array[x][y + 1].color == black and pixel_array[x - 1][y + 1].color == black and pixel_array[x + 1][y + 1].color == white:
                        pixel_array[x + 1][y + 1].color = black
                        pixel_array[x][y].color = white
    pygame.display.flip()
    fpsClock.tick(FPS)
