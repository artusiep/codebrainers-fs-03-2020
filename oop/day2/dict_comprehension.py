accounts = {'Artur': 10, 'Magda': 1000, 'Adam': 1500}


# For
accounts1 = {}
for key, value in accounts.items():
    accounts1[key] = value * 1.01

print(accounts1)

# Dict comprehension
# {}
accounts2 = {name: balance * 1.01 for (name, balance) in accounts.items()}
print(type(accounts2))
print(accounts2)


