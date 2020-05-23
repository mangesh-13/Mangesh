n= int(input("Enter the number of rows:"))
for row in range(1,n+1):
    for col in range(0,row):
        print(row,end=" ")
    print()
