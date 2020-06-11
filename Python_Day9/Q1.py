'''
1.Write a function to compute divide by zero and use try/except to catch the exceptions.
'''

def divide(a,b):
    try:
        result = a/b
        print(result)
    except Exception as e:
        print(e)
a = int(input("Enter a :"))
b = int( input("Enter b :"))
divide(a,b)