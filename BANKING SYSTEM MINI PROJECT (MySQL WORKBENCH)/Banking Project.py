import mysql.connector
import bcrypt
from fpdf import FPDF

# mysql details

def get_connection():
    return mysql.connector.connect(
        host= 'localhost',
        user = 'root',
        password = 'vikas@1020',
        database = 'banking_system'
    )

# Create New Bank Account(CREATE)

def create_account():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    acc_type = input("Account type (Saving/Current): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers (name, email, phone) VALUES(%s,%s,%s)",
        (name, email,phone)
    )

    customer_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO accounts (customer_id, balance, account_type) VALUES (%s, %s,%s)",
        (customer_id, 0, acc_type)
    )

    conn.commit()
    print("Account created successfully!")

    conn.close()

# View Account Details(READ)

def view_account():
    acc_id = int(input("Enter Account ID:"))

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT c.name, a.account_id, a.balance, a.account_type
    FROM customers c
    JOIN accounts a ON c.customer_id = a.customer_id
    WHERE a.account_id = %s
    """

    cursor.execute(query, (acc_id,))
    result = cursor.fetchone()

    if result:
        print("Name: ", result[0])
        print("Account ID:", result[1])
        print("Balance:", result[2])
        print("Type:", result[3])
    else:
        print("Account not found")

    conn.close()

# Deposit Money (UPDATE)
def deposit():
    acc_id = int(input("Enter Account ID: "))
    amount = float(input("Enter amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    # Update balance
    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE account_id = %s",
        (amount, acc_id)
    )

    # Insert transaction record
    cursor.execute(
        "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)",
        (acc_id, "DEPOSIT", amount)
    )

    conn.commit()
    print("Amount deposited successfully!")

    conn.close()

# Withdraw Money (WITH VALIDATION)
def withdraw():
    acc_id = int(input("Enter Account ID: "))
    amount = float(input("Enter amount: "))

    conn = get_connection()
    cursor = conn.cursor()

    # Fetch current balance
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_id = %s",
        (acc_id,)
    )

    result = cursor.fetchone()

    if not result:
        print("❌ Account not found")
        conn.close()
        return

    balance = result[0]

    if amount > balance:
        print("❌ Insufficient balance")
        conn.close()
        return

    # Update balance
    cursor.execute(
        "UPDATE accounts SET balance = balance - %s WHERE account_id = %s",
        (amount, acc_id)
    )

    # Insert transaction record
    cursor.execute(
        "INSERT INTO transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)",
        (acc_id, "WITHDRAW", amount)
    )

    conn.commit()
    conn.close()

    print("Withdrawal successful")

# Delete Account (DELETE)
def delete_account():
    acc_id = int(input("Enter Account ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM accounts WHERE account_id = %s", (acc_id,))
    cursor.execute("DELETE FROM customers WHERE customer_id = %s", (acc_id,))

    conn.commit()
    print("Account deleted successfully")
    conn.close()

# View Transaction History
def view_transactions():
    acc_id = int(input("Enter Account ID: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT transaction_id, transaction_type, amount, transaction_date
                   FROM transactions
                   WHERE account_id = %s
                   ORDER BY transaction_date DESC
    """, (acc_id,))

    records = cursor.fetchall()

    if not records:
        print("No transactions found.")
    else:
        print("\n--- Transaction History ---")
        for r in records:
            print(f"ID:{r[0]} | {r[1]} | {r[2]} | {r[3]}")

    conn.close()

# LOGIN WITH HASHED PASSWORD (SECURE)
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


# Create User (Secure)
def create_user():
    username = input("Username: ")
    password = input("Password: ")

    hashed = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO login_users(username, password) VALUES(%s,%s)",
        (username, hashed)
    )

    conn.commit()
    conn.close()

# Login Authentication
def login():
    username = input("Username: ")
    password = input("Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM login_users WHERE username = %s",
        (username,)
    )

    record = cursor.fetchone()

    if record and bcrypt.checkpw(password.encode(), record[0].encode()):
        print("Login Successful")
        return True
    else:
        print("Invalid credentials")
        return False
    

# Password Reset Function (Console Based)
def reset_password():
    username = input("Enter your username: ")
    old_password = input("Enter old password: ")
    new_password = input("Enter new password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM login_users WHERE username = %s",
        (username,)
    )
    result = cursor.fetchone()

    if not result:
        print("User not found")
        return
    
    stored_hash = result[0].encode()

    if not bcrypt.checkpw(old_password.encode(), stored_hash):
        print("Old password incorrect")
        return
    
    new_hash = bcrypt.checkpw(new_password.encode(), bcrypt.gensalt())
    
    cursor.execute(
        "UPDATE login_users SET password = %s WHERE username = %s",
        (new_hash, username)
    )

    conn.commit()
    conn.close()

    print("Password updated successfully")

# ACCOUNT STATEMENT (PDF)
def generate_statement():
    acc_id = int(input("Enter Account ID:"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT transaction_type, amount, transaction_date
                   FROM  transactions
                   WHERE account_id = %s
                   ORDER BY transaction_date DESC
    """, (acc_id,))

    records = cursor.fetchall()

    if not records:
        print("No transaction found.")
        return
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Bank Transaction Statement", ln=True, align="C")

    pdf.ln(5)
    pdf.set_font("Arial", size=12)

    for t in records:
        line = f"{t[2]} | {t[0]} | Amount: {t[1]}"
        pdf.cell(0, 10, line, ln=True)

    filename = f"statement_{acc_id}.pdf"
    pdf.output(filename)

    print(f"Statement generated: {filename}")
    


# Authentication menu
def auth_menu():
    while True:
        print("\n--- AUTH MENU ---")
        print("1. Login")
        print("2. Create New User")
        print("3. Reset password")
        print("4. Exit")

        choice = input("Enter choice:")


        if choice == "1":
            if login():
                atm_menu()
        elif choice == "2":
            create_user()
        elif choice =="3":
            reset_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


# Main Menu
def atm_menu():
    while True:
        print("\n--- ATM MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Transaction History")
        print("5. Account statement")
        print("6. Exit ")

        choice = input("Enter choice:")

        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            view_account()
        elif choice == "4":
            view_transactions()
        elif choice == "5":
            generate_statement()
        elif choice == "6":
            print("Thank you for using our ATM")
            break
        else:
            print("Invalid option")



if __name__ == "__main__":
    auth_menu()