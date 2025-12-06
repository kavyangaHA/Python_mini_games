#DRY - D
import random


ROCK = 'r'
PAPER = 'p' 
SCISSORS = 's'

emojis = {ROCK: '✊', PAPER: '✋', SCISSORS: '✌️'}
#ctrl+d to select same word multiple times and edit together with multiple cursors

#choices = [ROCK, PAPER, SCISSORS]
choices =tuple(emojis.keys())
#crtl+/ to comment multiple lines




def get_user_choice():
    while True:
        user_choices = input("rock, paper, scissors? (r/p/s): ").lower()
        if user_choices in choices:
            return user_choices
        else:
            print("Invalid choice! Please choose ROCK, PAPER, or SCISSORS.")

def display_choices(user_choices, computer_choice):
    print(f"You chose: {emojis[user_choices]}")
    print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choices, computer_choice):
    if user_choices == computer_choice:
        return "It's a tie!"
    elif ((user_choices == ROCK and computer_choice == SCISSORS) or 
        (user_choices == PAPER and computer_choice == ROCK) or 
        (user_choices == SCISSORS and computer_choice == PAPER) ):
        return "You Win!"
    else:
        return "You Lose!"   

def play_game():
    while True:
        user_choices = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choices, computer_choice)
        determine_winner(user_choices, computer_choice)
        print(determine_winner(user_choices, computer_choice))

        should_continue = input("Do you want to play again? (y/n): ").lower()
        if should_continue == 'n':
            print("Thanks for playing!")
            break
play_game()