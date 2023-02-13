'''
Data member and Methods

'''


class student:

    def getdata(self):  # self=s1

        self.name = input("enter student name:")  # itvedant
        self.rno = input("enter Rool number:")  # 35

    def display(self):
        print("student name:", self.name)  # s1.name
        print("student roll number:", self.rno)  # s1.rno


s1 = student()  # object created

s1.getdata()  # getdata(s1)
s1.display()  # display(s1)

s2 = student()  # second object created
s2.getdata()  # getdata(s2)
s2.display()  # display(s2)

'''

                            self=s1
                               |
                    ------------------------
                    |                       |
                   name                    rno
                itvedant                    35



                            self=s1
                               |
                    ------------------------
                    |                       |
                   name                    rno
                Eclasss                     56


'''