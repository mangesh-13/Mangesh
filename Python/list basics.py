list=[[1,2,2,4],[5,7,8,9],[10,11,45,100]]
print(id(list))
print("=============================")
for i in list:
    print(id(i))
print("===============================")
for i in list:
    for j in i:
        print(id(j))
    print("---------------------------------------------------------")

