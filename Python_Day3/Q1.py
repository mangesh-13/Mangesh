'''
1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

'''

List = list(map(int,input("Enter List elements:").strip().split()))
print("List:",List)
squares = [i**2 for i in List]
print("square_list:",squares)
