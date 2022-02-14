import pygame, sys
import math
import random
pygame.init()
size = width, height = 600, 600
r = 5
cols = int(height/r)
rows = int(width/r)
grey = 55, 55, 55
blue = 0, 0, 255
yellow = 255, 255, 0
pressed = False
screen = pygame.display.set_mode(size)
FPS = 120
fpsClock = pygame.time.Clock()
pixel_array = []


def Render_Text(what, color, where):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)


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
        self.state = 'stationary'
        #neighbors--
        self.top = None
        self.right = None
        self.bottomRight = None
        self.bottom = None
        self.left = None
        self.bottomLeft = None


    def refreshState(self):
        #for updating the state of element
        if self.updated == True and self.updateCount > 0:
            self.updated = False
            self.updateCount = 0


    def setMaterial(self):
        if self.type == 'sand':
            self.color = yellow

        if self.type == 'air':
            self.color = grey

        if self.type == 'water':
            self.color = blue

    def getState(self):
        if self.state == 'stationary':
            return False
        elif self.state == 'moving':
            return True

    def update(self):
        if self.type != 'air':
            self.setMaterial()
            self.getNeighbors()
            self.applyForce()
            self.setMaterial()
            self.refreshState()
            self.draw()


    def applyForce(self):
        #ignore air material for efficiency
        if self.type != 'air' and self.updated != True:

            #-- sand physics --
            if self.bottom != None and self.type == 'sand' and self.bottom.type == 'air':
                self.bottom.type = 'sand'
                self.bottom.updated = True
                self.bottom.updateCount += 1
                self.type = 'air'

    #For debugging
    def getIndex(self):
        for x in range(cols):
            for y in range(rows):
                if self == self.array[x][y]:
                    print("Exists")
                    print("self :",x, y)

    #getting neighbors if exists and storing them in self
    def getNeighbors(self):
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


while True:
    #mouse click changes air to selected material
    if pressed:
        x, y = pygame.mouse.get_pos()
        pixel_array[int(x / r)][int(y/r)].type = 'sand'
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        pressed = True
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            pressed = False
    screen.fill(grey)
    for x in range(cols):
        for y in range(rows):
            pixel_array[x][y].update()
    fpsClock.tick(FPS)
    Render_Text(str(int(fpsClock.get_fps())), (255,0,0), (0,0))
    pygame.display.flip()
