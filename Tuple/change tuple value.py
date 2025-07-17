x=("apple","banana","cherry")  #original typle before update
y= list(x)   #converted to list
y[1]= "kiwi"  #change the list
x=tuple(y)  #converted to tuple

print(x)  #print updated tuple
