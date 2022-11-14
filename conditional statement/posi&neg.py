'''
A number is entered by user , check whether number is positive
or negative number or not.


                        ------------------------
                       -3  -2  -1  0  1  2   3
                         negative< 0 > positive
positive: number must be greater than zero
negative: number must be less than zero
'''

print("enter number")
n=int(input())
if n>0:
    print("positive Number")
elif n==0:
    print("neutral number")
else :
    print("negetive Number")