# "game.py" FILE

# "determine_winner" FUNCTION DEFINTION
def determine_winner(user_choice,computer_choice):
    # DETERMINE THE WINNER LOGIC
    outcome = ""
    if user_choice == computer_choice: 
        outcome = "It's a tie!"
    elif user_choice == "rock": 
        if computer_choice == "scissors":
            outcome = "You win! Congrats"
        else: 
            outcome = "The computer won. It's ok"
    elif user_choice == "scissors":
        if computer_choice == "paper":
            outcome = "You win! Congrats"
        else: 
            outcome = "The computer won. It's ok"
    elif user_choice == "paper":
        if computer_choice == "rock": 
            outcome = "You win! Congrats"
        else: 
            outcome = "The computer won. It's ok"
    return outcome

# IMPORT RELEVANT PACKAGES
import random  
import os

# ALLOWS FOR A USER NAME

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One")

# MAIN CONDITIONAL
if __name__ == "__main__":

    # INTRO
    print("-------------------")
    print("Hi",PLAYER_NAME +"!", "Welcome to my Rock-Paper-Scissors game...")
    print("-------------------")

    # ASK FOR USER INPUT
        # NUMBER OPTIONS TO HELP WITH DATA VALIDATION
    print("Here are your play options: \n 1 (rock) \n 2 (paper) \n 3 (scissors)")
    user_choice = input ("Please select a number corresponding to your desired play: ")

    # VALIDATE USER INPUT
    if (user_choice != "1" and user_choice != "2" and user_choice != "3"):
        print("Whoops! That is not a valid play. Please try again.")
        exit()
    if user_choice == "1": 
        user_choice = "rock"
        print("You chose:", user_choice)
    elif user_choice == "2": 
        user_choice = "paper"
        print("You chose:", user_choice)
    else:
        user_choice = "scissors"
        print("You chose:", user_choice)

    # COMPUTER CHOICE
    computer_options = ["rock",'paper','scissors']
    computer_choice = random.choice(computer_options)
    print("The computer chose:", computer_choice)
    print("-------------------")

    # CALL THE "determine_winner" FUNCTION, PASSING IN USER AND COMPUTER PLAYS
        # ASSIGN RETURN VALUE TO VARIABLE
    outcome = determine_winner(user_choice, computer_choice)

    # FAREWELL
    print(outcome)
    print("-------------------")
    print("Thanks for playing", PLAYER_NAME+".", "Please play again soon!")
