import pygame, sys
import math
import random
size = width, height = 500, 500
grey = 55, 55, 55
blue = 30, 30, 200
white = 255, 255, 255
green = 255, 255, 0
cols = [blue, white, green]
screen = pygame.display.set_mode(size)
red = 255, 0 ,0
FPS = 40
fpsClock = pygame.time.Clock()

#CLASSES
class Biome:
    def __init__(self):
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.color = random.choice(cols)
        self.size = random.randint(40, 60)
        self.type = 1

    def draw_biomes(self):
        pygame.draw.circle(screen, red, (self.x, self.y), self.size)

#CLASSES
class Particle:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.r = 5
        self.vx = 1
        self.vy = 1
        self.type = 1
        self.searching = False

    def draw(self):
        pygame.draw.circle(screen, red, (self.x, self.y), self.r)

    def move(self, arr):
        if not self.searching:
            for i in range(len(arr)):
                if self.type == arr[i].type:
                    searching = True
                    x, y = arr[i].x, arr[i].y
        if self.searching:
            if self.x < x:
                self.x += self.vx
            else:
                self.x -= self.vx

            if self.y < y:
                self.y += self.vy
            else:
                self.y -= self.vy




#CLASSES

#DEFINITIONS
particles = []
biomes = []
for i in range(2):
    biomes.append(Biome())
for i in range(100):
    particles.append(Particle())



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(grey)
    for i in range(len(biomes)):
        biomes[i].draw_biomes()
    for i in range(len(particles)):
        particles[i].draw()
        particles[i].move(biomes)
    pygame.display.flip()
    fpsClock.tick(FPS)
