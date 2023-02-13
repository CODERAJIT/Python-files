'''
Random module
=============
search with this link:-
https://docs.python.org/3/library/random.html

type with [ random python module documentation]

'''

import random as r

#random()
'''
x=r.random() #gives fration value between 0 to 1
print(x)

t=x*1000
print(t)

otp=round(t)
print("otp to be send:",otp)
'''

#above program writen in single line code

otp=round(10000*r.random())
print("OTP to be send:",otp)

'''
out put:-

0.9177656223091455
917.7656223091454
otp to be send: 918

=============== RESTART: C:/7 modules in python/random_module.py ===============
OTP to be send: 3963

=============== RESTART: C:/7 modules in python/random_module.py ===============
OTP to be send: 65438

'''