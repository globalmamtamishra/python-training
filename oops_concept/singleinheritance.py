

class Parent:
    def func_1(self):
     print("this is parent class")

class Child(Parent):
    def func_2(self):
     print("this is child class")

obj=Child()
obj.func_1()
obj.func_2()