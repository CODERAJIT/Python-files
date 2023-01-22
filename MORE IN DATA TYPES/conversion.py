#conversion
#list,tuple,and set

t=(10,20,30,40)
print(t)

print(type(t))
#<class 'tuple'>

#convert tuple into  value
l=list(t)
l[2]=300
print(type(l))
    #<class 'list'>

#changing elements value

#l=(10, 20, 30, 40)
l[2]=300
print(l)
    #[10, 20, 300, 40]
tnew=tuple(l)
print(tnew)
    #(10, 20, 300, 40)
print(type(tnew))
    #<class 'tuple'>

