# We will use random to make the computer pick random choices
import random

while True:
    user_action = input('Choose either R(rock), P(paper) or S(scissors):')
    possible_actions = ['R', 'P', 'S']
    computer_action = random.choice(possible_actions)
    print(f'\n You chose {user_action},computer chose {computer_action}.\n ')

    if user_action == computer_action:
        print('It is a tie')
    elif user_action == 'R':
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Do you want to play the game again? (y/n): ")
    if play_again.lower() != "y":
        break
