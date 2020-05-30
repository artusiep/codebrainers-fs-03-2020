class MyClass:
    public_class_attribute = 0
    _protected_class_attribute = ""
    __private_class_attribute = "Private Class Attribute"

    def __init__(self, constructor_argument):
        self._object_attribute = constructor_argument
        self.__private_object_attribute = "Private Object Attribute"

    def get_object_attribute(self):
        return self._object_attribute

    def _protected_method(self):
        print(f"Invoke Protected Method {self} object of id {id(self)}")

    def public_method(self):
        self._protected_method()
        print(f"Invoke Public Method {self} object of id {id(self)}")


my_class_object = MyClass("a")
# print(my_class_object._object_attribute)              # Violate OOP Encapsulation Principle
print(my_class_object.get_object_attribute())
# my_class_object._object_attribute = "something else"  # Violate OOP Encapsulation Principle
# my_class_object._protected_method()                   # Violate OOP Encapsulation Principle
my_class_object.public_method()
my_class_object2 = MyClass("another_a")

print(MyClass.public_class_attribute)
MyClass.public_class_attribute = 1
print(MyClass.public_class_attribute)
print(my_class_object.public_class_attribute)

print(MyClass._MyClass__private_class_attribute)
print(my_class_object._MyClass__private_object_attribute)