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
FPS = 30
fpsClock = pygame.time.Clock()

pixel_array = []

class Pixel:
    def __init__(self, x, y, array):
        self.x = x
        self.y = y
        self.type = 'air'
        self.color = None
        self.array = array
        self.fallingSpeed = 1
        self.updated = False
        self.updateCount = 0
        #neighbors--
        self.top = None
        self.right = None
        self.bottom = None
        self.left = None



    def refreshMaterial(self):
        if self.updated == True and self.updateCount > 0:
            self.updated = False
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
        self.applyForce()
        self.refreshMaterial()
        self.draw()


    def applyForce(self):
        #ignore air material for efficiency
        if self.type != 'air' and self.updated != True:

            #-- sand physics --
            if self.bottom != None and self.type == 'sand' and self.bottom.type == 'air':
                # print(int(self.x / r),int((self.y / r) + 1))
                # print("check")
                # if self.bottom != None and self.bottom.type == 'air':
                self.bottom.type = 'sand'
                self.bottom.updated = True
                self.bottom.updateCount += 1
                self.type = 'air'

                print("done")



    def getIndex(self):
        for x in range(cols):
            for y in range(rows):
                if self == self.array[x][y]:
                    print("Exists")
                    print("self :",x, y)



    def getNeighbors(self):
        print("x:",self.x, "y:",self.y)
        if self.y > 0:
            self.top = self.array[int(self.x / r)][int((self.y - 1) / r)]
        if self.y == 0:
            self.top = None
        if self.y < height - r:
            self.bottom = self.array[int(self.x / r)][int(self.y / r) + 1]
        if self.y == height - r:
            self.bottom = None
        if self.x > 0:
            self.left = self.array[int((self.x - 1)/ r)][int(self.y / r)]
        if self.x == 0:
            self.left = None
        if self.x < width - r:
            self.right = self.array[int(self.x / r) + 1][int(self.y / r)]
        if self.x == width - r:
            self.right = None






    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, r, r])

for i in range(cols):
    pixel_rows = []
    for j in range(rows):
        pixel_rows.append(Pixel(i*r, j*r, pixel_array))
    pixel_array.append(pixel_rows)

pixel_array[20][0].type = 'sand'
while True:
    pixel_array[20][0].type = 'sand'
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    for x in range(cols):
        for y in range(rows):
            pixel_array[x][y].update()
    fpsClock.tick(FPS)
    pygame.display.flip()
