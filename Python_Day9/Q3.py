'''
3.	Write python program to check  that given email address is valid   or not?
'''

import re
s = input("Enter email id:")
m = re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.]com+',s)
if m != None:
    print("Valid mail id")
else:
    print("Invalid email id")