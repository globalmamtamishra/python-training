from Bank.Bank import Account


class Bank:
    def __init__(self):
        self.__accounts = {}
        self.__logged_in_user = None

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username not in self.__accounts:
            self.__accounts[username] = {'password': password, 'accounts': {}}
            print("Registration successful.")
        else:
            print("Username already exists. Please choose a different username.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.__accounts and self.__accounts[username]['password'] == password:
            print("Login successful.")
            self.__logged_in_user = username
        else:
            print("Invalid username or password.")

    def create_account(self):
        if self.__logged_in_user:
            account_number = input("Enter account number: ")
            if account_number not in self.__accounts[self.__logged_in_user]['accounts']:
                holder_name = input("Enter account holder's name: ")
                initial_balance = float(input("Enter initial balance: "))
                self.__accounts[self.__logged_in_user]['accounts'][account_number] = Account(account_number, holder_name, initial_balance)
                print("Account created successfully.")
            else:
                print("Account number already exists. Please choose a different account number.")
        else:
            print("Please login first.")

    def get_account(self, account_number):
        if self.__logged_in_user:
            if account_number in self.__accounts[self.__logged_in_user]['accounts']:
                return self.__accounts[self.__logged_in_user]['accounts'][account_number]
            else:
                print("Account not found.")
        else:
            print("Please login first.")

    def display_all_accounts(self):
        if self.__logged_in_user:
            print("All Accounts:")
            for account_number, account in self.__accounts[self.__logged_in_user]['accounts'].items():
                print(
                    f"Account Number: {account.get_account_number()}, Holder Name: {account.get_holder_name()},Balance: {account.check_balance()}")
        else:
            print("Please login first.")

    def delete_account(self, account_number):
        if self.__logged_in_user:
            if account_number in self.__accounts[self.__logged_in_user]['accounts']:
                del self.__accounts[self.__logged_in_user]['accounts'][account_number]
                print("Account deleted successfully.")
            else:
                print("Account not found.")
        else:
            print("Please login first.")


bank = Bank()

while True:
    print("Banking Operations:")
    print("1. Register")
    print("2. Login")
    print("3. Create Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Check Balance")
    print("7. Display All Accounts")
    print("8. Delete Account")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        bank.register()
    elif choice == "2":
        bank.login()
    elif choice == "3":
        bank.create_account()
    elif choice == "4":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
    elif choice == "5":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
    elif choice == "6":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            account.check_balance()
    elif choice == "7":
        bank.display_all_accounts()
    elif choice == "8":
        account_number = input("Enter account number to delete: ")
        bank.delete_account(account_number)
    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
