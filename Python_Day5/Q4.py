'''
4.	Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]

'''
'''
List1=["M","na","i","lak"]
List2=["y","me","s","han"]
concated_list=[]

for i,j in zip(List1,List2):
    concated_list.append(i+j)
print(concated_list)
'''

#or

List1=["M","na","i","lak"]
List2=["y","me","s","han"]
concated_list = [i + j for i,j in zip( List1, List2)]

print(concated_list)