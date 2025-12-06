import random
###Type 1
# while True:
#     choice=input("Roll the dice? (y/n): ").lower()
#     if choice =='y':
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         print(f"({die1}, {die2})")

#     elif choice == "n":
#         print("Thanks for playing!")
#         break
#     else:
#         print("Invalid choice! Please choose 'y' or 'n'.")

###Type 2
# choice=input("Roll the dice? (y/n): ").lower()
# if choice =='y':
#         turns=int(input("How many times do you want to roll the dice?"))
#         for _ in range(turns):
#             die1 = random.randint(1,6)
#             #die2 = random.randint(1,6)
#             #print(f"({die1}, ")
#             print(f"You rolled a {die1}")
# elif choice == "n":
#     print("Thanks for playing!")
   
# else:
#     print("Invalid choice! Please choose 'y' or 'n'.")        

##Type 3 -Type 1 with counter
counter=0
while True:
    choice=input("Roll the dice? 😎🤑🎲🪄🔮(y/n): ").lower()
    if choice =='y':
        counter+=1
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")

    elif choice == "n":
        print("Thanks for playing!")
        print("You have rolled the  dice",counter,"times")
        counter=0
        break
    else:
        print("Invalid choice! Please choose 'y' or 'n'.") 


