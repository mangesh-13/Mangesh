'''
# Given a number count the total number of digits in a number
#For example, the number is 75869, so the output should be 5.

def CountDigits(number):
    count=0
    while number!=0:
        number//=10
        count+=1
    return count



number=int(input("Enter the number who's count you want to find:"))
#75869
print(CountDigits(number))

'''

#Reverse the following list using for loop list1 = [10, 20, 30, 40, 50] 

#list1=[10,20,30,40,50]
n=int(input("Enter the length of list1:"))
list1=list(map(int,input("Enter the elements for list1:").strip().split()))[:n]
list1.reverse()
for i in list1:
    print(i)
