import pygame, sys
import math
import random
size = width, height = 500, 500
grey = 55, 55, 55
white = 255, 255, 255
green = 0, 255, 0
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()
r = 20
class Pixel:
    def __init__(self, i, j):
        self.i = i * r
        self.j = j * r
        self.color = green
        self.moving = False


    def draw(self):
        pygame.draw.rect(screen, self.color, [self.i, self.j, r, r])

class Generator:
    def __init__(self):
        self.array = []

    def draw_map(self):
        for i in range(width):
            for j in range(height):
                self.array.append(Pixel(i, j))

    def draw(self):
        for pix in self.array:
            pix.draw()

gen = Generator()
gen.draw_map()
pixel = Pixel(1, 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    gen.draw()
    pygame.display.flip()
    fpsClock.tick(FPS)
