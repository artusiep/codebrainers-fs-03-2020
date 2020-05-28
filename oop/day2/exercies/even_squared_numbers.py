a = range(30)

even_a = filter(lambda x: x % 2 == 0, a)
print(list(even_a))
print(list(even_a))
print(list(even_a))

squared_even_a = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, a))
print(list(squared_even_a))
print(list(squared_even_a))