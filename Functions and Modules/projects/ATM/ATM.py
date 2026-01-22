import operations

print("1. Balance\n2.Deposit\n3.Withdraw")
choice = int(input("Choose: "))

if choice == 1:
    print("Balance:", operations.check_balance())

elif choice == 2:
    amt = int(input("Enter amount: "))
    print("Updated Balance: ", operations.deposit(amt))

elif choice == 3:
    amt = int(input("Enter amount: "))
    print(operations.withdraw(amt))
    