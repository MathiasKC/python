import random
import pygame

height = 400
width = 600

class Grid:
    def __init__(self, x, y, r, screen, color):
        self.x = x
        self.y = y
        self.r = r
        self.screen = screen
        self.color = color
        rand = random.randrange(10)
        self.type = False
        if rand < 4:
            self.type = True




    def draw(self):
        top = pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x + self.r, self.y))
        right = pygame.draw.line(self.screen, self.color, (self.x + self.r, self.y), (self.x + self.r, self.y + self.r))
        bottom = pygame.draw.line(self.screen, self.color, (self.x + self.r, self.y + self.r), (self.x, self.y + self.r))
        left = pygame.draw.line(self.screen, self.color, (self.x, self.y + self.r), (self.x, self.y))

    def update(self):
        if self.type:
            self.x = width / 2
            self.y = 0
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.r, self.r))
