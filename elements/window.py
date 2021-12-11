import pygame, sys
from grid import Grid
import math

#window and background
size = width, height = 500, 500
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
r = 25
grid = []
# frames per second setting
FPS = 10
fpsClock = pygame.time.Clock()

cols = math.floor(width/r)
rows = math.floor(height/r)

for j in range(rows):
    for i in range(cols):
        grid.append(Grid(i, j, screen))

#setup:
grid[0].type = True
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
    for cell in grid:
        cell.draw()
        cell.update(grid)

    #update

    pygame.display.flip()
    fpsClock.tick(FPS)
