n1=int(input("Enter your 1st number"))
n2=int(input("Enter your 2nd number"))
def calculate(x,y):
     add=x+y
     sub=x-y
     mul=x*y
     div=x/y
     return add,sub,mul,div

a,b,c,d=calculate(n1,n2)
print("addition is :",a)
print("substration is :",b)
print("multipications is :",c)
print("division  is :",d)

'''
Enter your 1st number10
Enter your 2nd number20
addition is : 30
substration is : -10
multipications is : 200
division  is : 0.5
 
'''