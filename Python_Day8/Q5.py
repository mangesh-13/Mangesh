'''
5.Write a Python program to square and cube every number
in a given list of integers using Lambda.
'''

List=list(map(int,input("Enter list elements:").strip().split()))

square = list(map(lambda x : x**2,List))
print(square)
cube = list(map(lambda x : x**3,List))
print(cube)