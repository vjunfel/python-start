import random

alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_']


def random_password_generator():
    password = ""

    number_of_characters = int(input("How many characters do you want? "))
    if (len(password) < number_of_characters):
        for _ in range(number_of_characters):
            num = str(random.randint(0, 9))
            letter = str(alphabeth[random.randint(0, len(alphabeth) - 1)])
            spec = str(special[random.randint(0, len(special) - 1)])

            combined = num + letter + spec

            password += random.choice(combined)

    return password


print(random_password_generator())
