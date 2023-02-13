class customer:

    def __init__(self):

        self.bname="SBI"
        self.ifsc="SBIN123456789"
        self.loc="Eclass"

    def getdata(self):

        self.name=input("enter customer name:")
        self.mob=input("enter mobile number:")
        self.bal=float(input("enter account opening balance:"))

    def display(self):
        print("bank details:")
        print("------------------")
        print("bank name:",self.bname)
        print("bank IFSC code:",self.ifsc)
        print("bank Location:",self.loc)
        print()
        print("Customer details")
        print("-------------------")
        print("customer name:",self.name)
        print("customer mobile:",self.mob)
        print("customer balance:",self.bal)


c1=customer() #object created => constructor is called
c1.getdata() #getdata(c1)
c1.display() #display(c1)
print()
c2=customer()#2nd object creation=
c2.getdata() #getdata(c2)
c2.display() #display(c2)


'''

                            c1
                             |
        ------------------------------------------------
        |       |              |     |    |     |
        bname  ifsc           loc    name mob   bal
        SBI    SBIN123456789  Eclass



'''