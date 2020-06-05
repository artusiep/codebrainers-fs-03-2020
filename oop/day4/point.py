from copy import copy


class Point:
    _counter = 0

    # Not preferable way of doing copy constructor
    # def __init__(self, x=None, y=None, point=None):
    #     if x is not None and y is not None:
    #         self.x = x
    #         self.y = y
    #     elif point is not None:
    #         self.x = point.x
    #         self.y = point.y
    #     else:
    #         raise Exception()
    #     Point._counter += 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point._counter += 1

    @staticmethod
    def copy_constructor(point):
        print("Static method", Point._counter)
        return Point(point.x, point.y)

    # @staticmethod Nie mają dostępu do atrybutów klasy ani obiektu
    @staticmethod
    def dodaj(a, b):
        return a + b

    # @staticmethod Mają dostępu do atrybutów klasy, nie mają do atrubutów obiektu
    @classmethod
    def copy_constructor_class_method(cls, point):
        print("Class method", cls._counter)
        print(cls)
        return cls(point.x, point.y)

    def __del__(self):
        Point._counter -= 1

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __copy__(self):
        return Point(self.x, self.y)

    def distance(self, point):
        dist = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return dist


class Vector:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return self.point1.distance(self.point2)

    def __eg__(self, other):
        return self.length() == other.length()

    # lower than
    def __lt__(self, other):
        return self.length() < other.length()


point = Point(10, 25)
point_copy1 = Point.copy_constructor_class_method(point)
point_copy2 = Point.copy_constructor(point)
point_copy3 = copy(point)
point_copy3.x = 100
print(point)


point2 = point
point2.x = 100
print(point)

# point1 = Point(y=2, x=4)
# print(Point._counter)
#
# point2 = Point(1, 8)
# print(Point._counter)
#
# point3 = Point(4, 7)
# print(Point._counter)
#
# del point3
# point3 = Point(4, 5)
# print(Point._counter)
#
# del point3
# point3 = Point(4, 7123)
# print(Point._counter)
#
# point3 = Point(4, 1237)
# point3 = Point(4, 7)
# point3 = Point(4, 7)
# point3 = Point(4, 7)
# point3 = Point(4, 7)
# print(Point._counter)
# del point3
# point3 = 5
# print(Point._counter)
# point_copy = Point.copy_constructor(point1)
# # Ugly way
# # point_copy = Point(point=point2)
# print(Point.dodaj(10, 15))
# print(point1._counter)
# print(Point._counter)
# print(point1.distance(point=point2))
#
# del point1
#
# print(point2._counter)
# del (point2)
# del (point3)
# print(Point._counter)
