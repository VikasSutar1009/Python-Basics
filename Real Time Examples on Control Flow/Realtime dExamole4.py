# Billing system using match case
print("1.tea = 10")
print("2. Coffee = 20")
print("3. Sandwich = 50")
choice = int(input("choose item"))

match choice:
    case 1:
        print("You selected tea. Bill = 10")
    case 2:
        print("You selected Coffee. Bill = 20")
    case 3:
        print("You selected Sandwich. Bill = 50")
    case _:
        print("Invalid selection")