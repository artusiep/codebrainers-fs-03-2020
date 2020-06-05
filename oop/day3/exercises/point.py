class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        x_diff = self.x - other_point.x
        y_diff = self.y - other_point.y
        dist = (x_diff ** 2 + y_diff ** 2) ** 0.5
        return dist

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __add__(self, other_point):
        x_add = self.x + other_point.x
        y_add = self.y + other_point.y
        return Point(x_add, y_add)

    def __str__(self):
        return f"Point {self.x, self.y}"

    def __sub__(self, other_point):
        x_sub = self.x - other_point.x
        y_sub = self.y - other_point.y
        return Point(x_sub, y_sub)

