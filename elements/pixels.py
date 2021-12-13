import pygame, sys
import math
import random
size = width, height = 500, 500
r = 10
cols = int(height/r)
rows = int(width/r)

black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()
pressed = False

class Pixel:
    def __init__(self, i, j):
        self.i = i * r
        self.j = j * r
        self.color = white

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.i, self.j, r, r])


pixel_array = []


for i in range(cols):
    pixel_rows = []
    for j in range(rows):
        pixel_rows.append(Pixel(i, j))
    pixel_array.append(pixel_rows)


while True:
    if pressed:
        x, y = pygame.mouse.get_pos()
        print(x / r, y / r)
        pixel_array[int(x / r)][int(y/r)].color = black

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pressed = False

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
