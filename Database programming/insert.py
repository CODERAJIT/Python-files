'''
Insert record into database table
=================================

step1:- connect with database.
s2- create cursor
s3:- write sql query to insert record into database.
s4:- commit the change. (save)

step2:- create cursor
s1:- cursor is a temporary space given by database
s2:-managment system to store and execuet query.
s3:-cu=db.cursor()

step3:- rite query to insert record into database table.
s1:- insert into tablename(col1,col2,....,coln)values(val1,val2,.....,valn)
s2:-insert into employee(name,dept,sal)values('harry','it',70000)

step4:- Execute query with cursor
        cu.execute(query)

step5:- commit the changes or save it
       db.commit()

'''

import pymysql

try:

    db = pymysql.connect(host="localhost", user="root", password="", database="company")
    cu = db.cursor()  # without this cursor function we can't insert record in database
    q = "insert into employee(name,dept,sal)values('Mac','HR',60000)"
    q = "insert into employee(name,dept,sal)values('arrya','CS',90000)"
    cu.execute(q)
    db.commit()  # it is use to save the data which we have written, without this coude won't execuite
    print("Record inserted secuessfully")

except Exception as e:
    print("Error:", e)


