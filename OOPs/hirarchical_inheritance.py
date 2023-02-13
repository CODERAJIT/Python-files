'''
Hirarchical Inheritance
=======================
The inheritance in which there is one base class and many derive classes
is called as Hirarchical Inheritance.


                                B
                                |
            ------------------------------------------
            |         |         |       |            |
            D1        D2       D3       D4 .........Dn


eg:-

                A
                |
        --------------
        |            |
        B            C


'''

class A:

     def geta(self): #self=b1|self=c1
         self.a=int(input("Enter value of a:")) #b1.a=20 |c1.=30

class B(A):

    def getb(self): #self=b1
        self.b=int(input("Enter the value of b:")) #b1.b=30

    def addition(self):
        r1=self.a+self.b
        print("Addition of a and b is:",r1)

class C(A):

    def getc(self): #self=c1
        self.c=int(input("Enter the value of c:")) #c1.b=10

    def addition(self):
        r2=self.a+self.c
        print("Addition of a and c is:",r2)

b1=B()  #derived class object B.
b1.geta() #geta(b1)
b1.getb() #getb(b1)
b1.addition() #addition(b1)
print()
c1=C() #derived class object C
c1.geta() #geta(c1)
c1.getc() #getc(c1)
c1.addition() #addition*c1)