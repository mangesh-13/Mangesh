'''
Packing and Unpacking Arguments in Python
We use two operators * (for tuples) and ** (for dictionaries).

Background
Consider a situation where we have a function that receives four arguments.
We want to make call to this function and
we have a list of size 4 with us that has all arguments for the function.
If we simply pass list to the function, the call doesn’t work.
'''
'''
# A Python program to demonstrate need  
# of packing and unpacking 
  
# A sample function that takes 4 arguments 
# and prints them. 
def fun(a, b, c, d): 
    print(a, b, c, d) 
  
# Driver Code                    #error
my_list = [1, 2, 3, 4] 
  
# This doesn't work 
fun(my_list) 
'''

#Unpacking
'''
We can use * to unpack the list so
that all elements of it can be passed as different parameters.
'''
'''
# A sample function that takes 4 arguments 
# and prints the, 
def fun(a, b, c, d): 
    print(a, b, c, d) 
  
# Driver Code 
my_list = [1, 2, 3, 4] 
  
# Unpacking list into four arguments 
fun(*my_list)
'''
#Packing

'''
When we don’t know how many arguments need to be passed to a python function,
we can use Packing to pack all arguments in a tuple.
'''

# A Python program to demonstrate use 
# of packing 
''' 
# This function uses packing to sum 
# unknown number of arguments 
def mySum(*args):
    print(args)
    sum = 0
    for i in range(0, len(args)): 
        sum = sum + args[i] 
    return sum 
  
# Driver code 
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20)) 
'''
#Packing and Unpacking
#Below is an example that shows both packing and unpacking.


# A Python program to demonstrate both packing and 
# unpacking.
''' 
# A sample python function that takes three arguments 
# and prints them 
def fun1(a, b, c): 
    print(a, b, c) 
  
# Another sample function. 
# This is an example of PACKING. All arguments passed 
# to fun2 are packed into tuple *args. 
def fun2(*args): 
  
    # Convert args tuple to a list so we can modify it 
    args = list(args) 
  
    # Modifying args 
    args[0] = 'Mangesh'
    args[1] = 'awesome'
  
    # UNPACKING args and calling fun1() 
    fun1(*args) 
  
# Driver code 
fun2('Hello', 'beautiful', 'world!') 

 '''
# ** is used for dictionaries
'''
# A sample program to demonstrate unpacking of 
# dictionary items using **
def fun(a, b, c):
    print(a, b, c) 
  
# A call with unpacking of dictionary 
d = {'a':2, 'b':4, 'c':10} 
fun(**d) 
'''

# A Python program to demonstrate packing of 
# dictionary items using ** 
def fun(**kwargs):
    print(kwargs)
  
    # kwargs is a dict 
    print(type(kwargs)) 
  
    # Printing dictionary items 
    for key in kwargs: 
        print("%s = %s" % (key, kwargs[key])) 
  
# Driver code 
fun(name="Mangesh", ID="101", language="Python")













