print("Welcome to Python Pizza Deliveries!")
print("Small pizza (S): $15")
print("Medium pizza (M): $20")
print("Large pizza (L): $25")
print("*"*30)

size = input("What size of pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

price = 0
add_on = 0
final_bill = 0

if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Wrong input")

if pepperoni == "Y":
    add_on += 2
if extra_cheese == "Y":
    add_on += 1

final_bill = price + add_on


print("-"*30)
print(f"Size: {size}, Price: {price}")
print(f"Pepperoni $2: {pepperoni}")
print(f"Cheese $1: {extra_cheese}")
print("-"*30)
print(f"Your final bill is ${final_bill}")
