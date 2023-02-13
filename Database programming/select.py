'''
Retrive all records from database table
=======================================
sql query to retrieve all records from database

select *from tablename;
'''

import pymysql

try:

    db=pymysql.connect(host="localhost", user="root",password="",database="company")
    cu=db.cursor()
    q="select * from employee"
    cu.execute(q)
    data=cu.fetchall() #this fetchall function is use to fetch data from database and display in python result file
    print("Data in the table:")
    print(data)

except Exception as e:

    print("error:",e)

'''

                      cu.execute(q)              id  name      dept    sal
                      fetch()    1                1   harry
                   Dtata<=====   2    <=====      2   mac
                                 3                3   rox

'''