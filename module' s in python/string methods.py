'''
s="Itvedant_Eclass"
print(s)
print(type(s))

sup=s.upper()
print(sup) #output:- ITVEDANT_ECLASS

slow=s.lower()
print(slow) #output:- itvedant_eclass
'''

#String Methods

#isalpha()
'''
This method check whether entrire string contains alphabets.if all string elements are
alphabets then it return true or it returns false.
'''
'''
s="Itvedanteclass"

r=s.isalpha()
print(r)
'''

#isdigit():
'''
This method is used to check whether string elements are digits i.e 0,1,2,3,....,9
it returns true string contains all digits.
it returns false if string contains other than digit.
'''
'''
s="12345678"
r=s.isdigit()
print(r)
'''

#split():
'''
When there is need to convert a string into list, split() method is used.

syntax:
======

   str_variable.split('separator')

'''
'''
s='We are leaning-String method-in todays-class'
print(s)
#l=s.split(',')
l=s.split('-')
print(l)
print(type(l))
'''
'''
output:-

We are leaning-String method-in todays-class
['We are leaning', 'String method', 'in todays', 'class']
<class 'list'>
'''

s='We are leaning String method in todays class'
print(s)
l=s.split(' ')
print(l)
#defult separator is space. in above code we're not given anything as a separator hence it taking as default


'''
output:-
We are leaning String method in todays class
['We', 'are', 'leaning', 'String', 'method', 'in', 'todays', 'class']
'''



'''
home work:-
===========
#join() => iterable 
#replace() =>
'''

#join():-join() method is use to take all itrable and join into one string

s=("hello")
r=s.join("hey")
print(r)  #output:- hhelloehelloy

#replace():- replace is use to replace with specific string into another specific string

#syntax:- string_variable.replace("old_value","new_value)

s=("I like the way your")
r=s.replace("I like the","I'll be the") #output:- I'll be the way your
print(r)




