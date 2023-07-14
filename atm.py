class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive value.")

# Usage Example
account = BankAccount("12787878890")
print(f"Account Number: {account.account_number}")
print(f"Initial Balance: ${account.balance}")

account.deposit(1000)
account.withdraw(500)
account.withdraw(700)

