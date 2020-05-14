
#2.  Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1 
#Expected Outcome:         appendMiddle("Chrisdem", IamNewString) → "ChrIamNewStringisdem" 


def appendMiddle(str1,str2):
    no=len(str1)//2
    return (str1[:no-1]+str2+str1[no-1:])
    


#print(appendMiddle("Chrisdem","IamNewString"))
str1=input("Enter first String:")
str2=input("Enter second String:")
print(appendMiddle(str1,str2))