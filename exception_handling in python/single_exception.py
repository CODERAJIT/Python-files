'''
Handling Exception can be done using following instruction.

Try:

    Code to be inspected for exception
    or
    code in which there is change of
    getting exception.

exception ExceptionName:

   Except block to given msg.

'''

x=int(input("enter numerator:"))
y=int(input("enter denominator:"))

try:

    d=x/y
    print("Division is:",d)

except ZeroDivisionError:
    print("Denominotor canot be zero,please enter number other than zero")


'''
output:-enter numerator:9
enter denominator:0
Traceback (most recent call last):
  File "C:/8.exception handling in python/single_exception.py", line 19, in <module>
    d=x/y
ZeroDivisionError: division by zero

======== RESTART: C:/8.exception handling in python/single_exception.py ========
enter numerator:9
enter denominator:0
Denominotor canot be zero,please enter number other than zero

'''
#before writing try and except we was getting above error after adding msg in except it is displaying that as msg error 