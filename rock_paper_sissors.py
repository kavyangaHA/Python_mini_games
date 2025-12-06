import random

emojis = {'r': '✊', 'p': '✋', 's': '✌️'}
choices = ['r', 'p', 's']

while True:
    user_choices = input("rock, paper, scissors? (r/p/s): ").lower()
    if user_choices not in choices:
        print("Invalid choice! Please choose 'r', 'p', or 's'.")
        continue
    computer_choice = random.choice(choices)
    print(f"You chose: {emojis[user_choices]}")
    print(f"Computer chose: {emojis[computer_choice]}")
    if user_choices == computer_choice:
        print("It's a tie!")
    elif ((user_choices == 'r' and computer_choice == 's') or 
        (user_choices == 'p' and computer_choice == 'r') or 
        (user_choices == 's' and computer_choice == 'p') ):
        print("You Win!")
    else:
        print("You Lose!")

    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break
