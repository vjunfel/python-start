import random

friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

number = random.randint(0, len(friends))

print(len(friends))
print(number)

print(f"You will be the one to pay \"{friends[number]}\"")
