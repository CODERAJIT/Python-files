'''
Destructor
==========
1.it is a special method used to delete/release memmory allocated
to a object at its creation.
2.it has fixed name as _del_().
3.destructor is called when program control reaches end.
'''

class customer:

    def __init__(self):
        print("constructor is called....")

    def __del__(self):
        print("desctuctor is called...")


c1=customer() #customer(c1)=> constructor is called
c2=customer() #customer(c2)=> constructor is called
print("hello world") #this line is end of program, always desctorctor will execute after ending a program
#and how many number times object is created that many time desctuctor will called or ececuted and printed.

'''
output:-


C:\Users\Windows>cd C:\10.OOPs

C:\10.OOPs>python destructor_called.py
constructor is called....
constructor is called....
hello world
desctuctor is called...
desctuctor is called...

'''

#NOTE:- intervew question is:- defference between constructor and destructor 