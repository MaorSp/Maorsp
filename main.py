import random

choices = ["Rock", "Paper", "Scissors"]
while True:
    player_input = input("Choose your hand: Rock, Paper, Scissors or Quit to exit:")
    if player_input == "Quit":
        print("Thank you for playing")
        exit()
    if player_input not in choices:
        player_input = input("Wrong answer, please try again")
    else:
        random_choice = choices[random.randrange(0, 2)]
        if player_input == random_choice:
            result = "tie"
        elif player_input == "rock" and random_choice == "scissors":
            result = "Win"
        elif player_input == "paper" and random_choice == "rock":
            result = "Win"
        elif player_input == "paper" and random_choice == "rock":
            result = "win"
        elif player_input == "scissors" and random_choice == "paper":
            result = "win"
        else:
            result = "lose"
        print(f"Your choice is: {player_input} and Computer choice is: {random_choice}. You {result}")

