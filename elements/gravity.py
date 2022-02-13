import pygame, sys
import math
import random
size = width, height = 500, 500
r = 10
cols = int(height/r)
rows = int(width/r)
grey = 55, 55, 55
blue = 0, 0, 255
yellow = 255, 255, 0
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()

pixel_array = []

class Pixel:
    def __init__(self, x, y, array):
        self.x = x
        self.y = y
        self.type = 'sand'
        self.color = None
        self.array = array
        #neighbors--
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None


    def setMaterial(self):
        if self.type == 'sand':
            self.color = yellow

        if self.type == 'air':
            self.color = grey

        if self.type == 'water':
            self.color = blue

    def update(self):
        self.setMaterial()
        self.getNeighbors()
        #apply physics
        self.draw()


    def getNeighbors(self):
        if self.y > 0:
            self.top = self.array[int(self.x / 10)][int((self.y - 1) / 10)]
        if self.y == 0:
            self.top = None
        if self.y < height:
            self.bottom = self.array[int(self.x / 10)][int((self.y + 1) / 10)]
        if self.y == height:
            self.bottom = None
        if self.x > 0:
            self.left = self.array[int((self.x - 1)/ 10)][int(self.y / 10)]
        if self.x == 0:
            self.left = None
        if self.x < width:
            self.right = self.array[int((self.x + 1) / 10)][int(self.y / 10)]
        if self.x == width:
            self.right = None






    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, r, r])

for i in range(cols):
    pixel_rows = []
    for j in range(rows):
        pixel_rows.append(Pixel(i*r, j*r, pixel_array))
    pixel_array.append(pixel_rows)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    for x in range(cols):
        for y in range(rows):
            pixel_array[x][y].update()
    pygame.display.flip()
    fpsClock.tick(FPS)
