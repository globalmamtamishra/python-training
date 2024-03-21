class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Current balance: ₹{self.balance}")
        else:
            print("Insufficient amount or Invalid Withdrawal amount")

    def transfer(self, recipient_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.deposit(amount)
            print(f"Transferred ₹{amount}. Your new balance: ₹{self.balance}")
        else:
            print("Insufficient balance for transfer")

    def check_balance(self):
        print(f"Current balance for {self.name}: ₹{self.balance}")


def main():
    print("Welcome to the Bank Management System")
    name = input("Enter your Name: ")
    account = BankAccount(name)

    while True:
        print("\n Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter Deposit Amount: ₹"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter Withdrawal Amount: ₹"))
            account.withdraw(amount)
        elif choice == '3':
            amount = float(input("Enter Transfer Amount: ₹"))
            recipient_name = input("Enter recipient's Name: ")
            recipient_account = BankAccount(recipient_name)  
            account.transfer(recipient_account, amount)
        elif choice == '4':
            account.check_balance()
        elif choice == '5':
            print("Thank you for using the Bank Management System")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
