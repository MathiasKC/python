import random
import pygame
import math

height = 400
width = 400


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

    def set_mode(self):
        if self.type:
            self.x = width / 2
            self.y = 0



    def check_neighbors(self, grid_array):
        if self.index(self.x, self.y) > len(grid_array):
            return
        top = grid_array[self.index(self.x, self.y - 1)]
        right = grid_array[self.index(self.x + 1, self.y)]
        bottom = grid_array[self.index(self.x, self.y + 1)]
        left = grid_array[self.index(self.x - 1, self.y)]
        #print("TOP=",top,"RIGHT=", right, "LEFT=", left, "BOTTOM=", bottom)



    def update(self):
        if self.type:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.r, self.r))


    def index(self, x, y):
        if x < 0 or y < 0 or x > (width/self.r) - 1 or y > (height / self.r) - 1:
            return -1
        return int(x + y * width/self.r)
