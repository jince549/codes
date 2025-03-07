import random
game_icons = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
}

game_list = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please enter your choice (Type Rock, Paper, Scissors) :\n").lower().strip()
    com_choice = random.choice(game_list)
    
    if user_input not in game_list:
        print("Invalid input")
        continue

    print(f"Your choice : {user_input} {game_icons[user_input]}")
    print(f"Computer choose : {com_choice} {game_icons[com_choice]}")
    
    if user_input == com_choice:
        print("Game draw")
    else:
        if user_input == "rock" and com_choice == "paper":
            print("Computer wins")
        elif user_input == "paper" and com_choice =="scissors":
            print("Computer wins")
        elif user_input == "scissors" and com_choice == "rock":
            print("Computer wins")
        else:
            print("You win")
    while True:
        game_continue = input("Do you want to continue the game (Type Y/N) :").lower().strip()
        if game_continue == "n":
            print("Thank you")
            break
        elif game_continue == "y":
            break
        else:
            print("Invalid input")
    if game_continue == "n":
        break