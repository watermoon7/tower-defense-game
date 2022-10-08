import pygame
pygame.init()

class Tower():

    def __init__(self, range, cost, damage):
        self.range = range
        self.cost = cost
        self.damage = damage

    def stats(self):
        print(self.range)
        print(self.cost)
        print(self.damage)