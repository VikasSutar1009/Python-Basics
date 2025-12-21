def bmi(weight, height):
    return weight / (height ** 2)

result = bmi(70, 1.75)
print("BMI:", result)




# calculate sqare 
def sqare(num):
    return num ** 2

nums = sqare(6)
print(nums)


# calculate cube
def cube (num):
    return num ** 3

result = cube(3)
print(result)

# evenodd
def even_odd(num):
    if num % 2 == 0 :
        print("even")
    else:
        print("odd")

result = even_odd(10)
print(result)