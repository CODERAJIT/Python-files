'''
try..except..finally

finally block is executed in both situation
1.if there is exception.
2.if there is no exception.

'''
try:
    x=int(input("enter numerator:"))
    y=int(input("enter denominator:"))
    d=x/y
    print("Division is:",d)

except Exception as x:

    print("Error:",x)

finally:

    print("inside finally block")

'''
Whenever a transation of inserting record, retrieve records
update record and delete record with the database is completed,
it is a good practice to close connection of your code with
databse,so that data is secured.


        python---connection--->database[to perform operations]

    And even if exception arises, then connection to the database must be closed.

'''