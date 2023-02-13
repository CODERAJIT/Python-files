#Create class name arithmatic with add(),sub(),div(),mul() function. pass the values as aruments and perform the required operations

class arithmatic:


    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self, a,b):
        return a/b

none=int(input("enter first number:"))
ntwo=int(input("enter second number:"))


a1=arithmatic()
print("addition:",a1.add(none,ntwo))
print("substruction:",a1.sub(none,ntwo))
print("multiplcation:",a1.mul(none,ntwo))
print("division",a1.div(none,ntwo))

'''
output:-

================= RESTART: C:\10.OOPs\arithmatic_assignment.py =================
enter first number:10
enter second number:5
addition: 15
substruction: 5
multiplcation: 50
division 2.0

'''