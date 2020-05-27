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









