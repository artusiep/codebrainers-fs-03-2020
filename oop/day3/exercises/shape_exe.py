class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

    def circumference(self):
        raise NotImplementedError


# utworzyc klasy pochodne
# rectange, square, circle

class Circle(Shape):
    def __init__(self, radial):
        super().__init__()
        self.r = radial

    def area(self):
        return 3.14 * self.r ** 2

    def circumference(self):
        return 6.28 * self.r



class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def circumference(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

shape_list = [Square(10), Rectangle(5,10), Circle(10), Square(5)]
print(shape_list)
for shape in shape_list:
    print(shape.area(), shape.circumference())

sq = Square(10)
sq.area()
sq.circumference()