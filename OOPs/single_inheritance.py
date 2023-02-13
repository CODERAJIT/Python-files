'''
single inheritance:
===================
The inheritance in which there is only one base class and one derived class is
called as single inheritance

        A base class
        |
        |
        |
       B base class
class A
method   =>geta(self)
data member=>a

class B
method   =>getb(self)
data member=>b
'''

class A:

    def geta(self): #slf=b
        self.a=int(input("enter value of a:")) #b1.a=20

class B(A):

    def getb(self):#self=b1
        self.b=int(input("enter value of b:"))#b1.b=40

    def addition(self):#self=b1

        res=self.a+self.b #res=b1.a+b1.b=20+40=60
        print("Addition is:",res)

b1=B()#derived class object
b1.geta() #geta(b1)
b1.getb()#getb(b1)
b1.addition()#addition(b1)
