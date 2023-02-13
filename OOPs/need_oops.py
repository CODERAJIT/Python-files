'''
Types of programming
======================
1,procedural oriented programing
2.object oriented programing


procedural oriented programming system
========================================
The programming system in which contains inbuilt functions
or user defined functiones to executed a task or logic is
called as procedural programming.

1.security
==========
In procedural oriented programming system, a global varaiable value
can be accessed in all functions,this may create an issue of security
for a global variable storing sensitive information like username and
password.


2.user defined datatype
=======================
int,float and string these are built in datatype. if there is need to
create user defined datatype, then it can be achived with the help of oops.


3.Mapping entity digitally
=========================
Any real world entity can be mapped digitally easily in the system with the
help of oops.  eg:- pan number which is qnique.

In order to remove disadvantage of security in procedural programming system
and to create user defined datatype, mapping real world entity digitialy,there is need of oops.

object orinted programming system consisi of:
1.classes
2.objects

class
=====
class is a template or blueprint.

object
======
object is manufactured from class blueprint.

             student name:___________________
             Roll number:________________
             per        :_______________

             submit



          ---------------------------------------------------------------
          |                                                              |
student name:itvedant                                        student name:Ecl;ass
Roll number:45                                               roll number:35
per        :98                                               per        :67.9

   object 1                                                    object 2




'''
# x=10
# pi=3.14
uname = input("enter uername:")
upass = input("enter password:")


def greet():
    print("good evening ram")
    print("value of x is:", uname)


def helloworld():
    print("hello world")
    print("value of x:", uname)


greet()
helloworld()