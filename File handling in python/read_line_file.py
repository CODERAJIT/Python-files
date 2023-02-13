'''
readline():
This method read files line by line and return list of lines

'''

fp=open("data.txt",'r')
d=fp.readlines()

print("data in the file:")
print(d)

print(d[0])
print(d[1])

print("using for loop")
for x in d:
    print(x)

'''
output:-

============ RESTART: C:/9.file handling in python/readline_file.py ============
data in the file:
['8970368241\n', '9964112908\n']
8970368241

9964112908

using for loop
8970368241

9964112908
'''