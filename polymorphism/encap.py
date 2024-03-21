class BankAccount:
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance
    def get_accno(self):
        return self.__accno
    def get_balance(self):
        return self.__balance

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            print("withdraw successful")
        else:
            print("insufficient fund")

    def deposit(self,amount):
        if amount>100:
            self.__balance+=amount
            print("deposit successful")
        else:
            print("invalid deposit found")
mamta=BankAccount("1234",2000)
maya=BankAccount("1234",2000)



