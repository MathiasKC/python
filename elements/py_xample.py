import pygame, sys
import math
import random
size = width, height = 500, 500
grey = 55, 55, 55
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()



class Pixel:
    def __init__(self):
        self.x = width / 2
        self.y = 0
        self.isFalling = None
        self.type = 'sand'

    def behavior(self):
        if self.type == 'sand':
            self.y += 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    pygame.display.flip()
    fpsClock.tick(FPS)
