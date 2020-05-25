def Sum(number):
    Last=number%10
    first=0

    while(number>=10):

        number=number//10
        first=number

    return first + Last

number=int(input("Enter the number:"))
print(Sum(number))