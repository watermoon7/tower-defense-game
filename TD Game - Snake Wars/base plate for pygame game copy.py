import pygame, sys
from colours import *
pygame.init()

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W has been pressed")


    screen.fill(WHITE)
    rect1 = pygame.draw.rect(screen,BLUE,(100, 200, 50, 50))
    
    pygame.display.update()
