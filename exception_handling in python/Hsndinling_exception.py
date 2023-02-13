'''
Handling any exception with exception parent class.


'''

try:
    x = int(input("enter numerator:"))
    y = int(input("enter denominator:"))
    d = x / y
    print("Division is:", d)

except Exception as e:  # here we're not given any error type still it displaying print stament one as a error bcz all error types under exception, those types are child for exception

    print("error:", e)
    # print("somting went wrong !!!")

'''
ZeroDivisionError: diivision by zero

instent of writing the keyword if we print exception it'll print error discription

output:-

enter numerator:9
enter denominator:3
Division is: 3.0

======= RESTART: C:/8.exception handling in python/Handling_exception.py =======
enter numerator:9
enter denominator:0
somting went wrong !!!

======= RESTART: C:/8.exception handling in python/Handling_exception.py =======
enter numerator:9
enter denominator:0
error: division by zero

======= RESTART: C:/8.exception handling in python/Handling_exception.py =======
enter numerator:9
enter denominator:0
error: division by zero

======= RESTART: C:/8.exception handling in python/Handling_exception.py =======
enter numerator:two
error: invalid literal for int() with base 10: 'two'

'''