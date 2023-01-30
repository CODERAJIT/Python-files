'''
summation  of 1 to n using Recursion.
'''
num=int(input("Enter last term in in the series :"))
def summation(n):
    if n==1:
     return 1
    r=n+summation(n-1)
    return r
res=summation(num)
print("Summation is :",res)
'''
res=summtion(4)=>10
   |
   |
def summation(4):  ----def summation(3): --def summation(2): ---def summation(1):
                  |                     |                   |
    if 4==1: F    |      if 3==1: F     |    if 2==1: F     |     if 1==1: T
                  |                     |                   |        return 1
  10r=4+summation(3)    6r=3+summation(2)    3r=2+summation(1)              |
      |        |           |        |           |           |               |
    return()
'''


