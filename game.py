#Import necessary packages
import random  

#Intro

print("-------------------")
print("Hi 'Player One' Welcome to my Rock-Paper_Scissors game...")
print("-------------------")
# ASK FOR USER INPUT
print("Here are your play options \n 1 (rock) \n 2 (paper) \n 3 (scissors)")
user_choice = input ("Please select a number corresponding to your desired play: ")
# user_choice = input("Please choose either: 'rock', 'paper', 'scissors': ")

# VALIDATE USER INPUT

if (user_choice != "1" and user_choice != "2" and user_choice != "3"):
    print("Whoops! That is not a valid play. Please try again.")
    exit()
if user_choice == "1": 
    user_choice = "rock"
    print("You chose: rock")
elif user_choice == "2": 
    user_choice = "paper"
    print("You chose: paper")
else:
    user_choice = "scissors"
    print("You chose: scissors")

# if (user_choice == "rock" or user_choice == "ROCK" or user_choice =="Rock" 
# or user_choice == "paper" or user_choice == "PAPER" or user_choice =="Paper"
# or user_choice == "scissors" or user_choice == "SCISSORS" or user_choice =="Scissors"): 
#     print("You chose:",user_choice)
# else:
#     print("Whoops! That is not a valid play. Please check your spelling and try again.")
#     exit()

# COMPUTER CHOICE

computer_options = ["rock",'paper','scissors']
computer_choice = random.choice(computer_options)
print("The computer chose:", computer_choice)
print("-------------------")

# DETERMINE THE WINNER

if user_choice == computer_choice: 
    print("It's a tie!")
elif user_choice == "rock": 
    if computer_choice == "scissors":
        print("You win! Congrats")
    else: 
        print("The computer won. It's ok")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! Congrats")
    else: 
        print("The computer won. It's ok")
elif user_choice == "paper":
    if computer_choice == "rock": 
        print("You win! Congrats")
    else: 
        print("The computer won. It's ok")

# FAREWELL
print("-------------------")
print("Thanks for playing. Please play again soon!")

