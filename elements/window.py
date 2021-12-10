import pygame, sys

#window and background
size = width, height = 600, 400
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

while True:
    #exit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #fill screen
    screen.fill(black)
    #draw
    pygame.draw.line(screen, white, (0, 0), (240, 250))
    #update
    pygame.display.flip()
