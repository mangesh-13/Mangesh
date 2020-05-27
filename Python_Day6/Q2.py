'''
2.	Write program to implement Selection sort.
'''

List=[1,12,3,70,10,44,2]
print("Original List:",List)

for i in range(0,len(List)):


    min = i
    for j in range(i + 1, len(List)):
        if List[min] > List[j]:
            min = j


    List[i], List[min] = List[min], List[i]
print("Sorted List:",List)




