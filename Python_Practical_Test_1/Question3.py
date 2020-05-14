#3.  Arrange String characters such that lowercase letters should come first 
#Given input String of combination of the lower and upper case arrange characters in such a way 
#that all lowercase letters should come first. 



#string= "PyNaTive"

string=input("Enter the string:")

List = string.split()
lower_char_list = []
upper_char_list = []
for char in string:
    if char.islower():
        lower_char_list.append(char)
    else:
        upper_char_list.append(char)
string1 = ''.join(lower_char_list + upper_char_list)
print("arranging characters giving precedence to lowercase letters:"+str(string1))


