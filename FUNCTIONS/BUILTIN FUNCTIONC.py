
l=[10,3,2,-1,20,34]
print(l)
#[10, 3, 2, -1, 20, 34]
'''
Need of Function:
================
Reusability of code.

What is function?
=================
Portion  or pieace of code defined once and called n number of
times when required is called as Function.

Types of functions
==================
1)Built in Function
2)user defined function
'''

#built in Functions

#SORTED()
'''
lsort=sorted(l)
print(lsort)
'''
#[-1, 2, 3, 10, 20, 34] ansd

#reversed using sorted()
'''
lrev=sorted(l,reverse=True)
print(lrev)
'''
#[34, 20, 10, 3, 2, -1] desnd

#pow()

'''
pow(n,p): It is used to calculate one number raised to another number.

                2^3=8 n=2 p=3
'''

p=pow(2,3)
print(p)

#8

#sum()
'''
sum():Used to find integer sum of the elements in iterable.
'''

tot=sum(l)
print("summation number of elements in list :",tot)

#summation number of elements in list : 68


