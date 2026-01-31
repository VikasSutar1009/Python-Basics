# Billing system (supermarket Example):

total = 0

while True:
    item = input("Enter item name(or 'done' to finish):")

    if item == 'done':
        break

    price = float(input("Enter price:"))
    quantity = int(input("Enter quantity:"))

    total += price * quantity
print("Total Bill Amount:", total)