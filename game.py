#Import necessary packages
import random  

#Intro

print("-------------------")
print("Hi. Welcome to my Rock-Paper_Scissors game...")
print("-------------------")
# ASK FOR USER INPUT

user_choice = input("Please choose either: 'rock', 'paper', 'scissors': ")

# VALIDATE USER INPUT

if (user_choice == "rock" or user_choice == "ROCK" or user_choice =="Rock" 
or user_choice == "paper" or user_choice == "PAPER" or user_choice =="Paper"
or user_choice == "scissors" or user_choice == "SCISSORS" or user_choice =="Scissors"): 
    print("You chose:",user_choice)
else:
    print("Whoops! That is not a valid input. Please restart the game and try again.")
    exit()

# COMPUTER CHOICE

computer_options = ["rock",'paper','scissors']
computer_choice = random.choice(computer_options)
print("The computer chose:", computer_choice)
print("-------------------")

# DETERMINE THE WINNER

# FINAL RESULTS

