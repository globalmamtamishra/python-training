class Account:
    def __init__(self, account_number, holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} successfully. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} successfully. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account Balance: {self.__balance}")
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name


class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number not in self.__accounts:
            holder_name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            self.__accounts[account_number] = Account(account_number, holder_name, initial_balance)
            print("Account created successfully.")
        else:
            print("Account number already exists. Please choose a different account number.")

    def get_account(self, account_number):
        if account_number in self.__accounts:
            return self.__accounts[account_number]
        else:
            print("Account not found.")

    def display_all_accounts(self):
        print("All Accounts:")
        for account_number, account in self.__accounts.items():
            print(
                f"Account Number: {account.get_account_number()}, Holder Name: {account.get_holder_name()},Balance: {account.check_balance()}")

    def delete_account(self, account_number):
        if account_number in self.__accounts:
            del self.__accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account not found.")


bank = Bank()

while True:
    print("Banking Operations:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
    elif choice == "3":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
    elif choice == "4":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            account.check_balance()
    elif choice == "5":
        bank.display_all_accounts()
    elif choice == "6":
        account_number = input("Enter account number to delete: ")
        bank.delete_account(account_number)
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
