'''
3. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints:
To override a method in super class, we can define a method with the same name in the super class.
'''

class Shape:

    def area(self):
        self.area=0
        print(self.area)


class square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        self.area=self.length**2
        print("Area of square is:",self.area)


length=int(input("Enter length:"))
s=square(length)
s.area()








