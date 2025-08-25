import random

rock = """
        ______
    ---'   ___)
         (_____)
         (_____)
         (____)
    ---._(___)
    
    """


paper = """
        ______
    ---'   ____)__
            _______)
            _______)
            _______)
    ---.__________)

    """


scissors = """

    ( _\    /_)
    \ _\  /_ / 
    \ _\/_ /_ _
    |_____/_/ /|
    (  (_)__)J-)
    (  /`.,   /
    \/  ;   /
    | === |

    """

print("*" * 50)
print("Rock, Paper, Scissors — Best of 5 (first to 3 wins)")
print("*" * 50)

print(f"Select between 1, 2 or 3: ")

computer = 0
player = 0

computer_score = 0
player_score = 0

while computer_score < 3 and player_score < 3:
    player = int(input())
    computer = random.randint(1, 3)

    choices = [rock, paper, scissors]

    print(f"Player chose:\n{choices[player - 1]}")
    print(f"Computer chose:\n{choices[computer - 1]}")

    # SELECTION
    if (player == computer):
        print("Tie")

    elif (player == 1 and computer == 3) or \
        (player == 2 and computer == 1) or \
            (player == 3 and computer == 2):
        print("Player Wins!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    # SCORE BOARD
    print("*" * 50)
    print("--------------------- SCORE ----------------------")
    print(
        f'Computer: {computer_score} vs Player: {player_score}')
    print("*" * 50)

if player_score >= 3:
    print("\n🎉 CONGRATULATIONS! You won the game! 🏆")
else:
    print("\n💻 Computer wins the game! Better luck next time 😅")
