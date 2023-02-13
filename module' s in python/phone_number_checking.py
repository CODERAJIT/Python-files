'''
Validation:
==========
Input given by the user is as per rule defined by developer in the
application or validating the input.

Validate mobile number
======================

1.check whether it is digit or not => isdigit()
2. check whether it is 10 digit.
'''

mob=input("enter mobile number:") #8975642901
'''
if mob.isdigit(): #8975642901.isdigit()=>true, 8975642.isdigit() false

    if len(mob)==10: #len(8975642901)=>10=>true, 9==10=> false

        print("valid mobile number")

    else:
        print("invaild mobile number")

else:
    print("invalid mobile number")

'''
#same program using AND operater

if mob.isdigit() and len(mob)==10:

    print("valid mobile number")

else:

    print("invaild mobile number")

'''
output:-

enter mobile number:897564290
invaild mobile number

=========== RESTART: C:/7 modules in python/phone_number_checking.py ===========
enter mobile number:8975642901
valid mobile number

=========== RESTART: C:/7 modules in python/phone_number_checking.py ===========
enter mobile number:8975642901
valid mobile number
valid mobile number

=========== RESTART: C:/7 modules in python/phone_number_checking.py ===========
enter mobile number:89756429
invaild mobile number
invaild mobile number

'''