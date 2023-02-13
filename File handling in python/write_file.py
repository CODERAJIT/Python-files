'''
Writing into file
=================
Write(): This function is used to write date into file.

syntax:

    file_pointer.write(data)





      data.txt                                   write_file.py                     IDLE Shell
   -------------                               --------------------             ---------------
                         write()                                     input()    enter mobile No:
                    <----------------      mn=input()              <-----------


'''

fp=open('data.txt','w')
#d="This is first line in this file" #here we're giving data to print
#fp.write(d)

mn=input("enter mobile number:") #taking input from user in files
fp.write(mn)
fp.close()

'''
if a file is open in write mode and it has previous data, then new data
get overwritten on the previous data.

OTP generated
1.send to user mobile number
2.store in database or file in web application.

when user enter otp

for verfication
OTP entered by user is matched with the otp stored in file.
if above condition is true then user mobile is verified. 
'''