# For
parity_numbers = []

for x in range(0, 30):
    if x % 2 == 0:
        parity_numbers.append(x)

print(parity_numbers)

# List Comprehension

parity_numbers2 = [
    x
    for x in range(0, 30)
    if x % 2 == 0
]

print(parity_numbers2)

squared_parity_numbers = [y ** 2 for y in parity_numbers2]

print(squared_parity_numbers)

fruits = tuple(x for x in ['Jabłko', 'Wiśnia', 'Ziemniak'] if x != 'Ziemniak')
print(fruits)
