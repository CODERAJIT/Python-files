'''
connecting python with mysql database management system.
=======================================================

python and mysql are different platfrom. In order to establish
connection between python and mysql, there is need of cpnnector.
That connector is called as pymysql module.


         python                             mysql
                        pymysql
          .py file -----------------> database


To onstall any external module use following command on cmd prompt.

syntax:

pip install modulename

e.g. install pymysql
pip install pymysql

pip is a package installaction manger,whse duty is to download and install
all readymade packages in python.

connect(): This function connect python with mysql database

syntax:

pymysql.connect(host="localhost", user="root", password="", database="databasename")

pymysql.connect(host="localhost", user="root", password="", database="company")


example:--
fp=open("data.txt",'r')
fp was a reference object of data.txt file in python.

db=pymysql.connect(host="localhost", user="root", password="", database="company")

db is a reference object of that batabase in python file
'''

import pymysql
try:

    db=pymysql.connect(host="localhost", user="root", password="1234", database="company")

#print(db)
    print("connected successfully")

except Exception as e:

    print("Error:",e)