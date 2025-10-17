# Program to check prime number:
num =int(input("Enter a number:"))
if num > 2:
    for i in range(2,num):
        if num % 2 == 0:
            print("Number is not prime number")
            break
    else:
            print("Number is prime number")
else:
        print("Number is not prime number")



# Generate Fibonacci series up to N terms

n = int(input("Enter number of terms: "))  

a, b = 0, 1   
count = 0     

while count < n:        
    print(a, end=" ")   
    a, b = b, a + b     
    count += 1          