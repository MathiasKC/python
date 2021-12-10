
import pygame

class Grid:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


    def draw(self, screen, color):
        top = pygame.draw.line(screen, color, (self.x, self.y), (self.x + self.r, self.y))
        right = pygame.draw.line(screen, color, (self.x + self.r, self.y), (self.x + self.r, self.y + self.r))
        bottom = pygame.draw.line(screen, color, (self.x + self.r, self.y + self.r), (self.x, self.y + self.r))
        left = pygame.draw.line(screen, color, (self.x, self.y + self.r), (self.x, self.y))
