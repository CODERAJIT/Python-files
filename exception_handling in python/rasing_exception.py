'''
Raising an exception[raising exception means raising error description from our end when we get error]
====================
                                                                                --------- python
              When there is fault in runtime---exception is raised--handles by--|
                                                   by system                     --------try.excet(user defined)

Till now exception is raised internally by system,
if there is need to raised an exception,
then raise keyword to raise an exception.

exception is raised with recepct to certain condition.
Syntax to raise exception
=========================

  raise ExceptionName('Message')

'''



x=int(input("enter numerator:"))#x=9|x=9
y=int(input("enter denominator:"))#y=2|y=0

if y==0: #2==0F|0==0T

    raise ZeroDivisionError('Denominator cannot be Zero!!')


else:
    d=x/y #9/2=>4.5 |9/0=> Exception is rasied|ZeroDivisionError
    print("Division is:",d)

'''
output:-

enter numerator:9
enter denominator:2
Division is: 4.5

======== RESTART: C:/8.exception handling in python/raising_exception.py =======
enter numerator:9
enter denominator:0
Traceback (most recent call last):
  File "C:/8.exception handling in python/raising_exception.py", line 27, in <module>
    raise ZeroDivisionError('Denominator cannot be Zero!!')
ZeroDivisionError: Denominator cannot be Zero!!

'''

'''
home work:-

check weither it is digit or not  then if it is not digit then raise a exception for above code

'''