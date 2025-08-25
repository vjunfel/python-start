import random

alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
special = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_']


def random_password_generator():
    result = ""
    for _ in range(1, 12):
        if (len(result) < 12):
            num = str(random.randint(0, 9))
            letter = str(alphabeth[random.randint(0, len(alphabeth) - 1)])
            spec = str(special[random.randint(0, len(special) - 1)])

            result += num + letter + spec

    return result


print("FINAL:", random_password_generator())
