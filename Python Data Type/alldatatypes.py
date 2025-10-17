#text type
text="Hello, World" #str

#numeric types
integer_num=10        #int
float_num=10.5        #float


#sequence types
my_list=[1,2,3]      #list
my_tuple=(1,2,3)     #tuple
my_range= range(1,4) #range

#mapping type
my_dict = {'name':'Alice','age':25}  #dict

#set types
my_set= {1,2,3}                 #set

#boolean type
is_valid=True       #bool


#printing all values with their types
print("text Type:",text,type(text))
print("integer:",integer_num, type(integer_num))
print("float:", float_num, type(float_num))
print("list:", my_list, type(my_list))
print("tuple:", my_tuple, type(my_tuple))
print("range:",list(my_range), type(my_range))
print("dictionary:", my_dict, type(my_dict))
print("set:", type(my_set))
print("boolean:", is_valid, type(is_valid))
