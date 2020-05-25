def Unique(List):
    unique_list=[]
    for i in List:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


#List = [11,22,22,33,33,33,44,55,55,66]
List=list(map(int,input("Enter the elements of list:").strip().split()))
print(List)
print(Unique(List))
