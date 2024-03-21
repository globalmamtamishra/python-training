class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l+ self.w)


rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 6)


print("area of rectangle :", rect1.area())
print("Perimeter of rectangle :", rect1.perimeter())

