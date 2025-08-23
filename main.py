import re

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


# print(type(123_456.5))
# print(type("stringasdf"))
# print(type(True))

# print("----------------------------------")
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# payment = (tip / 100 * bill + bill) / people
# print(f"Each person should pay: ${payment:.2f}")


print("**************************************")


# def get_float(prompt):
#     """Keep asking until user enters a valid float"""
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("❌ Please enter a valid number.")


# def get_int(prompt):
#     """Keep asking until user enters a valid integer"""
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("❌ Please enter a valid integer.")


# # Ask inputs safely
# bill = get_float("What was the total bill? $")
# tip = get_int("How much tip would you like to give? 10, 12, or 15? ")
# people = get_int("How many people to split the bill? ")

# # Calculate
# total_bill = bill + (bill * tip / 100)
# payment = total_bill / people

# # Output
# print(f"Each person should pay: ${payment:.2f}")

class User:
    def fizz_buzz(input):
        arr = []
        for i in range(1, input + 1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
            elif i % 3 == 0:
                arr.append("Fizz")
            elif i % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(i)
        return arr

    def palindrome_text(text):
        origin = re.sub(r'[^a-zA-Z0-9]', '', str(text)).lower()
        reverse = origin[::-1]

        return origin == reverse

    def palindrome_number():
        print("Type a number:")
        number = int(input())
        reverse_number = int(str(number)[::-1])

        print("Palindrome number: ")
        return number == reverse_number

    def even_numbers():
        print("Type a number: ")
        number = int(input())
        even_count = 0

        for i in range(number + 1):
            if i % 2 == 0 and i > 0:
                print(i)
                even_count += 1

        return (f"There are {even_count} even numbers!")


print(User.fizz_buzz(32))
print("**************************************")
print(User.palindrome_text("A man, a plan, a canal, Panama!"))
print("**************************************")
print(User.palindrome_number())
print("**************************************")
print(User.even_numbers())


# Formatting
name = "John"
age = 25
print(f"my name is {name}, I'm {age}")
print("my name is {}, I'm {}".format(name, age))
print("my name is %s, I'm %s" % (name, age))
