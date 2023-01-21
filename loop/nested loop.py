'''
Nested Loop
===========
One loop inside another loop is called as Nested Loop.
There is a outerloop and ther is a inner loop.

'''

for i in  range(1,4,1):
    print("i : ",i)
    for j in range(1,5,1):
        print(j)


'''
                                  --------------------------------
                                |             j loop              |
i   i in [1,2,3]   print(i)     j    j in [1,2,3]   print(j)    j=j+1       i=i+1
1   1 in []T        1           1    1 in []T       1           j=2
                                2    2 in []T       2           j=3
                                3    3 in []T       3           j=4
                                4    4 in []F                               i=2

2   2 in []T        1           1    1 in []T       1           j=2
                                2    2 in []T       2           j=3
                                3    3 in []T       3           j=4
                                4    4 in []F                               i=3

3   3 in []T        1           1    1 in []T       1           j=2
                                2    2 in []T       2           j=3
                                3    3 in []T       3           j=4
                                4    4 in []F                               i=4

4   4 in []F

'''
