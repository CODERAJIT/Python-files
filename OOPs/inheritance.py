'''
Inheritance
===========
eg:

class A:

  def getdata(self):
     ..........
     ..........

  def display(self):
     ..........
     ..........


class B:

  def getdata(self):
     ..........
     ..........

  def display(self):
     ..........
     ..........


method getdata() defined in class A, same method is required in class B,
as a result we need to rewrite that method again in the class B which give
rise to code repeation.

In order to reuse the property of one class into another class there is needs`
of inheritance.

what is inheritance?
===================
The mechanism or process of deriving one class from another class to achieve
reusablity of code is called as inheritance.

The class from which another class derived is called as
base class pr parent class.

the class which is derived from another class is called as derived class or child class.

A parent or base class
         |
         |
         |
         B child or derived class

        Properited of class A or base class[data member and method]
        are now available to derived class or child class.



eg:

class A:
     body of class A

class B(A):
    body of class B


Types of inheritance:-
====================
1.single inheritance
2.multilevel inheritance
3.multiple inheritance
4.hierarchical inheritance
5.hybrid inheritance

'''