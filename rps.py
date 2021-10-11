  #Intro to Python - Rock Paper scissors game
import random

def rps():
  while True:
    user_action = input("Enter a choice rock, paper, or scissors: ")

    possible_actions= ["rock", "paper","scissors"]
    #we want the computer to choose random actions
    computer_actions =  random.choice(possible_actions)

    print(" you chose, computer chose .\n")

    print(f"You chose {user_action}, Computer chose {computer_actions}.\n")

    #Tie
    if user_action == computer_actions: 
      print(f"both players selected {user_action} its a tie")

    elif user_action == "rock":
      if computer_actions == "scissors": 
        print("rock smashes scissors! You win! ")
      else: 
        print("Paper covers rock...you lose")

        #User paper

    elif user_action == "paper":
      if computer_actions == "rock": 
        print("Paper covers! You win! ")
      else: 
        print("scissors cut paper...you lose")

    #user scissors
    elif user_action == "scissors":
      if computer_actions == "paper": 
        print("scissors cuts paper! You win! ")
      else: 
        print("Prock smashes scissors...you lose")

        play_again = input("Play again? (y/n)")
        if play_again.lower() != "y":
          exit()