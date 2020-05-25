'''1.	Write a function to find max of three numbers.'''

def max_numbers(a,b,c):
    if a>= b and a>=c:
        max=a
    elif b>=a and b>=c:
        max=b
    else:
        max=c
    return max


# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
a,b,c=input("Enter a,b,c values:").strip().split()
print("Max of three Numbers:",max_numbers(a,b,c))