'''
variable length argument => key value pair
'''
def addition(**x):
    #print(x)
    #print(type(x))
    for i in x:
        print(i)
addition(a=10,b=20)
addition(a=10,b=20,c=30)
addition(a=10,b=20,c=30,d=40)

'''
{'a': 10, 'b': 20}
<class 'dict'>
{'a': 10, 'b': 20, 'c': 30}
<class 'dict'>
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
<class 'dict'>
'''