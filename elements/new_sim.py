import pygame, sys
import math
import random

size = width, height = 500, 500
grey = 55, 55, 55
white = 255, 255, 255
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()

class Pixel:
    def __init__(self):
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        self.color = white
        self.xx, self.yy = None, None


    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, 5, 5])

    def look_for(self, array):
        closest = 1000
        closest_item = None
        for element in range(len(array)):
            d = math.sqrt((array[element].x - self.x)**2 + (array[element].y - self.y)**2)
            if d == 0.0:
                continue
            actual = array[element]
            if d < closest:
                closest = d
                closest_item = array[element]
                
        if closest_item != None:
            self.xx, self.yy = closest_item.x, closest_item.y




    def update(self):
        if self.xx != None and self.yy != None:
            self.move_to(self.xx, self.yy)

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
fill_array(2, pixel_array)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    for i in range(len(pixel_array)):
        pixel_array[i].draw()
        pixel_array[i].look_for(pixel_array)
        pixel_array[i].update()
    pygame.display.flip()
    fpsClock.tick(FPS)
