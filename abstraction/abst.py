
from abc import ABC, abstractmethod

class Animal(ABC):
  #abstractmethod
    def sound(self):
        pass

#abstract method
def action(self):
    pass
class Dog(Animal):
    def sound(self):
        return "Bark"

    def action(self):
        return "Run"

class Snake(Animal):
    def sound(self):
        return "Hiss"

    def action(self):
        return "Slither"


dog = Dog()
print("Dog sound:", dog.sound())
print("Dog action:", dog.action())

snake = Snake()
print("Snake sound:", snake.sound())
print("Snake movement:", snake.action())
