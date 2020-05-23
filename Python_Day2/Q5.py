'''5.Write python program to print the pattern given below
Note: Take input from user
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''

n=int(input("Enter number of rows you want:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

