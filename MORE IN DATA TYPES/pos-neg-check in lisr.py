    #from the give list filter positive and negetive element and create two lists.

l=[1,-9,89,76,-3,0,12,15,167,-8,2]
#print(len(l))
lpos=[]
lneg=list()

for x in l:
    #print(i)
    if x>0:
        lpos.append(x)
    else:
        lneg.append(x)

print("Positive Number is :",lpos)
print("Negetive Number is :",lneg)


'''
Positive Number is : [1, 89, 76, 12, 15, 167, 2]
Negetive Number is : [-9, -3, 0, -8]
'''
