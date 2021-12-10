import pygame, sys

#window and background
size = width, height = 600, 400
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
r = 10;

class Cell:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


    def draw(self):
        top = pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.r, self.y))
        right = pygame.draw.line(screen, white, (self.x + self.r, self.y), (self.x + self.r, self.y + self.r))
        bottom = pygame.draw.line(screen, white, (self.x + self.r, self.y + self.r), (self.x, self.y + self.r))
        left = pygame.draw.line(screen, white, (self.x, self.y + self.r), (self.x, self.y))


cell = Cell(0, 0, r)

while True:
    #exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #fill screen
    screen.fill(black)
    #draw
    cell.draw()
    #update
    pygame.display.flip()
