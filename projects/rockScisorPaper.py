# Make a scissor rock paper game

import random

choices = ["rock", "paper", "scissor"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissor) or 'exit' to quit: ").lower()
    if user_choice == "exit":
        print("Thanks for playing!")
        break
    elif user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice  == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice =="rock") or (user_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")