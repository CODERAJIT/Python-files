'''
Need of module
==============

Reusing functionality

   one.py           two.py                 third.py
------------       -----------          ----------------

def addition(x.y):  def addition(x,y)    def addition(x,y)

z=x+y               z=x+y                  z=x+y
print(z)           print(z)                print(z)

in above example function addition is defined in all the files which led to repeation of code.

In order to avoide this repeatition code,create a python file and define addition function in the python file and impory that python
file in another python files such as one.py,two.py,three.py.

The python file that is import in another file is called as module in python.






                                      arthmetic.py  =>module
                                    -----------------
                                    def addition(x,y):

                                    z=x=y
                                    print(z)
                                      |
                                      |
                   --------------------------------------------------------
                   |                    |                                 |
              one.py                two.py                           third.py


what is module?
==============
Module is pyhton files whicg is collection of functions,constantsand classes.

types of modules
================
1.build in modules
2.user defined modules
3.packages
'''