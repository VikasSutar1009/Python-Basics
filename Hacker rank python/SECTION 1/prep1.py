# print Hello, Wrorld !
print('Hello, World !')

# odd or even
# Input an integer, and print whether it's odd or even
num = int(input('Enter a number'))
if num % 2 == 0:
    print('even')
else:
    print('odd')

# Largest of Three Numbers
# Take 3 numbers as input and print the largest.
a= int(input('enter first no:'))

b= int(input('enter second no:'))

c= int(input('Enter third no:'))

largest = max(a,b,c)
print('Largest no is:', largest)

# Sum of N Natural Numbers
# Input: N → Output: Sum = 1 + 2 + ... + N
n = int(input('enter no:'))
sum = n*(n+1)
print('sum=', sum)


# Leap Year Checker
# Check if the given year is a leap year.
year = int(input('Enter year'))
if(year % 4== 0 and year % 100!= 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

# Simple Interest Calculator
# Formula: (P × R × T) / 100
P= float(input('enter principle:'))
R= float(input('enter rate:'))
T= float(input('enter time:'))
SI = (P * R * T) / 100
print('simple interest= ',SI)

# Swap Two Numbers Without a Temp Variable
# Use arithmetic or tuple unpacking.
a= int(input('enter first number (a):'))
b= int(input('enter second number (b):'))

print(f'\nbefore swapping: a = {a}, b = {b}')

a,b = b, a
print(f'After swapping: a = {a}, b = {b}')