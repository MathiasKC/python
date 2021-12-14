import pygame
import sys
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
FPS = 40
grey = 50, 50, 50
r = 50
cols = int(height/r)
rows = int(width/r)
walls = []

class Cell:
    def __init__(self, i, j):
        self.i = i * r
        self.j = j * r
        self.current = False
        
for i in range(cols):
    wall_rows = []
    for j in range(rows):
        wall_rows.append(Cell(i, j))
    walls.append(wall_rows)

for x in range(rows):
    print(walls[x])



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(grey)
    pygame.display.flip()
    fpsClock.tick(FPS)
