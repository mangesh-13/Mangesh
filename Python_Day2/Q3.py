'''
3.	Write a Python program to create the multiplication table (from 1 to 10) of a number.
'''

n=int(input("Enter number who multiplication table you want:"))
for i in range(1,11):
    print(n*i,end=" ")