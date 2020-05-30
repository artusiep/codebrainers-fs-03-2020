# Inheritance Syntax

class BaseClass:
    pass


class ChildClass(BaseClass):
    pass


class Base:
    def __init__(self):
        self.name = "Base"
        print("Base class constructor")

    def fun(self):
        print("Base class fun method", self.name)


class Child01(Base):
    def __init__(self):
        super().__init__()
        print("Child01 class constructor")

    def fun(self):
        print("Child01 class fun", self.name)


class Child02(Base):
    def __init__(self):
        super().__init__()
        self.name = "Child02"
        print("Child02 class constructor")

    def fun(self):
        print("Child02 class fun", self.name)

    def not_so_funny(self):
        print("This is no funny")


b = Base()
b.fun()


c = Child01()
c.fun()

c2 = Child02()
c2.fun()
c2.not_so_funny()
