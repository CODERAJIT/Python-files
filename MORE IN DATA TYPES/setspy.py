#Sets
'''
1)Set is collections of dissimilar datatype elements.
2)sets are enclosed within curly braces {}
3)sets are mutable.
4)sets are unordered.
   In other data types index position of the element is fixed.
   but in set position of the element changes.
5)sets allows only unique values[no duplication].
'''


s={10,20,'itvedant',78.5,'eclass'}
print(s)
#type()
print(type(s))

#len()
n=len(s)
print("Total number of element in the sets :",n)

#5
'''
#print(S[1])Error

#indexing or accessing elements is not possible in set
#slicing which require index is not possible in set

#for loop over set

#for loop with index-no

for x in s:
    print(x)'''
'''
itvedant
20
10
78.5
eclass
'''

#add element in the set
'''
add(): This function is used to add element in the set.

  set_varianle.add(value)
'''
'''
s.add("itvedant_eclass")
print(s)
'''

#updating an existing value is not possible in set=> no index
#delete or remove element from set
'''
set_variable.remove(value)
'''
'''
s.remove(78.5)
print(s)'''


#del(s)
#print(s)
'''
for i  in[10,20]:
    s.remove(i)
print(s)
'''
#{'eclass', 'itvedant', 78.5}