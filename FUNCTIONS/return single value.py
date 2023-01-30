'''
syntax:

def function_name(arguments):

    function body

    return value

Need: If there is need for a function to return a value or
      result there use return statement.
Problem:
=======
values given to function=>marks of 3 subjects
definition of function  =>Calculate total

%  = marks obtained           marks obtained
     -------------- x 100  => ---------------
        300                          3

returned value is returned at the place of the function call.
Thus we require a variable to which function call is assigned
so that returned value is stored in that variable.
'''

m1=int(input("enter  1st your numbeer :"))
m2=int(input("enter  2nd your numbeer :"))
m3=int(input("enter  3rd y0ur numbeer :"))
def marksadd(a,b,c):#function definition, a=70, b=85, c=90
    t=a+b+c #t=70+85+90=245
    return t
tot=marksadd(m1,m2,m3)
print("Total Marks",tot)

'''
enter  1st your numbeer :70
enter  2nd your numbeer :85
enter  3rd y0ur numbeer :90
Total Marks 245

'''