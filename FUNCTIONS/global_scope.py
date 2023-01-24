'''
scope of variable
=================
The region the program where value of the variable can be accessed is called as
scope of variable.

or
life of a variable.

There are two types of scope:
1)Local Scope
2)Global Scope


'''
'''
x=10
print("value of the variable :",x)
def global_scope():
    print("value of the variavble in function",x)
global_scope()
'''
'''
value of the variable : 10
value of the variavble in function 10
'''
#global scope
'''
The variable that is defined outside the function and whose value can be accessed
outside as well as inside the function is called as Global Variable.

'''
#local scope
def scope_variable():
    x=40
    print(x)
scope_variable()
print(x)