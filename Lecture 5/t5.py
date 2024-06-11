class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds available balance.")
        elif amount >0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")
            
account = BankAccount("Alice", 300)
print(f"Account owner: {account.owner}")
print(f"Initial balance: {account.balance}")

account.deposit(50)
account.withdraw(30)
account.withdraw(150)
account.deposit(200)
account.withdraw(250)
account.withdraw(2000)