# 1.Simple function
def greet():
    print("Hello World")

# 2. Function with parameters
def add(a,b):
    return a + b

# 3. Function with return
def square(x):
    return x * x

# 4. Function withour return
def show_msg():
    print("Welcome")

# 5. Function with default argument
def country(name = "India"):
    print("Country: ", name)

# 6. Function calling another function
def total(a, b):
    return add(a,b)

# 7. Function with list input
def total_marks(marks):
    return sum(marks)

# 8. Function with String input
def uppercase(text):
    return text.upper()

# 9. Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

# 10. Function returning multiple values
def math_ops(a,b):
    return a+b, a-b, a*b

