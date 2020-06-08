'''
From a list containing ints, strings and floats, make three lists to store them separately.
'''
Int = []
Str = []
Float = []

List =[1,10.0,"Mangesh",11.5,"Rahul","Nikhil",15,16,50.60,7,8,5,"Avdhut",40.20,30,10]

for i in List:

    if type(i) == int:
        Int.append(i)
    elif type(i) == float:
        Str.append(i)
    else:
        Float.append(i)

print(Int)
print(Str)
print(Float)

