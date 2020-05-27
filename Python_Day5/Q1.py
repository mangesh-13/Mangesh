'''
1.	Write a Python program to sort a list of elements using the bubble sort
Algorithm.
'''
def BubbleSort(List):
    for i in range(0,len(List)-1):

        for j in range(0,len(List)-i-1):

            if List[j] >List [j+1] :

                List[j],List[j + 1]=List[j+1],List[j]

#List=[47, 64, 37, 76, 95,4,44,5,60,100] or
List=list(map(int,input("Enter list elements:").strip().split()))
print(List)
BubbleSort(List)
print(List)


