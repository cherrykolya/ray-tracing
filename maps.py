from line import Line
from structures import Point, Cell
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

    def generate_maze(self, n: int):
        RES = WIDTH, HEIGHT = self.WIDTH, self.HEIGHT
        
        cols, rows = n, n
        Cell.cols, Cell.rows = n, n

        TILE = WIDTH // cols

        grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        
        current_cell = grid_cells[0]
        stack = [1]
        colors, color = [], 40

        while len(stack) != 0:
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(grid_cells)
            if next_cell:
                next_cell.visited = True
                stack.append(current_cell)
                colors.append((min(color, 255), 10, 100))
                color += 1
                Cell.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif stack:
                current_cell = stack.pop()
    
        for cell in grid_cells:
            if cell.walls['top']:
                l = Line(Point(cell.x*TILE, cell.y*TILE), Point(cell.x*TILE + TILE, cell.y*TILE))
                if l not in self.borders:
                    self.borders.append(l)
            if cell.walls['right']:
                l = Line(Point(cell.x*TILE + TILE, cell.y*TILE), Point(cell.x*TILE + TILE, cell.y*TILE + TILE))
                if l not in self.borders:
                    self.borders.append(l)
            if cell.walls['bottom']:
                l = Line(Point(cell.x*TILE + TILE, cell.y*TILE + TILE), Point(cell.x*TILE , cell.y*TILE + TILE))
                if l not in self.borders:
                    self.borders.append(l)
            if cell.walls['left']:
                l = Line(Point(cell.x*TILE, cell.y*TILE + TILE), Point(cell.x*TILE, cell.y*TILE))
                if l not in self.borders:
                    self.borders.append(l)

