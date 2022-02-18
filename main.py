from line import Line
from structures import Point
from maps import Map
from player import Player
import pygame
import numpy as np
import sys



pygame.init()
screen = pygame.display.set_mode((1600, 800))

# set map size
HEIGHT = 800
WIDTH = 800

# create random borders
borders = Map(HEIGHT, WIDTH)
borders.generate_maze(10)

#set start position
player = Player(400,400)
mouse_pos = Point(400, 400)

R = 800
key = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # get mouse move event
        if event.type == 1024:
            mouse_pos.x = pygame.mouse.get_pos()[0] if pygame.mouse.get_pos()[0] < 800 else 800 
            mouse_pos.y = pygame.mouse.get_pos()[1]
            mouse_pos.x, mouse_pos.y = mouse_pos.x - player.pos.x, mouse_pos.y - player.pos.y

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.dir_y = "s"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.dir_y = "w"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.dir_x = "a"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.dir_x = "d"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.dir_y = None
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.dir_y = None
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.dir_x = None
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.dir_x = None

    screen.fill((0, 0, 0))

    current_direction = player.current_direction(mouse_pos)
    x, y = player.pos.x, player.pos.y
    # for 3D visualisation in "deg" degrees
    deg = 90
    step = 2

    scene = np.zeros(deg)
    angles = [i if i < 360 else i - 360 for i in range(current_direction-deg//2, current_direction+deg//2,step)]
    
    # draw game map and rays
    for i , angle in enumerate(angles):
        dx, dy = R*np.sin(angle*np.pi/180), R*np.cos(angle*np.pi/180)
        line = Line(Point(x, y), Point(x+dx, y+dy))
        distance = np.Infinity
        point_to_draw = Point(x,y)

        for border in borders.borders:
            #  draw borders
            pygame.draw.line(screen, (255,255,255), (border.start.x, border.start.y), (border.end.x, border.end.y))
            
            #find intersection point
            dot = line.intersection(border)
            if dot:
                r = np.sqrt((dot.x - x)**2 + (dot.y - y)**2)
                if r < distance:
                    distance = min(distance, r)
                    point_to_draw = dot
        # draw rays on game map
        pygame.draw.line(screen, (255,255,255), (x,y), (point_to_draw.x, point_to_draw.y))
        
        # trying to decrease fisheye effects
        distance *= abs(np.cos((angle-current_direction)//2*np.pi/180))
        scene[i] = distance

    width_step = 800/deg*step
    

    # draw game 3D scene
    for i , intense in enumerate(scene):
        mult = 0.5
        scalar = 0.5
        c = 255/intense**mult if 255/intense**mult < 255 else 255 

        heigth = 800 /( scalar*(intense**mult))
        heigth_start = (800 - heigth)/2
        r = pygame.Rect(800+i*width_step, heigth_start, width_step, heigth)    
        pygame.draw.rect(screen, (c,c,c), r)
    
    player.move(current_direction)       
    pygame.display.flip()


