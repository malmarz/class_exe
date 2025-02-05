import math

class Circle:
  def __init__(self, radius):
    self.radius = radius
  def show_radius(self):
    print(self.radius)
  def calc_area(self):
    print(math.pi * (self.radius ** 2))


circle = Circle(5)
circle.calc_area()
