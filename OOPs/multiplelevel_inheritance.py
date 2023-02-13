'''
Multilevel inheritance
======================

                      A Base class
                      |
                      |
                      B  Intermediate base class
                      |
                      |
                      c  Intermediate base class
                      |
                      |
                      D  derived class


'''

class A:

     def geta(self): #self=d1
         self.a=int(input("Enter value of a:")) #d1.a=20

class B(A):

    def getb(self): #self=d1
        self.b=int(input("Enter the value of b:")) #d1.b=30

class C(B):

    def getc(self): #self=d1
        self.c=int(input("Enter value of c:")) #d1.c=50

class D(C):

    def addition(self): #self=d1
        res=self.a+self.b+self.c #res=d1.a+d1.b+d1.c=20+30+50=100
        print("Addition is:",res)


d1=D() #derived class object is created
d1.geta() #geta(d1)
d1.getb() #getb(d1)
d1.getc() #getc(d1)
d1.addition() #addition(d1)