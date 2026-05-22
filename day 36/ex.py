class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
            return True
        return False
    
    
b1= BankAccount("Alice", 1000)
print(b1.get_balance())  # Output: 1000
b1.deposit(500)
print(b1.get_balance())  # Output: 1500