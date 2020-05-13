# #Python Iterators

# Iterators are present in python.They are mostly 
# implemented within for loops, comprehensions,
# generators etc. but hidden in plain sight

# Iterator in python is simply an object that can be
# iterated upon.
# An object which will return data, one element at a Time.


# Technically speaking, Python iterator object must
# implement two special methods,
# ___iter___() and __next__, collectively called the
# iterator proocol.

# An object is called iterable if we can get an iterator
# from it.
# Most of bulit-in containors in Python like 
# :list , tuple, string etc. are iterables

# The iter() function(which in turn calls the __iter__() methods)
# return an iterator from them.
# The __next__ method must return the next item in the 
# sequence. On reaching the end, and in subsequent calls
# it must raise StopIterations.


class Pow_of_Two:
    def __init__(self, max=0):
        self.max=max
        
    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n<=self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
            
            
a=Pow_of_Two(4)
it=iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))




































