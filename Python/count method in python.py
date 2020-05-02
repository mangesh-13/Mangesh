'''
Python String | count()
count() function in an inbuilt function in python programming language that returns the number of occurrences of a substring in the given string.

Syntax:

string.count(substring, start=…, end=…)



Parameters:

The count() function has one compulsory and two optional parameters.
Mandatory parameter:
1)substring – string whose count is to be found.

Optional Parameters:
1)start (Optional) – starting index within the string where search starts.
2)end (Optional) – ending index within the string where search ends.

Return Value:
count() method returns an integer that denotes number of times a substring occurs in a given string.
'''
'''
#without optional parameter
# Python program to demonstrate the use of 
# count() method without optional parameters  
  
# string in which occurrence will be checked 
string = "This is python world" 
  
# counts the number of times substring occurs in  
# the given string and returns an integer 
print(string.count("is")) 
'''
#with optional parameters
# Python program to demonstrate the use of 
# count() method  using optional parameters 
  
# string in which occurrence will be checked 
string = "This is python world" 
  
# counts the number of times substring occurs in  
# the given string between index 0 and 5 and returns  
# an integer 
print(string.count("is", 0, 5)) 
  
print(string.count("is", 0, 15)) 
