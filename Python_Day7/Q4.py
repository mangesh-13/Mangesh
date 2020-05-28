

'''
Using reference counter we can count total number of references that
are made internally in python to assign a value to a data object.
'''


import sys
a="Welcome to the world of python"

print(sys.getrefcount(a))