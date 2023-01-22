
'''
list
====
1)List is collection of dissimialr datatype elements.
2)Element in list are enclosed in square brackets.
3)List is mutable.[Once defined they can be changed.]
'''

#define list

l=[10,89.7,-3,45,'itvedant']

print( "list is :",l)
print(type(l))

'''
[10, 89.7, -3, 45, 'itvedant']
<class 'list'>
'''

#len

'''

n=len(l)
print(n)

'''

#indexing

'''

print(l[3])
print(l[-4])

'''


#slicing

'''

l1=l[1:4:1]
print(l1)

'''
#reversed list with slicing

'''

lrev=l[::-1]
print(lrev)

'''

# ['itvedant', 45, -3, 89.7, 10]

#for loop over list

'''
for i in range(0,len(l),1):
    print(l[i])
    
'''


'''
10
89.7
-3
45
itvedant

'''

'''
for i in l:
    print(i)
'''


'''
10
89.7
-3
45
itvedant

'''



#append()
'''
l.append(23.3)
print(l)
'''

#[10, 89.7, -3, 45, 'itvedant', 23.3]

'''
l.append('eclass')
print(l)
'''
#[10, 89.7, -3, 45, 'itvedant', 23.3, 'eclass']


#insert()
'''`
l.insert(3,50)
print(l)
`'''
#[10, 89.7, -3, 50, 45, 'itvedant']


#Update list element
'''
l[4]="Itvedant-Eclass"
print(l)
'''
#list is : [10, 89.7, -3, 45, 'itvedant']
#[10, 89.7, -3, 50, 'Itvedant-Eclass', 'itvedant']


#delete or remove elements in list
#list is : [10, 89.7, -3, 45, 'itvedant']
'''
l.pop()
print(l)
'''
#[10, 89.7, -3, 45]


'''
l.pop(2)
print(l)
'''
#[10, 89.7, 45, 'itvedant']


#del : this keyword is used to delete the entire list at  once.

'''
del l
print(l)

'''

