import pygame, sys
import math
import random
size = width, height = 500, 500
r = 10
cols = int(height/r)
rows = int(width/r)
#colors, elements
sand = 255, 255, 0
white = 255, 255, 255
water = 0, 0, 255
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()
pressed = False
liquid = False

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
        pixel_array[int(x / r)][int(y/r)].color = sand

    if liquid:
        x, y = pygame.mouse.get_pos()
        print(x / r, y / r)
        pixel_array[int(x / r)][int(y/r)].color = water

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pressed = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            liquid = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                liquid = False


    screen.fill(white)
    for x in range(cols):
        for y in range(rows):
            pixel_array[x][y].draw()
    for x in range(cols):
        for y in range(rows):
            if y < cols - 1:
                #SAND PHYSICS
                if pixel_array[x][y].color == sand and pixel_array[x][y + 1].color == white:
                    pixel_array[x][y + 1].color = sand
                    pixel_array[x][y].color = white

                if x < rows - 1:
                    if pixel_array[x][y].color == sand and pixel_array[x][y + 1].color == sand and pixel_array[x - 1][y + 1].color == white:
                        pixel_array[x - 1][y + 1].color = sand
                        pixel_array[x][y].color = white

                    if pixel_array[x][y].color == sand and pixel_array[x][y + 1].color == sand and pixel_array[x - 1][y + 1].color == sand and pixel_array[x + 1][y + 1].color == white:
                        pixel_array[x + 1][y + 1].color = sand
                        pixel_array[x][y].color = white

                #WATER PHISICS
                #falling
                if pixel_array[x][y].color == water and pixel_array[x][y + 1].color == white:
                    pixel_array[x][y + 1].color = water
                    pixel_array[x][y].color = white
                if x < rows - 1:

                    #check left down - sand
                    if pixel_array[x][y].color == water and pixel_array[x][y + 1].color == sand and pixel_array[x - 1][y + 1].color == white:
                        pixel_array[x - 1][y + 1].color = water
                        pixel_array[x][y].color = white

                    #check right down
                    if pixel_array[x][y].color == water and pixel_array[x + 1][y + 1].color == white:
                        pixel_array[x + 1][y + 1].color = water
                        pixel_array[x][y].color = white


                    #check for white block on the left
                    if pixel_array[x][y].color == water and pixel_array[x - 1][y].color == white:
                        pixel_array[x - 1][y].color = water
                        pixel_array[x][y].color = white



            #water lighter than sand
            if pixel_array[x][y].color == water and pixel_array[x][y - 1].color == sand:
                pixel_array[x][y - 1].color = water
                pixel_array[x][y].color = sand





    pygame.display.flip()
    fpsClock.tick(FPS)
