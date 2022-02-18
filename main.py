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
borders.create_random_walls(5)

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
    norm = np.sqrt(mouse_pos.x**2+mouse_pos.y**2)
    normed_x = mouse_pos.x/norm
    normed_y = mouse_pos.y/norm
    current_direction = int(np.angle(complex(normed_x, -normed_y), deg = True) +90) 
    
    x, y = player.pos.x, player.pos.y
    #print(x, y)
    pygame.draw.line(screen, (255,255,255), (800, 0), (800, 800))
    # for 3D visualisation in 40 degrees
    scene = np.zeros(40)

    angles = [i if i < 360 else i - 360 for i in range(current_direction-20,current_direction+20,1)]
    
    # draw game map
    for i , angle in enumerate(angles):
        dx = R*np.sin(angle*np.pi/180)
        dy = R*np.cos(angle*np.pi/180)
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
            #else:
            #    pygame.draw.line(screen, (255,255,255), (x,y), (x+dx, y+dy))
        pygame.draw.line(screen, (255,255,255), (x,y), (point_to_draw.x, point_to_draw.y))
        scene[i] = distance

    width_step = 800/40
    player.move(current_direction)
    # draw game scene
    for i , intense in enumerate(scene):
        mult = 0.2
        heigth = 800 / intense**mult
        heigth_start = (800 - heigth)/2
        r = pygame.Rect(800+i*width_step, heigth_start, width_step, heigth)
        c = 255/intense**mult if 255/intense**mult < 255 else 255 
        pygame.draw.rect(screen, (c,c,c), r)
            
    pygame.display.flip()


