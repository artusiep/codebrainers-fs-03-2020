# reduce
from functools import reduce

temperates = [10.1, 12.31, 15.13, 14.13, 4.31, 13.10, 12.02]

temp_variable = 0
for x in temperates:
    temp_variable += x
print(temp_variable)

print(sum(temperates))

temp_variable = 1
for x in temperates:
    temp_variable = x * temp_variable
print(temp_variable)


def multiply(elem1, elem2):
    return elem1 * elem2


acc2 = reduce(lambda arg1, arg2: arg1 * arg2, temperates)
acc3 = reduce(multiply, temperates)
print(acc2)
print(acc3)

# [10.1, 12.31, 15.13, 14.13, 4.31] -> 1 Etap
# [124.331, 15.13, 14.13, 4.31] -> 2 Etap
# [1881.12803, 14.13, 4.31] -> 3 Etap
# [26580.339063900003, 4.31] -> 4 Etap
# [114561.261365409] -> 5 Etap
# 114561.261365409 -> 6 Etap
