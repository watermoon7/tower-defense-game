import pygame
import sys
import random

from pygame import display
import TOWER_CLASS as TC
from colours import *
pygame.init()

SQ_SIZE = 60
moveList = []

track1 = [
        ['--','--','--','--','--','--','--','--','--','--','--','TT','TT','TT','--','--','--','--','--','--'],
        ['T1','TT','TT','--','--','--','--','--','--','--','--','TT','--','TT','TT','TT','TT','TT','TT','--'],
        ['--','--','TT','--','--','TT','TT','TT','--','--','--','TT','--','--','--','--','--','--','TT','--'],
        ['--','--','TT','--','--','TT','--','TT','--','--','--','TT','TT','--','--','--','--','--','TT','--'],
        ['--','TT','TT','--','--','TT','--','TT','--','--','--','--','TT','--','--','--','--','TT','TT','--'],
        ['--','TT','--','--','TT','TT','--','TT','--','--','--','--','TT','--','TT','TT','TT','TT','--','--'],
        ['TT','TT','--','--','TT','--','--','TT','--','--','--','TT','TT','--','TT','--','--','--','--','--'],
        ['TT','--','--','--','TT','--','--','TT','--','--','TT','TT','--','--','TT','--','--','TT','TT','TT'],
        ['TT','TT','TT','TT','TT','--','--','TT','TT','TT','TT','--','--','--','TT','TT','TT','TT','--','--'],
        ['--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--']
    ]

def reset():
    global track1
    enemy = random.randint(1, 5)
    print(enemy)
    track1 = [
        ['--','--','--','--','--','--','--','--','--','--','--','TT','TT','TT','--','--','--','--','--','--'],
        [f'T{enemy}','TT','TT','--','--','--','--','--','--','--','--','TT','--','TT','TT','TT','TT','TT','TT','--'],
        ['--','--','TT','--','--','TT','TT','TT','--','--','--','TT','--','--','--','--','--','--','TT','--'],
        ['--','--','TT','--','--','TT','--','TT','--','--','--','TT','TT','--','--','--','--','--','TT','--'],
        ['--','TT','TT','--','--','TT','--','TT','--','--','--','--','TT','--','--','--','--','TT','TT','--'],
        ['--','TT','--','--','TT','TT','--','TT','--','--','--','--','TT','--','TT','TT','TT','TT','--','--'],
        ['TT','TT','--','--','TT','--','--','TT','--','--','--','TT','TT','--','TT','--','--','--','--','--'],
        ['TT','--','--','--','TT','--','--','TT','--','--','TT','TT','--','--','TT','--','--','TT','TT','TT'],
        ['TT','TT','TT','TT','TT','--','--','TT','TT','TT','TT','--','--','--','TT','TT','TT','TT','--','--'],
        ['--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--','--']
    ]

def drawBoard(screen, track):
    global colors
    colors = [WHITE, YELLOW1]
    image = pygame.image.load("background2.png")
    screen.blit(image, (0, 0))
    for r in range(10):
        for c in range(20):
            if track[r][c][0] == 'T':
                image = pygame.image.load("track2.png")
                screen.blit(image, (SQ_SIZE*c, SQ_SIZE*r))
                #pygame.draw.rect(screen, GREEN3, pygame.Rect(SQ_SIZE*c, SQ_SIZE*r , SQ_SIZE, SQ_SIZE))
                #pygame.draw.rect(screen, GRAY49, pygame.Rect(SQ_SIZE*c, SQ_SIZE*r , SQ_SIZE, SQ_SIZE), 1)
                if track[r][c][1] == '1':
                    #pygame.draw.circle(screen, BLACK, (SQ_SIZE*c+30, SQ_SIZE*r+30), 20)
                    image = pygame.image.load("smallsnake.png")
                    screen.blit(image, (SQ_SIZE*c, SQ_SIZE*r))
                elif track[r][c][1] == '2':
                    pygame.draw.circle(screen, YELLOW1, (SQ_SIZE*c+30, SQ_SIZE*r+30), 20)
                elif track[r][c][1] == '3':
                    pygame.draw.circle(screen, GREEN, (SQ_SIZE*c+30, SQ_SIZE*r+30), 20)
                elif track[r][c][1] == '4':
                    pygame.draw.circle(screen, PINK, (SQ_SIZE*c+30, SQ_SIZE*r+30), 20)
                elif track[r][c][1] == '5':
                    pygame.draw.circle(screen, PURPLE, (SQ_SIZE*c+30, SQ_SIZE*r+30), 20)

def moveEnemy(screen):
    global moveList
    global track1
    for r in range(10):
        for c in range(20):
            if track1[r][c][0] == 'T':
                if track1[r][c][1] != 'T' and track1[r][c][1] != '0':
                    typeEnemy = track1[r][c][1]
                    directions = [1, -1]
                    try:
                        if track1[r+1][c] == 'TT':
                            track1[r][c] = 'T0'
                            track1[r+1][c] = f'T{typeEnemy}'
                            return ''
                        elif track1[r-1][c] == 'TT':
                            track1[r][c] = 'T0'
                            track1[r-1][c] = f'T{typeEnemy}'
                            return ''
                        elif track1[r][c+1] == 'TT':
                            track1[r][c] = 'T0'
                            track1[r][c+1] = f'T{typeEnemy}'
                            return ''
                        elif track1[r][c-1] == 'TT':
                            track1[r][c] = 'T0'
                            track1[r][c-1] = f'T{typeEnemy}'
                            return ''
                    except:
                        print("hello")
                        reset()
                        return ''
                        
                    
                    
def drawTrack(screen, track1):
    pass

screen = pygame.display.set_mode((1200, 600))
bigDuck = TC.Tower(1, 15, 1)
bigDuck.stats()
screen.fill(WHITE)
drawBoard(screen, track1)
display.flip()
num = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("W has been pressed")
    num += 1
    if num == 30:
        num = 0
        moveEnemy(screen)
    drawBoard(screen, track1)
    pygame.display.update()
