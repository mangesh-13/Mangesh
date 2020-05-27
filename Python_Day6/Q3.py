'''
3.	Write program to implement Insertion sort.
'''

List=[5,4,10,1,6,2]

for i in range(0,len(List)):
    temp=List[i]
    j=i-1
    while(j>=0 and List[j]>temp):
        List[j+1]=List[j]
        j-=1
    List[j+1]=temp

print(List)

'''
def insertion_sort(A):
    for i in range(1,len(A)):
        for j in range(i-1,-1,-1):
            if A[j]> A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
            else:
                break

A=list(map(int,input("Enter List elements:").strip().split()))
print(A)
insertion_sort(A)
print("List after sorting:",A)
'''







