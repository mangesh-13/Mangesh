'''
Write a program to check wheather number is even or odd using if
Else statement…
'''

def EvenOdd(number):
    if number%2==0:
        print(str(number)+" "+"is even")
    else:
        print(str(number)+" "+"is odd")

number=int(input("Enter the number you want to check:"))
EvenOdd(number)