from structures import Point 
from typing import Optional


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
    
    def intersection(self, line) -> Optional[Point]:
        znam = (self.start.x - self.end.x)*(line.start.y - line.end.y) - (self.start.y - self.end.y)*(line.start.x - line.end.x)
        # (x1-x2)(y3-y4) - (y1-y2)(x3-x4)
        if znam == 0:
            return None
        else:
            numerator1 = (self.start.x - line.start.x)*(line.start.y - line.end.y) - (self.start.y - line.start.y)*(line.start.x - line.end.x) 
            # (x1-x3)(y3-y4) - (y1-y3)(x3-x4)
            numerator2 = (self.start.x - line.start.x)*(self.start.y - self.end.y) - (self.start.y - line.start.y)*(self.start.x - self.end.x)
            # (x1-x3)(y1-y2) - (y1-y3)(x1-x2)
            t = numerator1/znam
            u = numerator2/znam
            if t <= 1 and t >= 0 and u >= 0 and u <= 1:
                x = self.start.x + t*(self.end.x - self.start.x)
                y = self.start.y + t*(self.end.y - self.start.y)
                return Point(x, y)
            else: return None




