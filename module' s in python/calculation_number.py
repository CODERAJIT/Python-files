'''
Calculator: Console based Application
=====================================
1.Addition
2.subtraction
3.multiplication
4.division
5.exit

enter your choice:2

'''
while True:
    print()
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    print()
    ch = int(input("enter your choice="))  # 1,2,3,4,5 othen than 1-5
    # x=int(input("enter first number:"))
    # y=int(input("enter second number:"))

    if ch == 1:
        x = int(input("enter first number:"))
        y = int(input("enter second number:"))
        z = x + y
        print("addition is:", z)

    elif ch == 2:
        x = int(input("enter first number:"))
        y = int(input("enter second number:"))
        z = x - y
        print("subreaction is:", z)

    elif ch == 3:
        x = int(input("enter first number:"))
        y = int(input("enter second number:"))
        z = x * y
        print("multiplication is:", z)

    elif ch == 4:
        x = int(input("enter first number:"))
        y = int(input("enter second number:"))
        z = x / y
        print("division is:", z)

    elif ch == 5:
        print("exit from program, thank you for using serive!!")
        break

    else:
        print("enter valid choice between 1 to 5 !!")



