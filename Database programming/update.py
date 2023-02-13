'''
Updating a specific record
==========================

Arrya=>mac   CS=>IT   90000=>75000

sql query to update a record
============================
update tablename set colname1=newval1,colname2=newval2
                     colnamen=newvaln where id=valname

'''

import pymysql

try:

    db = pymysql.connect(host="localhost", user="root", password="", database="company")
    cu = db.cursor()
    q = "update employee set name='mac', dept='HR', sal=75000 where id=2"
    cu.execute(q)
    db.commit()
    print("record update successfully")


except Exception as e:

    print("error:", e)