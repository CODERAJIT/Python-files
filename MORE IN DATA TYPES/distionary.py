'''
1)Dictionary is also a collection of dissimilar elements.
2)Elements in dictionary are arranged in key:value format.
3)They are mutable.
4)keys are unique and values can be duplicated.
5)Elements are enclosed in curly braces.

'''
d={'a':'apple','b':'ball',2:'two',10:100}
print(d)
print(type(d))

    #{'a': 'apple', 'b': 'ball', 2: 'two', 10: 100}
    #<class 'dict'>
#len()
'''
n=len(d)
print("Total Number of elements in the dictionary",n)

#Total Number of elements in the dictionary 4
'''
#indexing or accessing with index=no since there is no index.
#But since there is key which is unique we can access element
#value using key
'''
   dictionary_variable[keyname]
'''
'''
print(d['b'])
print(d[10])
'''
    #ball
    #100

#slicing not possible as it require index.

#for loop
#for loop using index is not possible
'''
for x in d:
    #print(x)

    print(d[x])
'''
    #keys #print(x)
'''
a
b
2
10
'''
    #values #print(d[x])
'''
apple
ball
two
100
'''

#add element in Dictionary
#d={'a': 'apple', 'b': 'ball', 2: 'two', 10: 100}
'''
d['c']='cat'
print(d)
'''
    #{'a': 'apple', 'b': 'ball', 2: 'two', 10: 100, 'c': 'cat'}

#update or add element in dictionary
'''
d['c']='cat'
print(d)
    #{'a': 'apple', 'b': 'ball', 2: 'two', 10: 100, 'c': 'cat'}
'''
'''
d['b']='bat'
print(d)
    #{'a': 'apple', 'b': 'bat', 2: 'two', 10: 100}'''

#to remove elements in dictionary
#to remove element in Dictionary
'''
pop()
syntax:
       d.pop(keyname)
'''

#d.pop(2)
#print(d)
    #{'a': 'apple', 'b': 'ball', 10: 100}

#del d (for delete)

