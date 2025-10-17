a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
op=input("Choose operator:,+,-,*,/")

if op == "+":
    print("Result=",a+b)
elif op == "-":
    print("Result=",a-b)
elif op == "*":
    print("Result=",a*b)
elif op == "/":
    print("Result=",a-b)
else:
    print("invalid operator")