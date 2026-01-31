# real time example on control flow
# ATM system
balance = 5000
pin = 1234

entered_pin = int(input("Enter your pin:"))

if entered_pin == pin:
    print("Login successful")

    while True:
        print("\n1. check Balance")
        print("2. Withdraw")
        print("3. Exit")


        choice = int(input("Enter choice:"))

        if choice == 1:
            print("Your balance is:")

    
        elif choice == 2:
            amount = int(input("Enter amount:"))
            if amount <= balance:
                balance -= amount
                print("Withdrawl successful, Balance:", balance)
            else:
                print("Insufficient balance")
        elif choice == 3:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid Option")

else:
    print("Incorrect PIN")