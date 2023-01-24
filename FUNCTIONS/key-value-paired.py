'''
1. required argument
2. Default argument
3. Key value pair argument.
   key=value


   area of rectangle=length x breadth

           3
    ---------------
   |               |
   |               | 2    area=3x2=6
   |               |
    ---------------
'''

def area(l,b):
    print("length of rectangle is :",l)
    print("breadth of ractangle  is :",b)
    a=l*b
    print("area of rectangle is:",a)
area(20,10)

'''
length of rectangle is : 10
breadth of ractangle  is : 15
area of rectangle is: 150
'''

#area(10,20)#corrct parameters
#area(20,10)

#area(l=10,b=20)
area(b=20,l=10)
'''
length of rectangle is : 10
breadth of ractangle  is : 20
area of rectangle is: 200
'''