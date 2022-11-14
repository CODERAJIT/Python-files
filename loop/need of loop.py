'''
Need of Loop:
============
To achieve reusability or to reduce code repeatition, there
is need of loop.



#display string "Hello World" 5/10/100 times on the console.
print("Hello World")
print("Hello world")
print("Hello World")
print("Hello world")
print("Hello world")
print("Hello World")
print("Hello world")
print("Hello World")
print("Hello world")
print("Hello world")




In above approach of writing same instruction or statement
again and again, this led to code repeatition.
Code repeatition has following disadvantages.
=============================================
1) length of the program increase due to which debugging sometime
   become difficult.
2) Memory increase.
3) Waste of compiler or interpreter time as same code is
   executed.

In order to remove or dicard disadvantage caused by code
repeatition there is need of loop control instuction.



what is loop control instruction?
================================
The instruction which allows us to write code once and repeat it
n number times or infinite number of time are called as
loop control instructions.

Types of Loop control instrcution
================================
1) while loop
2) for   loop



#while loop

syntax:

initialization

while condition:


    body or code to be repeated
    increment or decrement

variable used in intialization is called as counter variable.
As it is used to store number of repeatition or iteration
perfomed by loop.
working of loop:
===============

working:
step1:initialization [Done only once]
step2:check condition
step3:If condition is True then executed code or loop body.
step4:increment or decrement
step5:repeat step2 to step4 till condition is True.
step6:Once condition is False ,go to step7.
step7:stop
initialization
                                |
				|       False
                 ----------->condition-------->Out of loop
                |               |
                |               | True
                |          code in loop[Body]
                |               |
                |               |
                |               |
	        	incre/decre<----


i   i<=10   print("Hello World")   i+=1 => i=i+1
1   1<=10 T Hello World            i=1+1=2
2   2<=10 T Hello World            i=2+1=3
3   3<=10 T Hello world            i=3+1=4
4   4<=10 T Hello World            i=4+1=5
5   5<=10 T Hello World            i=5+1=6
6
7
8
9
10  10<=10T Hello World            i=10+1=11
11  11<=10F Loop Stops

 '''



