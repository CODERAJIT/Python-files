import string as s
import random as r

alpha = s.ascii_letters
digit = s.digits

# print(alpha)
# print(digit)

alnum = alpha + digit
# print(alnum)


'''

                                      alnum


       abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
       0123456......................................................61 =>index

captach would of 5 character.

step1: select random index value
step2: access character of that randomaly selected index.
step3: concatenate with the string

'''

captcha = ""

for i in range(0, 5):
    index = r.randrange(0, len(alnum))
    # print(index)
    # print(alnum[index])
    captcha = captcha + alnum[index]
    # print(captcha)
    # print("---------------------------")

print(captcha)

'''
output:-


58
6
6
---------------------------
19
t
6t
---------------------------
21
v
6tv
---------------------------
58
6
6tv6
---------------------------
60
8
6tv68
---------------------------

============ RESTART: C:/7 modules in python/captcha_using_string.py ===========
f1cmj

============ RESTART: C:/7 modules in python/captcha_using_string.py ===========
a7BqZ

'''