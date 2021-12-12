import pygame, sys
import math

import random
#window and background
size = width, height = 100, 100
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

# frames per second setting
FPS = 30
fpsClock = pygame.time.Clock()
r = 10
cols = math.floor(width/r)
rows = math.floor(height/r)
grid_array = []

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, white, pygame.Rect(self.x, self.y, r, r))
print(cols, rows)
for x in range(cols):
    col = []
    for y in range(rows):
        col.append(Grid(y, x))
    grid_array.append(col)



class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = white

    def draw(self):
        x = self.x * r
        y = self.y * r
        pygame.draw.rect(self.screen, self.color, pygame.Rect(x, y, r, r))
#setup:




#events



#main loop
while True:
    #exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #mouse click


    #fill screen
    screen.fill(black)

    #draw

    grid_array[1][5].draw()


    #update

    pygame.display.flip()
    fpsClock.tick(FPS)
