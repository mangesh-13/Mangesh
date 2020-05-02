'''

Python String | split()
split() method returns a list of strings after breaking the given string by the specified separator.

Syntax :

str.split(separator, maxsplit)
Parameters :



separator : The is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.

maxsplit : It is a number, which tells us to split the string into maximum of provided number of times. If it is not provided then there is no limit.

Returns :

returns a list of strings after breaking the given string by the specified separator.

'''

text = 'geeks for geeks'
  
# Splits at space 
print(text.split()) 
  
word = 'This, is, it'
  
# Splits at ',' 
print(word.split(', ')) 
  
word = 'this :is:it'
  
# Splitting at ':' 
print(word.split(':')) 
  
word = 'CatBatSatFatOr'
  
# Splitting at 3 
print([word[i:i+3] for i in range(0, len(word), 3)]) 
