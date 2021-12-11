import random
import pygame
import math
width, height = 500, 500
r = 25
cols = math.floor(width/r)
rows = math.floor(height/r)
white = (255, 255, 255)
black = (0, 0, 0)

class Grid:

    def __init__(self, i, j, screen):
        self.i = i
        self.j = j
        self.screen = screen
        self.type = False
        self.color = white
        self.next_move = pygame.time.get_ticks() + 100

    def draw(self):
        x = self.i * r
        y = self.j * r
        pygame.draw.rect(self.screen, self.color, pygame.Rect(x, y, r, r))




    def update(self, grid):
        if pygame.time.get_ticks() >= self.next_move:
            self.next_move = pygame.time.get_ticks() + 100 # 100ms = 0.1s
            top = grid[index(self.i, self.j - 1)]
            right = grid[index(self.i + 1, self.j)]
            bottom = grid[index(self.i, self.j + 1)]
            left = grid[index(self.i - 1, self.j)]
            if self.type == True:
                bottom.color = black
                right.color = black






def index(i,j):
    if i < 0 or j < 0 or i > cols-1 or j > rows-1:
        return -1;
    else:
        return i + j * cols;
