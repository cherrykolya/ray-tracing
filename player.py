import pygame
from structures import Point
import numpy as np
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.pos = Point(x,y)
        self.dir_x = None
        self.dir_y = None
        self.speed = 2

    def move(self, current_direction):
        """
        current_direction - angle between current direction and direction on south
        """
        x = np.cos(np.deg2rad(current_direction-90)) * self.speed
        y = np.cos(np.deg2rad(current_direction)) * self.speed
        
        if self.dir_y == "w":
            self.pos.y += y
            self.pos.x += x 
        elif self.dir_y == "s":
            self.pos.y -= y
            self.pos.x -= x 
        if self.dir_x == "d":
            self.pos.y += x
            self.pos.x += -y 
        elif self.dir_x == "a":
            self.pos.y -= x
            self.pos.x -= -y 
        if self.pos.x <= 0:
            self.pos.x = 795
        if self.pos.x >= 800:
            self.pos.x = 5
        if self.pos.y <= 0:
            self.pos.y = 795
        if self.pos.y >= 800:
            self.pos.y = 5
    
    def current_direction(self, mouse_pos: Point):
        norm = np.sqrt(mouse_pos.x**2 + mouse_pos.y**2)
        normed_x = mouse_pos.x/norm
        normed_y = mouse_pos.y/norm
        return int(np.angle(complex(normed_x, -normed_y), deg = True) +90) 