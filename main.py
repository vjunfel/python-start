
# def main():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")

#     print("Hello", name, "You are now", age, "years old")

# main()

# a = [1, 52, 3, 12, 4, 52]
# print(a.count(52))

# username = input("What is your name? ")
# length = len(username)

# print(length)


# glass1 = "milk"
# glass2 = "juice"

# new_glass = glass1
# glass1 = glass2
# glass2 = new_glass

# print("GLASS1: ", glass1)
# print("GLASS2: ", glass2)

# print("--------------------------------------------------")
# print("Hello and welcome to Band Name Generator!")
# print("--------------------------------------------------")
# city = input("What city did you grew up?\n")
# pet = input("What is your pet's name?\n")
# print("Your band name is:", city + " " + pet)


print(type(123_456.5))
print(type("stringasdf"))
print(type(True))

# print("----------------------------------")
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# payment = (tip / 100 * bill + bill) / people
# print(f"Each person should pay: ${payment:.2f}")


print("**************************************")


def get_float(prompt):
    """Keep asking until user enters a valid float"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


def get_int(prompt):
    """Keep asking until user enters a valid integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")


# Ask inputs safely
bill = get_float("What was the total bill? $")
tip = get_int("How much tip would you like to give? 10, 12, or 15? ")
people = get_int("How many people to split the bill? ")

# Calculate
total_bill = bill + (bill * tip / 100)
payment = total_bill / people

# Output
print(f"Each person should pay: ${payment:.2f}")

x = 1
