#Task 5: Extending a Class
import math

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"Point({self.x}, {self.y})"

  def __eq__(self, other):
    return (self.x, self.y) == (other.x, other.y)
  
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
  
  def euclidean(self, other):
    x_distance = self.x - other.x
    y_distance = self.y - other.y
    return math.sqrt((x_distance**2) + (y_distance**2))
  
class Vector(Point):
  def __init__(self, x, y):
    super().__init__(x, y)

  def __repr__(self):
    return f"Vector<{self.x}, {self.y}>"
  
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  


point_a = Point(0, 0)
point_b = Point(2, 2)
point_c = Point(0, 0)
point_d = Point(5, 6)
point_e = point_b + point_d
print(point_a)
print(point_a == point_b)
print(point_a == point_c)
print(point_a.euclidean(point_b))
print(point_e)

vector_a = Vector(4, 5)
vector_b = Vector(1, 1)
vector_c = Vector(4, 5)
print(vector_a)
print(vector_a == vector_b)
print(vector_a == vector_c)
print(vector_a + vector_b)
