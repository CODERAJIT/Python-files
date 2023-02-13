'''
Exception
=========

Erros:These are the faults or mistake in the program,
There are two types of errors
1.compile time error
2.runtime error

Compile Time Error
==================
These errors are mainly due to mistake done in writing the syntax of the code.

Run Time Error
==============
The errors which occurs during program execution are called as run time error.
mainly due to user input.

Note:-Run Time Errors are called as Exception

stage1:error checking stage.
stage2:code execution stage.

'''
#example for compile time error
'''
x=int(input("enter numerator:"))
y=int(input("enter denominator:") # here one close bracket is not closed then while executing syntax error will popup by saying '(' is not closed

d=x/y
print("division is:",d)
'''
#example for Runtime time error

#import arithametic #Runtime error of ModuleNotFoundError
# here no syntax error but while executing if it's shows error then it is complier error, arithmatic file is not there in this folder so can't import
x=int(input("enter numerator:"))
y=int(input("enter denominator:"))

d=x/y #9/2=4.5 | 9/0=> zero can't be divided=> Run time error is called exception.
print("division is:",d)

'''
HOMEWORK:-
What is difference between Error and Exceptions?
'''