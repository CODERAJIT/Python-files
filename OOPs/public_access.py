'''
Four pillars of object oriented programming system
==================================================
1.Abstraction
2.encapsulation
3.Inheritance
4.polymorphism

Need of Encapsulation
=====================
Security

medicine capsule:
================
Capsule cover protect the medicine ingredients that are inside capsule.

Similerly, Data member and method are enclosed withing class wrapper.
class indirectly provide security to the data member and method[function] inside class.

The process of wrapping data in a single unit class is called as encapsulation.

class is wrapping data member and methods in a single unit.

Access specfier
===============
1.public
2.private

By Default all data member and methods has public access.
The data member with public access specifier can be access inside class as well as outside class.

'''

class student:

    def getdata(self):

        self.name=input("enter name:")
        self.rno=input("enter roll number:")
        self.display()#display(self)=>display(s2). access function inside function

    def display(self):
        print("student name:",self.name)
        print("Roll number:",self.rno)


#s1=student() #object is created

#Accessing name and rno outsid class
#s1.name="Itvedant"
#s1.rno=56

#s1.display()#display(s1)

s2=student()
s2.getdata()