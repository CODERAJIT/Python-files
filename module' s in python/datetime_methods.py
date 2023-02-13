'''

                         datetime
                            |
           ------------------------------------
           |                |                  |
        date              time              datetime  1 level
                                               |
                                                 -year()
                                               |
                                                 -month()   2nd level
                                               |
                                                 -day()
                                               |
                                                 -now()


'''

#create datetime
'''
datetime(year,month,day,hour,minute,second)

'''

import datetime
'''
dt=datetime.datetime(2022,11,21)
print(dt)

dt1=datetime.datetime(2022,11,21,20,25,45)
print(dt1)
'''
'''
output:-
2022-11-21 00:00:00
2022-11-21 20:25:45
'''

#To extract system date and time use now() method

sysdt=datetime.datetime.now()
print(sysdt) #2022-12-09 19:33:02.682685

#current year using year() method

year=sysdt.year
print("year:",year)
m=sysdt.month
print("month:",m)
d=sysdt.day
print("day:",d)
h=sysdt.hour
print("hour:",h)
min=sysdt.minute
print("minute:",min)
sec=sysdt.second
print("second:",sec)

'''
output:-

2022-12-09 19:43:54.863634
year: 2022
month: 12
day: 9
hour: 19
minute: 43
second: 54

'''