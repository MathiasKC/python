import random
import pygame
import math
width, height = 500, 500
r = 10
cols = math.floor(width/r)
rows = math.floor(height/r)
white = (255, 255, 255)
black = (0, 0, 0)

class Grid:

    def __init__(self, i, j, screen):
        self.i = i
        self.j = j
        self.color = white
        self.screen = screen

    def draw(self):
        x = self.i * r
        y = self.j * r
        pygame.draw.rect(self.screen, self.color, pygame.Rect(x, y, r, r))

    def check_neighbors(self, grid):
        top = grid[index(self.i, self.j-1)]
        right = grid[index(self.i + 1, self.j)]
        bottom = grid[index(self.i, self.j + 1)]
        left = grid[index(self.i - 1, self.j)]





def index(i,j):
    if i < 0 or j < 0 or i > cols-1 or j > rows-1:
        return -1;
    else:
        return i + j * cols;
