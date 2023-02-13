'''

Build in module
===============

                          module
                --------------------------
                |          |             |
            functions    Constants    Classes

module documents link is :-
=========================
https://docs.python.org/3/library/math.html
python math module documents(search with this)

In order to use match module in the python file.then there is s need to
import that module

step1:import module
step2: use the module
'''

#import math

#factorial
'''
r=math.factorial(4) #there use dot we are importing functions or constants or class with that names, here example math we're used
print("factorial of number is:",r)
'''

#Alisaing module => giving different name eg. import math as m, here we giving different name for math so we can call that function with the name of m

#import math as m

#Ceil() and floor()
'''
15.7=>15 to 16=>16  #ceil() will give higher value like 15.2 or 15.7 it gives 16
15.5=>15 to 16=>16  #floor() will gives lower value like 15.2 or 15.7 it gives 15
15.2=>15 to 16=>16

'''
'''
print(m.ceil(15.8))
print(m.ceil(15.5))
print(m.ceil(15.3))
'''
'''
floor():
15.2=>15 to 16=>15
15.7=>15 to 16=>15
15.5=>15 to 16=>15
'''
'''
print(m.floor(15.8))
print(m.floor(15.5))
print(m.floor(15.3))
'''

#import specific functionality from module

from math import factorial,sqrt

r=factorial(6)
print("factorial is :", r)

sroot=sqrt(25)
print("square root is:",sroot)