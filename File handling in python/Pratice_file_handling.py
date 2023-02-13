# File handling:- open(), close(), read(),write(),appended

'''
fp=open('file.txt','w')
d=input("enter the txt:")
output=fp.write(d)
print(output)
fp.close()
'''
# read()
'''
fp=open('file.txt','r')
d=fp.read()
print(d)
'''
# readline()
'''
fp=open('file.txt','r')
d=fp.readline()
print(d)

print(d[0])
print(d[1])

for i in d:
    print(i)

'''

# appended()

fp = open('file.txt', 'a')
d = fp.write("world")
print(d)

x = input("enter mobaile number:")
y = fp.write(x)
print(y)
fp.close()