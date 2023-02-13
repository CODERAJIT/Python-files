'''
try......except and else
========================
else block is excecuted only when there is no exception.

'''

try:
    x=int(input("enter numerator:"))#x=9|x=9
    y=int(input("enter denominator:"))#y=2|y=0
    d=x/y #9/2=>4.5 |9/0=> Exception is rasied|ZeroDivisionError
    #print("Division is:",d)

except Exception as x:

    print("Error:",x)

else:
    print("In the else block")
    print("Division is:",d)  #to save execution time and compiler time we are printing this statment here, in this print no chance of getting run time error

'''
output:-

enter numerator:9
enter denominator:2
Division is: 4.5
In the else block

======= RESTART: C:/8.exception handling in python/try_exception_else.py =======
enter numerator:9
enter denominator:two
Error: invalid literal for int() with base 10: 'two'

======= RESTART: C:/8.exception handling in python/try_exception_else.py =======
enter numerator:9
enter denominator:0
Error: division by zero
'''

'''
else block is used to offload try block.
try block should always contains only those lines of code in which
there is chance of getting error.
code line in which there is no chance of getting run time error
or exception must be in else block. 

'''