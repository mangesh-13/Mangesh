'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def div(start,end):
    List = []
    for i in range(start,end+1):
        if i%7==0 and i%5 !=0 :
            List.append(str(i))
    return (",".join(List))




start=int(input("Enter the start number:"))
end=int(input("Enter the end number:"))
print(div(start,end))



