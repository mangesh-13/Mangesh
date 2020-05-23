'''1.	Python Program to Read a Number n And Print the Series “1+2+…..+n= “
          sample:
          Case 1:
	Enter a number: 4
1 + 2 + 3 + 4 = 10
Case 2:
Enter a number: 5
1 + 2 + 3 + 4 + 5 = 15'''


n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    print(i,"+",end="")
    sum+=i
print("=",sum)