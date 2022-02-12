import pygame, sys
import math
import random

size = width, height = 500, 500
grey = 55, 55, 55
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()



resources_number = 1


class Resource:
    def __init__(self):
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        self.color = green
        self.TYPE = None
        self.stock = 100
        self.r = 50

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.r, self.r])






class Pixel:
    def __init__(self):
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        self.homeX = random.randrange(width)
        self.homeY = random.randrange(width)
        self.color = white
        self.distance = None
        self.xx, self.yy = None, None
        self.reach = 300
        self.type = None
        self.center_d = None
        self.filled = False


    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, 5, 5])

    #find distance and item in array
    def look_for(self, array):
        closest = 1000
        closest_item = None
        for element in range(len(array)):
            d = math.sqrt((array[element].x - self.x)**2 + (array[element].y - self.y)**2)
            if d == 0.0:
                continue
            self.distance = d
            actual = array[element]
            if d < closest:
                closest = d
                closest_item = array[element]

        if closest_item != None:
            #get center of item
            self.xx, self.yy = closest_item.x + array[element].r / 2, closest_item.y + array[element].r / 2

    #random movement - to improve
    def wander(self):
        rand = random.randint(1, 100)
        if rand < 50:
            self.x += 1
        elif rand > 50:
            self.x -= 1
        rand = random.randint(1, 100)
        if rand < 50:
            self.y += 1
        elif rand > 50:
            self.y -= 1


    def update(self):
        if self.distance < self.reach:

            if self.xx != None and self.yy != None and self.filled == False:
                self.move_to(self.xx, self.yy)

            if self.x == self.xx and self.y == self.yy:
                self.filled = True

            if self.filled:
                self.move_to(self.homeX, self.homeY)
                if self.x == self.homeX and self.y == self.homeY:
                    self.filled = False

        else:
            self.wander()


    def move_to(self, x, y):
            if x > self.x:
                self.x += 1
            if x < self.x:
                self.x -= 1

            if y > self.y:
                self.y += 1
            if y < self.y:
                self.y -= 1



def fill_array(number, array):
    for x in range(number):
        array.append(Pixel())

pixel_array = []
resource_array = []
for i in range(resources_number):
    resource_array.append(Resource())



fill_array(10, pixel_array)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    for i in range(len(resource_array)):
        resource_array[i].draw()
    for i in range(len(pixel_array)):
        pixel_array[i].draw()
        pixel_array[i].look_for(resource_array)
        pixel_array[i].update()
    pygame.display.flip()
    fpsClock.tick(FPS)
