# Check four digit armstrong number
print("Enter your four digits number :")
x=input()
n=int(x)

a=n%10 #8208%10=8
b=n//10 #8208//10=820
c=b%10 #820%10=0
d=b//10 #820//10=82
e=d%10 #
f=d//10

su=a**4+c**4+e**4+f**4

if su==n:
    print("this is a armstrong number ")
else:
    print("this is  not a armstorng number")