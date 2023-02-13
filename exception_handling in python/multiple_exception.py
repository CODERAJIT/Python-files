'''

Handling Multiple Exception can be done using following instruction.

Try:

    Code to be inspected for exception
    or
    code in which there is change of
    getting exception.

exception ExceptionName1:

   Except block to given msg.

exception ExceptionName2:

   Except block to given msg.

.
.
.
.
exception ExceptionNamen:

   Except block to given msg.


'''



try:
    x=int(input("enter numerator:"))
    y=int(input("enter denominator:"))
    d=x/y
    print("Division is:",d)

except ZeroDivisionError:
    print("Denominotor canot be zero,please enter number other than zero")

except ValueError:
    print("Enter proper digit for numerator or denominator")


'''
output:-

enter numerator:9
enter denominator:two
Traceback (most recent call last):
  File "C:/8.exception handling in python/multiple_exception.py", line 32, in <module>
    y=int(input("enter denominator:"))
ValueError: invalid literal for int() with base 10: 'two'

======= RESTART: C:/8.exception handling in python/multiple_exception.py =======
enter numerator:0
enter denominator:9
Division is: 0.0

======= RESTART: C:/8.exception handling in python/multiple_exception.py =======
enter numerator:9
enter denominator:0
Denominotor canot be zero,please enter number other than zero

======= RESTART: C:/8.exception handling in python/multiple_exception.py =======
enter numerator:9
enter denominator:two
Enter proper digit for numerator or denominator

'''

#seaching the exception errors types to write code is (https://docs.python.org/3/library/exceptions.html)
#name to search (exception in python document)
