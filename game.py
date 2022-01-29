


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#




# ASK FOR USER INPUT

user_choice = input("Please choose one of: 'rock', 'paper', 'scissors': ")

# VALIDATE USER INPUT

if (user_choice == "rock" or user_choice == "ROCK" or user_choice =="Rock" 
or user_choice == "paper" or user_choice == "PAPER" or user_choice =="Paper"
or user_choice == "scissors" or user_choice == "SCISSORS" or user_choice =="Scissors"): 
    print("User Choice:",user_choice)
else:
    print("Whoops! That is not a valid input. Please restart the game and try again.")
    exit()

# COMPUTER CHOICE



# DETERMINE THE WINNER

# FINAL RESULTS

