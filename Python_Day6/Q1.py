'''
1.	Python program to Swap Keys and Values in Dictionary.
'''
'''
Dict={"Name":"Mangesh","age":28,"id":40,"Address":"Pune" }
nDict={}
for key,value in Dict.items():
    if key in Dict:
        nDict[value]=key
    else:
        nDict[value]=key

print(nDict)
'''
#or

Dict={"Name":"Mangesh","age":28,"id":40,"Address":"Pune" }
nDict=dict([value,key] for key,value in Dict.items())
print(nDict)