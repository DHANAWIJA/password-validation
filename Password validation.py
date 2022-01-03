#PASSWORD VALIDATION

import re
password=input("enter your password:")
lower=re.findall('[a-z]',password)
upper=re.findall('[A-Z]',password)
number=re.findall('[0-9]',password)
spacial=re.findall('\w',password)

while True:
    if len(password)<8:
        print('your password is too short')
    elif len(password)>15:
        print('your password is too long')
    elif len(lower)<1:
        print('your password should contain atleast one lower character')
    elif len(upper)<1:
        print('your password should contain atleast one upper character')
    elif len(number)<1:
        print('your password should contain atleast one numeric value')
    elif len(spacial)<1:
        print('your password should contain atleast one spacial character')

    if len(lower)>=1 and len(upper)>=1 and len(number)>=1 and len(spacial)>=1:
        print('you have a entered valid password')
        break
    else:
        print('retry with combination of lower case,upper case,numeric and spacial')
        break



