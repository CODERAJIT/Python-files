'''

variable length argument
========================

variable:changing

length:number of argument

'''

'''
def addition(x,y):
    z=x+y
    print("addition is:",z)
addition(10,20)
'''
'''
addition(10,20,30)
# addition() takes 2 positional arguments but 3 were given
'''
'''
addition(50)
#addition() missing 1 required positional argument: 'y'
'''
  
def addition(*x):
  #print(x)
  #print(type(x))
  sum=0
  for i in x:
   # print(i)
    sum=sum+i
  print("summation of argumets is :",sum)

addition(20,30)
addition(20,30,70)
addition(50)

'''
<class 'tuple'>
20
30
<class 'tuple'>
20
30
70
<class 'tuple'>
50
'''
'''
summation of argumets is : 50
summation of argumets is : 120
summation of argumets is : 50
'''
#addition(20,30)
#x=(20,30)

'''
i  i  in x    sum=sum+i      i
20 20 in x[T] sum=0+20=20    30
30 30 in xT   sum=20+30=50      --F

summation is:50

'''
#addition(20,30,40)
#x=(20,30,40)

'''
i   i in x    sum=sum+i    i

'''
