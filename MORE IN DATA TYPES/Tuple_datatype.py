#tuple
'''
t=(10,20,'itvedant',89.5,'e-class')
print(t)
print(type(t))
'''
'''
(10, 20, 'itvedant', 89.5, 'e-class')
<class 'tuple'>
'''

#len

'''
t=(10,20,'itvedant',89.5,'e-class')
n=len(t)
print("Total Number of elements is Tuple :",n)

'''
#Total Number of elements is Tuple : 5

#accessing tuple elements with index
'''
print(t[2])
print(t[4])
'''
#itvedant
#e-class

#slicing in Tuple

'''

li=t[1:4:1]
l2=t[0:5:1]
print(li)
print(l2)
'''
#(20, 'itvedant', 89.5)
#(10, 20, 'itvedant', 89.5, 'e-class')

#loop over Tuple

'''
t=(10,20,'itvedant',89.5,'e-class')
for i in t:
    print(i)
    '''

'''
10
20
itvedant
89.5
e-class
'''

#tuple reversed

'''
t=(10,20,'itvedant',89.5,'e-class')
n=t[::-1]
print(n)
'''
'''
10
20
itvedant
89.5
e-class
('e-class', 89.5, 'itvedant', 20, 10)
'''

#summation of element of Tuple
'''
tu=(10,4,5,67,8,90)
sum=0
for i in tu:
    #print(i)
    sum=sum+i
print("Summation of Tuple is  :",sum)
'''

#ACCESSING TUPLE OF ELEMENTS IN TUPLE:
'''
    (10, 20, 'itvedant', 89.5, 'e-class')
      0   1     2          3       4
     -5  -4    -3         -2     -1 

'''

#Occurance:cout():it is used to count occurance of elements
# of tuple.

'''
t=(10,20,'itvedant',89.5,'e-class',10,20,10,20,10)
tc=t.count(10)
print("Occurance of elements is :",tc)
'''
#Occurance of elements is : 4


#print total number of elements in tuple
'''
t=(10,20,'itvedant',89.5,'e-class',10,20,10,20,10)

for i  in range (0,len(t)):
      if t[i]==20:
         print(i)'''

'''
1
6
8
'''
#index in tuple:index():
'''
tpos=t.index(20)
print("index position  of elements is:",tpos)
'''
#index position  of elements is: 1
