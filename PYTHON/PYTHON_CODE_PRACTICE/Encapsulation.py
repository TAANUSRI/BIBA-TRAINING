class BankAccount:
    def __init__(self, account_holder, balance=0):
        self._account_holder = account_holder  
        self.__balance = balance  
    def get_account_holder(self):
        return self._account_holder
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
account = BankAccount("Alice")
print("Account Holder:", account.get_account_holder())  
print("Balance:", account.get_balance())  
account.deposit(100)  
account.withdraw(30) 
account.withdraw(80)  

