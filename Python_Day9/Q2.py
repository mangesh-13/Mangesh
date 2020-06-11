'''
2.	Write python program to check  that given number is valid mobile number or not?
'''


# [6-9][0-9]{9} or [6-9]\d{9}

import re
s = input('Enter mobile number to validate:')
m = re.fullmatch('[6-9]\d{9}',s)
if m != None :
    print(s,'is valid mobile number')
else:
    print(s,'is not valid number')