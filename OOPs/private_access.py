'''
Private access specifier
=======================
The data member and method defined as private cannot be accessed
outside they can be accessed only inside class.

syntax defining:-

1.data member

  __variablename

2.method

  __methodname()

'''


class student:

    def getdata(
            self):  # this public method, bcz we can't make both the method as private bcz we can't call the function
        self.__name = input("enter name:")
        self.__rno = input("enter the rollno:")
        self.__display()

    def __display(self):  # private method
        print("Student name:", self.__name)
        print("Roll number:", self.__rno)


s1 = student()
s1.getdata()  # getdata(s1)
# self.__display() #error

# here we're trying to access outside the class but error will popup
'''
print("Name:",s1.__name) #error
print("Roll number:",s1__rno) #error
'''