from abc import ABC


class Polygon(ABC):

    # abstract method
    def sides(self):
        pass


class Triangle(Polygon):

    def sides(self):
        print("Triangle has 3 sides")


class Pentagon(Polygon):

    def sides(self):
        print("Pentagon has 5 sides")


class Hexagon(Polygon):

    def sides(self):
        print("Hexagon has 6 sides")


class square(Polygon):

    def sides(self):
        print("I have 4 sides")

    # Driver code


t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
