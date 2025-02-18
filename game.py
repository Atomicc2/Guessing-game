# Author: Anderson S.
# Project: Guessing Game
# Version: 1.0
# A simple number guessing game where the player selects a difficulty level and tries to guess the randomly generated number within a limited number of attempts.

from random import randint
from time import sleep
import sys

# Creating the error return function
def error(error_type):
    """Displays an error message based on the error type."""
    messages = {
        1: "This is not a valid number! Try again!",
        2: "Invalid input! Try again!"
    }
    print(messages.get(error_type, "Unknown error!"))

# Function to display difficulty options and return user's choice
def alternatives():
    """Prompts the user to select a difficulty level and returns the choice."""
    print("Hello, welcome to the game! Choose the difficulty level. Good luck!")
    sleep(2)
    print("Easy: 1 to 30\nMedium: 1 to 50\nHard: 1 to 100")

    while True:
        try:
            difficulty = input("Difficulty: ").lower()
            if difficulty == 'easy':
                print("Geez, this guy is scared!")
                return 1
            elif difficulty in ['medium', 'médium']:
                print("Good guy, go to safe!")
                return 2
            elif difficulty == 'hard':
                print("Good! Double good luck!")
                return 3
            else:
                error(2)
        except ValueError:
            error(2)

# Function to generate a random number based on the difficulty level
def random_number(choice):
    """Returns a random number based on the user's selected difficulty."""
    ranges = {1: 30, 2: 50, 3: 100}
    return randint(1, ranges[choice])

# Function to prompt user for their number guess
def requisition(choice):
    """Prompts the user to input a number within the range based on difficulty."""
    messages = {1: 30, 2: 50, 3: 100}
    print("You'll have 8 attempts!")
    sleep(1.2)

    while True:
        try:
            user_number = int(input(f"Choose a number between 1 and {messages[choice]}: "))
            if 1 <= user_number <= messages[choice]:
                print("Good, now let's check it out!")
                return user_number
            else:
                error(1)
        except ValueError:
            error(2)

# Function to display loading animation
def animation_loading():
    """Displays a simple loading animation."""
    for i in range(20):
        sys.stdout.write("\r" + "■" * i + " " * (20 - i))
        sys.stdout.flush()
        sleep(0.07)
    print("\n")

# Function to check user's result and manage the guessing loop
def result(draw_number, user_number, choice):
    """Compares user's guess with the drawn number and handles attempts."""
    animation_loading()
    attempts_list = []
    attempts = 7

    if draw_number == user_number and choice == 3:
        print("YOU ARE A GOD, AMAZING")
        return True

    while attempts > 0:
        try:
            if draw_number > user_number:
                user_number = int(input("It's a bigger number: "))
            elif draw_number < user_number:
                user_number = int(input("It's a smaller number: "))

            attempts -= 1
            print(f"Incorrect! Remaining attempts: {attempts}")
            attempts_list.append(user_number)

            if draw_number == user_number:
                print("Congratulations, good shot!")
                print(f"You guessed it in {8 - attempts} attempts!")
                print(f"Your attempts were: {attempts_list}")
                return True
        except ValueError:
            error(2)
    
    print(f"Game Over! The correct number was {draw_number}")
    return False

# Function to ask the user if they want to play again
def play_again(draw_number, user_number, choice):
    """Prompts the user to decide whether to play again."""
    while True:
        try:
            if draw_number == user_number and choice == 3:
                response = input("I don't recommend it, but do you want to try again? (yes/no): ").lower()
            else:
                response = input("Play again? (yes/no): ").lower()
            if response in ['yes', 'y']:
                animation_loading()
                print("Okay, go again")
                return True
            elif response in ['no', 'n']:
                animation_loading()
                print("Okay, bye bye")
                return False
            else:
                error(2)
        except ValueError:
            error(2)

# Main game loop
def main():
    """Main game loop that runs the gameplay until the user decides to stop."""
    while True:
        choice = alternatives()
        draw_number = random_number(choice)
        user_number = requisition(choice)
        result(draw_number, user_number, choice)
        if not play_again(draw_number, user_number, choice):
            break

# Run the game if the script is executed directly
if __name__ == "__main__":
    main()
