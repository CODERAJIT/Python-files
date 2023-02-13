import arithmetic as ar


a=int(input("enter first number:"))
b=int(input("enter second number:"))

res=ar.addition(a,b)
print("addition is:",res)

res=ar.subtraction(a,b)
print("subtraction is:",res)

res=ar.multiplication(a,b)
print("multiplication is:",res)

res=ar.division(a,b)
print("division is:",res)