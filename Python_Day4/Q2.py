'''2.	Write a Python program to detect the number of local variables declared in a function.'''
def f():
    a,b=10,30
    string="Welcome to world"
def f1():
    pass


print(f.__code__.co_nlocals)
print(f1.__code__.co_nlocals)