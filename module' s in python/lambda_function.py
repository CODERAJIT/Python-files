#Lambda function

#passing values to arguments by written lambda function

'''
n1=int(input("enter first value:"))
n2=int(input("enter second value:"))

a=lambda x,y:x+y
res=a(n1,n2) #taking vales from the user using lambda function
print("addition:",res)


a=lambda x,y:x+y
res=a(10,20) #return vales to the variables
print("addition:",res)
'''

#Squar root of given number using lambda function

n=int(input("enter number:",))
s=lambda x:x**2
sqrt=s(n)
print("squar root of :", sqrt)