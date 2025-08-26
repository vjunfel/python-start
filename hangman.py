import random

word_list = [
    "dog", "cat", "lion", "tiger", "elephant", "zebra", "giraffe", "monkey", "bear", "panda",
    "kangaroo", "koala", "wolf", "fox", "deer", "camel", "horse", "donkey", "sheep", "goat",
    "cow", "buffalo", "ox", "pig", "rabbit", "squirrel", "mouse", "rat", "hamster", "hedgehog",
    "bat", "whale", "dolphin", "shark", "octopus", "crab", "lobster", "jellyfish", "seal", "penguin",
    "ostrich", "peacock", "eagle", "hawk", "falcon", "parrot", "sparrow", "pigeon", "duck", "goose",
    "chicken", "turkey", "swan", "owl", "vulture", "crow", "flamingo", "pelican", "stork", "seagull",
    "ant", "bee", "butterfly", "dragonfly", "mosquito", "fly", "beetle", "grasshopper", "cricket", "ladybug",
    "snake", "lizard", "crocodile", "alligator", "frog", "toad", "turtle", "chameleon", "iguana", "gecko",
    "salmon", "trout", "carp", "goldfish", "catfish", "tuna", "mackerel", "sardine", "anchovy", "eel",
    "hippopotamus", "rhinoceros", "leopard", "cheetah", "jaguar", "cougar", "lynx", "meerkat", "otter", "armadillo"
]

chosen_word = random.choice(word_list).lower()
# print(chosen_word.upper())

life = 5
placeholder = ""

game_over = False
correct_letters = []

for item in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

while life > 0 and not game_over:
    print("LIFE: ", life)
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("DISPLAY: ", display.upper())

    if guess not in chosen_word:
        life -= 1

    if display.lower() == chosen_word.lower():
        game_over = True
        print("*" * 50)
        print("Congrats! You Win :-)")

    if life == 0:
        game_over = True
        print("*" * 50)
        print("Game Over! You Failed :-(")
