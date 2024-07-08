import random

options = ["rock", "paper", "scissors"]
bot_choice = random.choice(options)
user_choice = str(input("Enter your choice of rock, paper, or scissors: ")).lower()

while user_choice not in options:
    for game_option in options:
        if user_choice == game_option:
            continue
        else:
            user_choice = str(input("Enter your choice of rock, paper, or scissors: "))


if user_choice == bot_choice:
    print("TIE")
    print(f"Game Recap: \nYour choice: {user_choice}\nBot choice: {bot_choice}")
elif user_choice == "rock" and bot_choice == "scissors":
    print("You win!")
    print(f"Game Recap: \nYour choice: {user_choice}\nBot choice: {bot_choice}")
elif user_choice == "paper" and bot_choice == "rock":
    print("You win!")
    print(f"Game Recap: \nYour choice: {user_choice}\nBot choice: {bot_choice}")
elif user_choice == "scissors" and bot_choice == "paper":
    print("You win!")
    print(f"Game Recap: \nYour choice: {user_choice}\nBot choice: {bot_choice}")
else:
    print("You lose!")
    print(f"Game Recap: \nYour choice: {user_choice}\nBot choice: {bot_choice}")
