balance = 10000

def check_balance():
    return balance

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        return balance
    else:
        return "Insufficient Balance"
    
    