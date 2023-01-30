'''
Recursive function
==================
Recursion

 1
---=0.333333333333333333333 => Recurring  => 0.334
 3
Recursive
=========
When function call is given inside function body or definition
then that function is called as Recursive function.

When a function call is detected in function body,it goes
into never ending loop. So there is need to frame a condition
to stop recursion.
'''
i=1
def abc():
    global i
    print("hello",i)
    i+=1
    abc()
abc()