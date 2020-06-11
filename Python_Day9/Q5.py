
'''
5.	Write a python program to decorate arithmetic operations.
'''
def decor(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@decor
def divide(a,b):
    print(a/b)

# divide=decor(divide)

divide(2,4)
divide(10,2)

