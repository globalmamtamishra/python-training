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


# class Bank:
#     def __init__(self):
#         self.__accounts = {}
#         self.__logged_in_account = None
#
#     def register(self):
#         account_number = input("Enter account number: ")
#         if account_number not in self.__accounts:
#             holder_name = input("Enter account holder's name: ")
#             initial_balance = float(input("Enter initial balance: "))
#             self.__accounts[account_number] = Account(account_number, holder_name, initial_balance)
#             print("Account created successfully.")
#         else:
#             print("Account number already exists. Please choose a different account number.")
#
#     def login(self):
#         account_number = input("Enter account number: ")
#         if account_number in self.__accounts:
#             print("Login successful.")
#             self.__logged_in_account = self.__accounts[account_number]
#         else:
#             print("Account not found.")
#
#     def create_account(self):
#         if self.__logged_in_account:
#             account_number = input("Enter account number: ")
#             if account_number not in self.__accounts:
#                 holder_name = input("Enter account holder's name: ")
#                 initial_balance = float(input("Enter initial balance: "))
#                 self.__accounts[account_number] = Account(account_number, holder_name, initial_balance)
#                 print("Account created successfully.")
#             else:
#                 print("Account number already exists. Please choose a different account number.")
#         else:
#             print("Please login first.")
#
#     def get_account(self, account_number):
#         if account_number in self.__accounts:
#             return self.__accounts[account_number]
#         else:
#             print("Account not found.")
#
#     def display_all_accounts(self):
#         print("All Accounts:")
#         for account_number, account in self.__accounts.items():
#             print(
#                 f"Account Number: {account.get_account_number()}, Holder Name: {account.get_holder_name()},Balance: {account.check_balance()}")
#
#     def delete_account(self, account_number):
#         if account_number in self.__accounts:
#             del self.__accounts[account_number]
#             print("Account deleted successfully.")
#         else:
#             print("Account not found.")
#
#
# bank = Bank()
#
# while True:
#     print("Banking Operations:")
#     print("1. Register")
#     print("2. Login")
#     print("3. Create Account")
#     print("4. Deposit")
#     print("5. Withdraw")
#     print("6. Check Balance")
#     print("7. Display All Accounts")
#     print("8. Delete Account")
#     print("9. Exit")
#
#     choice = input("Enter your choice (1-9): ")
#
#     if choice == "1":
#         bank.register()
#     elif choice == "2":
#         bank.login()
#     elif choice == "3":
#         bank.create_account()
#     elif choice == "4":
#         account_number = input("Enter account number: ")
#         account = bank.get_account(account_number)
#         if account:
#             amount = float(input("Enter amount to deposit: "))
#             account.deposit(amount)
#     elif choice == "5":
#         account_number = input("Enter account number: ")
#         account = bank.get_account(account_number)
#         if account:
#             amount = float(input("Enter amount to withdraw: "))
#             account.withdraw(amount)
#     elif choice == "6":
#         account_number = input("Enter account number: ")
#         account = bank.get_account(account_number)
#         if account:
#             account.check_balance()
#     elif choice == "7":
#         bank.display_all_accounts()
#     elif choice == "8":
#         account_number = input("Enter account number to delete: ")
#         bank.delete_account(account_number)
#     elif choice == "9":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please enter a number between 1 and 9.")
