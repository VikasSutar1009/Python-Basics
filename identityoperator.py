x=[1,2,3]
y=x            #y refers to the same object as x
z=[1,2,3]      #z is a different object with the same content

#Identity: is
print("x is y:",x is y)  #True(same object)
print("x is z:",x is z)  #False(different object)

#Identity: is not
print("x is not z:",x is not z)  #True
