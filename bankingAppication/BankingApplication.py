class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} successfully. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, holder_name, initial_balance)
            print("Account created successfully.")
        else:
            print("Account number already exists. Please choose a different account number.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")

    def display_all_accounts(self):
        print("All Accounts:")
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}, Holder Name: {account.holder_name}, Balance: {account.balance}")


# Example usage:
bank = Bank()

# Creating accounts
bank.create_account("12345", "Alice", 1000)
bank.create_account("67890", "Bob", 500)

# Deposit and withdraw
alice_account = bank.get_account("12345")
if alice_account:
    alice_account.deposit(500)
    alice_account.withdraw(200)

# Check balance
bob_account = bank.get_account("67890")
if bob_account:
    bob_account.check_balance()

# Display all accounts
bank.display_all_accounts()
