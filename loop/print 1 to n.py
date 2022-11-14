'''
i   i<=10     print(i)   i=i+1
1   1<=10 T   1          i=1+1=2
2   2<=10 T   2          i=2+1=3
3   3<=10 T   3          i=3+1=4
4   4<=10 T   4          i=4+1=5
5
6
7
8
9
10  10<=10T   10         i=10+1=11
11  11<=10F

'''

n=int(input("Enter   your Last number"))
i=1
while i<=n:
    print(i)
    i+=1
