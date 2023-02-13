'''
In database, data is stored in the form of table.

By using Mysql DBMS
steo1:- create database. => Done
step2:- Create table inside database to store record.

    tablename:employee
    table employee stores employee information

         name   dept   sal
        -------------------
        Harry   It     70000
        Mac     HR     60000
        Shree   IT     95000

Number of columns:4

column name      datatype
id               int
name             varchar(size)=> size:number of character
dept             varchar(size)
sal              float

Table creation done.

              write()
           ------------>
    .py file          data.txt
           <------------
           read(),readlines()


                             database

                             employee

            insert query     id name  dept  sal
            ------------->
     .py file

           <-------------
            select query

1. insert record from python into database table
2. retrive all records from database table into python file
3. delete record from database table from python file.
4.update record from database table from python file.

 CRUD
 C=> create
 R=> read
 U=> update
 D=> delete



praticaly
========

step1:-open xampp:- start mysql and apacha
step2:-http://localhost/dashboard/
step3:- phpMyadmin
step4:- in that create database => then database name we should enter database name which name we have to create
'''