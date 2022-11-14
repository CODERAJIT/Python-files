'''
code editor  ------print()-----> console(output screen)

If there is need to bring user input from output screen or
console to the code editor or to store in a variable, we need
input() function.

syntax:

   variable=input()

step1: Give message to user           => print()
step2: store that input into variable => var=input()
'''


'''
print ("enter your first number")
x=input()
#print ("value of x is :",x)
print ("enter your second number")
y=input()
z=x+y
print ("addintion  of ",x, "and",y,"is :",z)

'''


'''
print ("enter your first number")
x=input()
print (type (x))
a=int(x)
print (type(a))

'''
print ("enter your first number")
x=input()
a=float(x)
print ("enter your second number")
y=input()
b=float(y)
z=a+b
p=x+y
print ("conat /joined  of ",x, "and",y,"is :",p)
print ("addintion  of ",a, "and",b,"is :",z)
