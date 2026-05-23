from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
            
    @abstractmethod
    def account_type(self):
        pass
    

class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"
    
class CheckingAccount(Account):
    def account_type(self):
        return "Checking Account"
    
# Example usage:
acc1 = SavingsAccount("Alice", 1000)
acc2 = CheckingAccount("Bob", 500)

acc1.account_type()
acc2.account_type()
acc1.deposit(200)
acc1.withdraw(150)
acc2.deposit(300)
acc2.withdraw(100)

print(acc1.get_account_holder())