list = ['apple', 'banana', 'orange', 'mango', 'cherry', 'kiwi', 'pinapple']
print(list[2:6])
print(list[:4])

print(list[3])

list.remove[5]
print(list)

list[1:3] = ('honda','suzuki', 'hundai')
print(list)

# Print (numbers from 1 to 50)
for i in range (1,51):
    print(i)

# Print only even numbers between 1 and 100
for i in range(1,101,2):
        print(i)

# Reverse countdown
for list in range(10,0,-1):
    print(list)


# Sum of first N numbers
n = int(input("Enter a number:"))
total = 0
for i in range(1, n+1):
    total += i
    
print("sum = ", total)


# Multiplication Table
num = int(input("Enter a number:"))

for i in range (1,11):
    print(num, "X", i, "=", num * i)