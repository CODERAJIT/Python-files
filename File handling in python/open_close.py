'''
Functions in file handling:-

1. open():
This function is used to open a file for reading,writing and appending data from the file.

Syntax:

   open('filepath',mode)

filepaths : its a file relative path with the help of which python file
is accessing the file which is used to store data.

mode: There are three modes used for opening.
      read => r : To read from the file
      write => w :To write in file
      append => a : To write in file with appending.

open() Function retun file pointer i.e reference of the file in the python file.

close(): This function is used to close file and save data into the file

'''

fp=open('data.txt','w')
print(fp)

fp.close()