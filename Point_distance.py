import math


class Point2D:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f'Point [x= {self.x}, y= {self.y}]'


class Point3D:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def __str__(self):
        return f'Point [x= {self.x}, y= {self.y}, z= {self.z}]'


def distance2d(p1: Point2D, p2: Point2D) -> float:
    return math.sqrt(abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2)


def distance3d(p1: Point3D, p2: Point3D) -> float:
    return math.sqrt(abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2 + abs(p1.z - p2.z) ** 2)


point2d1 = Point2D(1, 1)
point2d2 = Point2D(2, 2)
point3d1 = Point3D(34, 76, 24)
point3d2 = Point3D(87, 12, 6)

print(point2d1)
print(point2d2)
print(f'Distance = {distance2d(point2d1, point2d2)}')

print(point3d1)
print(point3d2)
print(f'Distance = {distance3d(point3d1, point3d2)}')
