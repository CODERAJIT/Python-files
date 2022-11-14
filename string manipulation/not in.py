
'''
user enter number between 1 and 10. if user entered number
as 8,9 then program must print invalid number otherwise it
must print valid number

'''



n=int(input("Enter your Number :"))

if n not in(8,9):
    print("Number is valid : ")
else:
    print("Number is invalid")
