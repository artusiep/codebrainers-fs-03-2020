from copy import copy

# from copy import copy
# copy()

# import copy
# copy.copy()


x = [1, 2, 3, 4, 5]
y = copy(x)

print(x)
print(y)

y.append(100)

print(x)
print(y)

# BEZ Copy
#      x -> memory 0x1313
# y -> x -> memory 0x1313

# Z Copy
# x -> memory 0x1313
# y -> memory 0x1380
