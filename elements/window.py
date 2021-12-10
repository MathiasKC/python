import pygame, sys
from grid import Grid


#window and background
size = width, height = 600, 400
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
r = 10;
grid_array = []


#setup:

for x in range(0, width, r):
    for y in range(0, height, r):
        grid_array.append(Grid(x, y, r))

#main loop
while True:
    #exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #fill screen
    screen.fill(black)
    #draw

    for grid in grid_array:
        grid.draw(screen, white)
    #update
    pygame.display.flip()
