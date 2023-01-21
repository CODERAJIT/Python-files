'''

prime number
============

A numebr which is completely divisible by 1 and itself is called as prime number

7 is prime number=> 7 is completely divisible by 1 and 7

8 is also completly divisible by 1 and 8, but 8 is non prime number.

n=7

   1     2 3 4 5 6    7
         ---------
  excluding 1 and 7 check whether any number completly divides 7, so none of in between numbers completly divides 7, thus
  it is prime number.

n=9

   1    2 3 4 5 6 7 8   9
        -------------

  Excluding

'''
n=int(input("enter Your Number : "))
for i in range(2,n,1):
    r=n%i
    if r == 0:
        print("Non Prime Number")
        break
    '''else:
        print("its a prime number ")
'''
else:
    print("it is a prime Number")

'''
n=6

i   i in [2,3,4,5]   r=6%i     r==0   print("Non-prime")    i=i+1
2   2 in[]T          r=6%2     0==0T  Non-prime             i=3
3   3 in[]T          r=6%3     0==0T  Non-prime             i=4
4   4 in[]T          r=6%4=2   2==0F   -----                i=5
5   5 in[]T          r=6%5=1   1==0F   -----                i=6
6   6 in[]F


'''
