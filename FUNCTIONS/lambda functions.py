'''
Functions are divided into two main parts:
1)Built in Function.
2)User defined function.
   -user defined function is divided into two parts
      1) Lambda function(anonymous function)
      2) recursive function

Lambda Function
===============
Need of function
----------------
1)Single it is one line function,it has faster execution.
  [Shorter the code,faster is execution]
2)If there is need to pass a function as an argument to another
  function, then use lambda function to pass as an argument.

Function without name is called as Anonymous function or lambda
function.
lambda function always returns result of the expression.

syntax for lambda function definition:
=====================================

var=lambda arguments:expression

to call lambda function
----------------------
var(arguments)

'''
a=lambda x,y:x+y  #lambda 20,30:20+30
res=a(20,30) #lambda call
print("summation is :",res)
#summation is : 50