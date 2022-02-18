from line import Line
from structures import Point
import numpy as np

class Map:
    """class for store and create gaming objects like walls and borders
    """
    def __init__(self, height:int, width:int):
        self.HEIGHT = height
        self.WIDTH = width
        self.borders = []
        self.create_boundary()

    def create_boundary(self):
        self.borders.append(Line(Point(0, 0), Point(self.WIDTH, 0)))
        self.borders.append(Line(Point(self.WIDTH, 0), Point(self.WIDTH, self.HEIGHT)))
        self.borders.append(Line(Point(self.WIDTH, self.HEIGHT), Point(0, self.HEIGHT)))
        self.borders.append(Line(Point(0, self.HEIGHT), Point(0, 0)))

    def create_random_walls(self, n:int):
        for _ in range(n):
            x1 = np.random.randint(0, self.WIDTH)
            x2 = np.random.randint(0, self.WIDTH)
            y1 = np.random.randint(0, self.HEIGHT)
            y2 = np.random.randint(0, self.HEIGHT)
            self.borders.append(Line(Point(x1, y1), Point(x2, y2)))
