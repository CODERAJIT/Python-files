'''
Hybrid inheritance
==================

The inheritance which is the combination of hirachical and multiple
inheritance is called as hybrid inheritance.

                   A geta() =>self.a
                   |
        ------------------------
        |                      |
        B getb()=>self.b       C self.c <= getc()
        |                      |
        -----------------------
                   |
                   D addition()

class A:

cl;ass B(A):

class C(A):

class D(B,C): derived class

'''


class A:

     def geta(self): #self=c1
         self.a=int(input("Enter value of a:")) #c1.a=20

class B(A):
    def getb(self): #self=c1
        self.b=int(input("Enter the value of b:")) #c1.b=30

class C(A):
    def getc(self):
        self.c=int(input("Enter the value of c:"))

class D(B,C):

    def addition(self):
        res=self.a+self.b+self.c
        print("Addition is:",res)

d1=D()  #derived class object.
d1.geta() #geta(c1)
d1.getb()
d1.getc()
d1.addition() #addition(c1)
