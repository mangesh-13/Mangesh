'''
2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
'''
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        self.area= math.pi*self.radius*self.radius
        print("Area of the circle is:",round(self.area))

    def Perimeter(self):
        self.perimeter=2*math.pi*self.radius
        print("Perimeter of the circle is:",round(self.perimeter))

    def display(self):
        self.Area()
        self.Perimeter()

radius=int(input("Enter radius of the circle:"))
c=Circle(radius)
c.display()