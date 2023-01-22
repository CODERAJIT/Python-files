#find a number of vowels and consonants in the string entered by user.

str=input("enter your string :")
print(str)
v=0
c=0
for x in str:
    if x in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    else:
        c+=1

print("Total Number of Vowels",v)
print("Total Number of Consonants",c)
