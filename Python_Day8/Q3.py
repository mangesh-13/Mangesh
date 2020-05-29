'''
3.	Write a program to implement multiple inheritance.
'''

# Multiple parents but single child

class A1:
    def m1(self):
        print("A1 method")

class A2:
    def m1(self):
        print("A2 method")

class B(A1,A2):pass
b=B()
b.m1()

