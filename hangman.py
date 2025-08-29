import random
from hangman_words import word_list, hangman_logo

choosen_word = random.choice(word_list).lower()
# Create a hangman game that will guess the random word by guessing its letters.
word_length = len(choosen_word)
life = 6

correct_letters = []
game_over = False
letter_placeholder = ""


# display "_" each letter on a word.
for letter in range(word_length):
    letter_placeholder += "_"

print("Welcome to \n", hangman_logo)
print("Life: ", life)
# print(choosen_word.upper())
print(letter_placeholder.center(50, "="))


def hangman_game():
    global life, game_over

    while life > 0 and not game_over:
        display = ""

        guess_letter = input("Type a letter: ").lower()

        if guess_letter not in choosen_word:
            life -= 1
            print("Wrong letter! Life:", life)

        if guess_letter in correct_letters:
            print("You already guessed that letter!")
            continue

        for letter in choosen_word:
            if letter == guess_letter:
                display += letter
                correct_letters.append(letter)
                print("Correct! life:", life)

            elif letter in correct_letters:
                display += letter

            else:
                display += "_"

        print("*" * 50)
        print(display.center(50, "="))

        if display == choosen_word:
            game_over = True
            print("*" * 50)
            print("Congrats, You Win! :-)")

        if life == 0:
            game_over = True
            print("*" * 50)
            print(choosen_word.center(50, "="))
            print("Game Over, You've lost! :-(")


hangman_game()
