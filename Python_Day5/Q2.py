'''
2.	Write a Python program for sequential search (Linear search).
'''
def Sequential_search(List, key):
    for i in range(0,len(List)):
        if key == List[i]:
            return f"{key} is found at index {i}"

    return -1

List=list(map(int,input("Enter list elements:").strip().split()))
key=int(input("Enter the element you want to search:"))
print(Sequential_search(List,key))