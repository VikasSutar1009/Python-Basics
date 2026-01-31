# Login system (username + password)
username = "admin"
password = "admin123"

for attempt in range(3):
    u = input("Username: ")
    p = input("Password: ")

    if u == username and p == password:
        print("Login successful")
        break
    else:
        print("Invalid credentials")
else:
    print("Account locked. Try later")