'''
Mulyipule inheritance
=====================
The inheritance in which there are many base class but only one
derived class is called as multiple inheritance.


                  B1    B2    B3  ............. Bn
                  |     |     |                 |
                  -------------------------------
                               |
                               D



Syntax:
class D(B1,B2,B3,.....,Bn):

    body of derived class

      A   B  -> both are base class
      |   |
      ----
       |
       C -->derived class

'''

class A:

     def geta(self): #self=c1
         self.a=int(input("Enter value of a:")) #c1.a=20

class B:
    def getb(self): #self=c1
        self.b=int(input("Enter the value of b:")) #c1.b=30

class C(A,B):

    def addition(self):
        res=self.a+self.b
        print("Addition is:",res)

c1=C()  #derived class object.
c1.geta() #geta(c1)
c1.getb() #getb(c1)
c1.addition() #addition(c1)`    