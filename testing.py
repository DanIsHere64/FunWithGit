class Shape:
    def __init__(self, w=1, l=1):
        self.width = 1
        self.length = 1
        if w > 1 and w % 1 == 0:
            self.width = w
        if l > 1 and l % 1 == 0:
            self.length = l


class Rectangle(Shape):
    def __init__(self, w, l):
        super().__init__(w, l)

    def __str__(self):
        print()
        return "\n".join(("* " * self.width) for _ in range(self.length))


class Square(Shape):
    def __init__(self, l):
        super().__init__(l, l)

    def __str__(self):
        print()
        return "\n".join(("* " * self.length) for _ in range(self.length))


class Triangle(Shape):
    def __init__(self, l):
        super().__init__(l, l)

    def __str__(self):
        print()
        return "\n".join(("* " * (self.length - i)) for i in range(self.length))


class Parallelogram(Shape):
    def __init__(self, w, l):
        super().__init__(w, l)

    def __str__(self):
        print()
        return"\n".join((" " * (self.length - i) + "* " * (self.width - i) + "* " * (i)) for i in range(self.length))


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print(r1)
s1 = Square(6)
print(s1)
t1 = Triangle(7)
print(t1)
p1 = Parallelogram(10, 3)
print(p1)
r2 = Rectangle(0, 0)
print(r2)
p1.width = 2
p1.width = -1
p1.height = 2
print(p1)