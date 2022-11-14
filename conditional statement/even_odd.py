'''
A number is entered by User. Write a program to check whether
number is even or odd number.

even: The number which is completely divisible by 2.
      Since it is completely division its remainder of
      the division is Zero.
      opertor:%
'''

print("enter number")
n=int(input())
r=n%2
if r==0:
    print("Even Number")
else:
    print("Odd Number")