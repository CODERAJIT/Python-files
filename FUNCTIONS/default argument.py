'''
Default argument
================

   Number of argument or        Number of variable used to
   values or variable passed =  receive.
'''
'''
def addition(x,y):
    z=x+y
    print("addition is :",z)
addition(10)
'''
#we got error
# addition() missing 1 required positional argument: 'y'

#use default arguments

def addition(x,y=0):
    z=x+y
    print("addition is :",z)
addition(10)

#addition is : 10





