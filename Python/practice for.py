# Print all numbers from 1 to 10.
# for i in range(1,11):
#     print(i)

# Print even numbers from 1 to 50.
# for i in range(2,51,2):
#     print(i)

# Print all odd numbers between 1–20 using while.
# total = 0
# for i in range(1,11):
#     total += i
# print('Sum = ', total)

# Print all odd numbers between 1–20 using while.
# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         print(i, end='')
#     i += 1

# Display the square of numbers 1–5.
# for i in range(1,6):
#     print(f'{i} = {i**2}')

# # Print characters of a string using for.
# for ch in "PYTHON":
#      print(ch)

# # Print multiplication table of 7.
# n = 7
# for i in range(1,11):
#      print(f'{n} * {i} = {n*i}')

# # Calculate factorial of a number.
# num = int(input('Enter a number:'))
# fact = 1

# for i in range(1, num + 1):
#      fact *= i
# print('Factorial = ', fact)


# # Count digits in an integer.
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits:", count)
# Medium
# Find the sum of all even numbers between 1–100.
# sum_even = 0
# for i in range(2, 101, 2):
#     sum_even += i
# print('Sum of even numbers between 1-100:', sum_even)

# # Display Fibonacci series up to N terms.
# n = int(input('Enter number of terms:'))
# a,b = 0,1
# print('Fibonacci Series:')
# for i in range(n):
#     print(a, end='')
#     a,b =b,a+b

# Reverse a number using a while loop.
# num = int(input('Enter a number:'))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print('Reversed number:', rev)

# Check if a number is a palindrome.
# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# if temp == rev:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")

# Find prime numbers between 1–100.
# for num in range(2,101):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#     else:
#         print(num,end='')

# Display pattern:
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     print('*'*i)

# Calculate sum of all numbers entered by user until they type 0
# total = 0
# while True:
#     num = int(input('Enter a number(0 to stop):'))
#     if num == 0:
#         break
#     total += num
# print('Total sum:', total)

# Print the following pattern:
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# Create a simple menu using while:

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Exit
# 1:-
# while True:
#     print('\nMenu:')
#     print('1. Add')
#     print('2. Subtract')
#     print('3. Multiply')
#     print('4.Exit')

#     choice = int(input('Enter your choice: '))

#     if choice == 4:
#         print('Exiting program...')
#         break

#     a = int(input('Enter first number: '))
#     b = int(input('Enter second number: '))

#     if choice == 1:
#         print('Result:', a + b)
#     elif choice == 2:
#         print('Result:', a - b)
#     elif choice == 3:
#         print('Result:', a * b)
#     else:
#         print('Invalid choice ! Try again.')

# 2:-
# while True:
#     choice = int( input('Enter your choice(1:Add, 2:Sub, 3:Mul, 4:Exit):'))

#     if choice == 4:
#         print('Exiting program...')
#         break
#     elif choice not in (1,2,3):
#         print('Invalid choice! Try again.')
#         continue

#     a = int(input('Enter first number:'))
#     b = int(input('Enter second number:'))

#     if choice == 1:
#         print('Result:', a + b)
#     elif choice == 2:
#         print('Result:', a - b)
#     elif choice == 3:
#         print('Result:', a * b)
#     else:
#          print('Invalid choice ! Try again.')