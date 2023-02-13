'''
x=10
print("Data type of variable x:",type(x))

class student:

    def greet(self):

        print("hello")

s1=student()

print("Data type of object s1:",type(s1))
'''
'''
output:-

=================== RESTART: C:/10.OOPs/datatype_checking.py ===================
Data type of variable x: <class 'int'>
Data type of object s1: <class '__main__.student'> #in this object datatype is class name
'''

'''
conclusion:

Data type of variable is built in datatype i.e. int,float
Data type of object is classname.
In above program data type of object s1 is classname=>student.

'''


'''
x is variable of built in datatype.
s1 object is variable of user defined datatype.

x=10

In a single x variable is defined[memory allocate] and it is intialize to value 10.



                                           -----------
                                           |    10    |  we sre storing 10 value in x varaiable and  x is allocating memory for the value 10. 
                                           ------------
                                                x



if there is any need to initialize object at its creation,then
there is need of constructor.
'''

'''
1.Constructor is a special method or function which is used to initialize
object at  the time of it's creation.

2.It has fixed name name as __init__().
3.constructor is always called automatically when object of the class is created.

'''

class customer:

    def __init__(self):

        print("constructor is called!!")

c1=customer() #object created=> when object is created at the time constructor called
c2=customer() #2nd time object created, so how many times we created objects that many time constructor go na called or print

'''
output:-

constructor is called!!
constructor is called!!

Note:- see in above output two times we created object so two time constructor called and prined the output

'''

