from line import Line
from structures import Point
import pygame
import numpy as np
import sys

pygame.init()

screen = pygame.display.set_mode((1200, 800))

angles = [i for i in range(0,361,5)]

# create random borders
borders = []
for i in range(5):
    x1 = np.random.randint(0,1200)
    x2 = np.random.randint(0,1200)
    y1 = np.random.randint(0,800)
    y2 = np.random.randint(0,800)
    borders.append(Line(Point(x1, y1), Point(x2, y2)))

R = 1200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # get mouse move event
        if event.type == 1024:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            screen.fill((0, 0, 0))
    
    # main cycle of the game loop
    for angle in angles:
        dx = R*np.sin(angle*np.pi/180)
        dy = R*np.cos(angle*np.pi/180)
        line = Line(Point(x, y), Point(x+dx, y+dy))
        distance = np.Infinity
        point_to_draw = Point(x,y)
        
        for border in borders:
            #  draw borders
            pygame.draw.line(screen, (255,255,255), (border.start.x, border.start.y), (border.end.x, border.end.y))
            
            #find intersection point
            dot = line.intersection(border)
            if dot:
                r = np.sqrt((dot.x - x)**2 + (dot.y - y)**2)
                if r < distance:
                    distance = min(distance, r)
                    point_to_draw = dot

        pygame.draw.line(screen, (255,255,255), (x,y), (point_to_draw.x, point_to_draw.y))
            
    pygame.display.flip()
