class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.1416*(self.radius**2)
R = int(input("Radius:"))
circle = Circle(R)
print(circle.area())