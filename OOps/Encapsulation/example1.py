class Account:
    def __init__(self,balance):
        self.__balance=balance  #private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    
acc =Account(1000)
acc.deposit(500)
print(acc.get_balance())   #output:1500



# class Account:
    # def __init__(self, balance):
        # self.__balance = balance  # private variable
# 
    # def deposit(self, amount):
        # if amount > 0:
            # self.__balance += amount

    # def get_balance(self):
        # return self.__balance

# acc = Account(1000)
# acc.deposit(500)
# print(acc.get_balance())  # Output: 1500
