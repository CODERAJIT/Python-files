'''

Need
If there is need to skip execution of the code for a particular iteration in a loop then we can use continue
statement to achieve it.
e.g

print Hello world for all iterations in loop except fourth iteration.

continue
=======
It is keyword
It is also associated with if condition.
when continue keyword is executed or encountered, loop control goes to increment/decrement step skipping code
for execution after continue keyword.

'''

for i in range(1,10):
    if i==4:
        continue
    print(i,"HELLO WORLD")


'''

i     i in [1,2,3...10]  i==4      print(i,"-Hello World")    i in step of 1
1     1 in []T           1==4 F    1-Hello World              2
2     2 in []T           2==4 F    2-Hello World              3
3     3 in []T           3==4 F    3-Hello World              4
4     4 in []T           4==4 T    -------------              5
5     5 in []T           5==4 F    5--Hello World             6
6     6 in []T           6==4 F    6--Hello World             7
7
8
9
10   10 in []T          10==4 F    10--Hello World           11
11   11 in []F

'''