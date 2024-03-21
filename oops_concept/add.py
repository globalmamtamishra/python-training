# class BankAccount:
#     def __init__(self):
#         self.bal = 0
#
#     def deposit(self, amount):
#         self.bal += amount
#         print(self.bal)
#
#     def withdraw(self, amount):
#         if amount <= self.bal:
#             self.bal -= amount
#             print(self.bal)
#         else:
#             print("Insufficient balance")
#
#
# account = BankAccount()
# account.deposit(800)
# account.withdraw(500)
# account.withdraw(500)



class AddAndsub:
    def __init__(self,a, b):
        self.a = a
        self.b= b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


class MulAndDiv(AddAndsub):
    def __init__(self, a, b):
        super().__init__(a, b)

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


obj = MulAndDiv(10, 5)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())














