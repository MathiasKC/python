import pygame, sys
import math
import random
size = width, height = 500, 500
grey = 55, 55, 55
screen = pygame.display.set_mode(size)
FPS = 40
fpsClock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    pygame.display.flip()
    fpsClock.tick(FPS)
