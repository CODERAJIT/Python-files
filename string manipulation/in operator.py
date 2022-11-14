'''
Write a program to check whether character entered by
user is vowel or consonant.

vowels=> a,e,i,o,u,A,E,I,O,U
consonants: Other than vowels are consonants.

in and not in are called as membership operators.
'''



ch=input("enter your Charcter: ")
if ch in('i','e','a','o','u','A','E','I','I','O','U'):
    print("Its a Vowel")
else:
    print("Its is a Consnent")