'''
3.	Write a Python program for Binary search.
'''
def Binary_Search(List,data):
    Left=0
    right=len(List)-1
    mid=0

    while Left <= right:

        mid=(Left + right)//2
        if data < List[mid] :
            right= mid - 1

        elif data > List[mid]:
            Left= mid + 1

        else:
            return f"data is found at index {mid}"
    return f"data not found index {-1}"



List=list(map(int,input("Enter list elements:").strip().split()))
List.sort()
print(List)
data=int(input("Enter the data you want to search:"))
print(Binary_Search(List,data))