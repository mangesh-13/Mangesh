#collection: Counter


# Counter is containor that stores the elements as dictionary keys and
# their counts as dictionary values


from collections import Counter
a="aaaaaaabbbbbbcccc"
my_counter=Counter(a)
print(my_counter)


'''
Definition and Usage
The items() method returns a view object. The view object contains the key-value pairs of the dictionary,
 as tuples in a list.

The view object will reflect any changes done to the dictionary.

Syntax
dictionary.items()
Parameter Values:
No parameters
'''

print(my_counter.items())
print(my_counter.values())
print(my_counter.keys())
 
