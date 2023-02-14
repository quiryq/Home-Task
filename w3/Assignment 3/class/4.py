import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return f"First point: ({self.x}, {self.y})"
    def move(self, x1, y1):
        self.x += x1
        self.y += y1
        return f"Second point: ({self.x}, {self.y})"
    def dist(self, x2, y2):
        xd = abs(self.x - x2)
        yd = abs(self.y - y2)
        return "Distance between points: " + str(math.sqrt(xd**2 + yd**2))
point = Point(int(input("X coordinate: ")), int(input("Y coordinate: ")))
print(point.show())
print(point.move(int(input("Second X-point: ")), int(input("Second Y-point: "))))
print(point.dist(int(input("Coordinates of the next point on the X-axis: ")), int(input("Coordinates of the next point on the Y-axis: "))))