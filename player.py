import pygame
from structures import Point
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.pos = Point(x,y)
        self.dir_x = None
        self.dir_y = None
        self.speed = 1

    def move(self):
        if self.dir_y == "w":
            self.pos.y -= self.speed
        elif self.dir_y == "s":
            self.pos.y += self.speed
        if self.dir_x == "a":
            self.pos.x -= self.speed
        elif self.dir_x == "d":
            self.pos.x += self.speed
        if self.pos.x <= 0:
            self.pos.x = 795
        if self.pos.x >= 800:
            self.pos.x = 5
        if self.pos.y <= 0:
            self.pos.y = 795
        if self.pos.y >= 800:
            self.pos.y = 5