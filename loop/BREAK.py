'''
break keyword:

Need of break keyword
=====================
Ideally loop stop working when condition become false.
If there is need  to stop loop even the condition of the loop is true, then there is need of break
keyword.

break keyword [It has reserved meaning]
=============
break is a keyword which is used to stop or terminate loop even if the loop condition is True.
break is always associated with if statement in loop i.e break keyword does its work to terminate
the loop based on certain condition.

'''


for i in range(0,10):
    if i==5:
        break
    s=i+1
    print(s)

print("out of loop")
'''
1
2
3
4
5
out of loop
'''
for i in range(1,10):
    if i==5:
        break
    print(i)

print("out of loop")
'''
1
2
3
4
out of loop
'''

'''
i    i in [1,2,3,...10]   i==5        print(i)     i with 1 step
1    1 in []T             1==5 F      1            2
2    2 in []T             2==5 F      2            3
3    3 in []T             3==5 F      3            4
4    4 in []T             4==5 F      4            5
5    5 in []T             5==5 T    break ==> loop stops


'''
