'''
5)Write a Python program to check whether a given number is a narcissistic number or not
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  3^3 + 7^3 + 1^3 the sum is 371. Other 3-digit narcissistic numbers are
153 = 1^3 + 5^3 + 3^3
370 = 3^3 + 7^3 + 0^3
407 = 4^3 + 0^3 + 7^3.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 1^4+6^4+3^4+4^4
8208 = 8^4+2^4+0^4+8^4
9474 = 9^4+4^4+7^4+4^4
'''
def narcissistic(number):
    sum=0
    while number != 0:
        rem = number % 10
        number = number//10
        print(rem)
        sum += rem **3
    return sum

number =int(input("Enter number:"))
result = narcissistic(number)
print('Result:',result)
if result == number:
    print("Given number is narcissistic")
else:
    print("Given number is not narcissistic")