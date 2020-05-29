'''
4.	Write a program to implement operator overloading in python.
'''
'''
We can extend plus operator functionality for our own objects using operator overloading concepts.
 In our example,we have defined __add__ magic method.
 If we apply + operator for b1 and b2, Book class corrosponding magic
 method will be executed.The return value of the magic method
 will be the output of b1 + b2
'''

class Book:

    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
         result =self.pages + other.pages
         b=Book(result)
         return b

    def __mul__(self, other):
        result= self.pages * other.pages
        return Book(result)

    def __sub__(self, other):
        result = self.pages - other.pages
        return Book(result)

    def __floordiv__(self, other):
        result =self.pages // other.pages
        return Book(result)

    def __str__(self):
        return f"Result is = {str(self.pages)}"



b1=Book(600)
b2=Book(1)
b3=Book(200)
print(b1+b2+b3)
print(b1*b2*b3)
print(b1-b2-b3)
print(b1//b2//b3)