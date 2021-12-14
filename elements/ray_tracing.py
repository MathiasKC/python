import pygame
import sys
import random
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
FPS = 40
grey = 50, 50, 50
white = 255, 255, 255
red = 255, 0, 0
r = 50
cols = int(height/r)
rows = int(width/r)
map = []
walls = []

class Cell:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.i = i * r
        self.j = j * r
        self.current = False
        self.state = 0
        self.closest = None

    def draw_map(self):
        if self.state == 1:
            pygame.draw.rect(screen, white, [self.i, self.j, r, r])

    def trace(self):
        if self.closest != None and self.current == True:
            pygame.draw.rect(screen, red, [self.i, self.closest / r, r, r * self.closest])


    def get_closest(self):
        if self.closest == None:
             for y in range(cols):
                 if y != self.y:
                     saved = walls[self.x][y].state
                     if saved == 1 and y < self.y:
                         if y == 0:
                             y = 0.5
                         nearest_y = y

                         self.closest = nearest_y



#SETUP
for i in range(cols):
    map_rows = []
    for j in range(rows):
        rand = random.randrange(10)
        value = 0
        if rand <= 2:
            value = 1
        map_rows.append(value)
    map.append(map_rows)

for i in range(cols):
    wall_rows = []
    for j in range(rows):
        wall_rows.append(Cell(i, j))
    walls.append(wall_rows)

for x in range(cols):
    for y in range(rows):
        if map[x][y] == 0:
            walls[y][x].state = 0
        if map[x][y] == 1:
            walls[y][x].state = 1

for x in range(rows):
    for y in range(cols):
        walls[x][y].draw_map()
for x in range(rows):
    print(map[x])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            walls[int(x/r)][int(y/r)].current = True
            print(walls[int(x/r)][int(y/r)].closest)
            print(x/r, y/r)



    screen.fill(grey)

    for x in range(rows):
        for y in range(cols):
            #walls[x][y].draw_map()
            walls[x][y].get_closest()
            walls[x][y].trace()

    pygame.display.flip()
    fpsClock.tick(FPS)
