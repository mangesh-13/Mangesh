#Iterable- Something that can be looped over.
#e.g List is iterable bcoz we can looped over the list
# we can loop over the tuple,dictornary,,strings, set, generators,files
'''

nums=[1,2,3]
for i in nums:
    print(i)
'''   
    
#if something is iterable then it needs to have a special
#method called __iter__() 
#To look at the methods and attributes available to a
# specific object we can pass that in built in dir() function
#Check the attributes and methods available for our list
'''
print(dir(nums))
'''
# We can see one method is __iter__()
#So basically something that can looped over, if it has that method
#So what the for loop is doing in the background here?
#-->It is calling iter on our object and return iterator
# that we can loop over, so that is why we call a list iterable

# iterator=iter(nums)---> calls __iter__() method
#which converts our list to iterator and return iterator


# If we run __iter__() on our list then it will return an iterator
# So iterator is an object with a state so that it 
#remembers where is drawing iteration.

#Iterators also know how to get the next value.
#They get the next value using __next__() method.

# e.g

'''
List=[10,20,30,40]

it=iter(List) # calls __iter__ method and that method returns iterator

print(next(it)) # calls __next__() method and returns next value each time
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # error-StopIteration

'''


# User defined Iterator


class MyRange:
    def __init__(self,start, end):
        self.value=start
        self.end=end
        
    def __iter__(self):
        return self
    def __next__(self):
        if self.value>=self.end:
            raise StopIteration
            
        current=self.value
        self.value+=1
        return current
    
    
    
   
num=MyRange(1,10)
# print(type(num))
# it=iter(num)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

# for i in num:
#     print(i)








