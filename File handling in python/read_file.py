'''
Reading data from file.

read(): This method is used to read entire data from the file.

Syntax:-

      file_pointer.read()

readlines():
    This method read the files line by line and returns list of lines.

    data.txt               read_file.py                    console
              read()                       print()
           ------------->d               ------------->

'''
fp=open("data.txt",'r')

d=fp.read()

print("data in the file is:")
print(d)