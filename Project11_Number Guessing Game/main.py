# TODO: Import the logo from art module
from art import logo
import random

count = 0
number = range(1, 100)
num = random.choice(number)

# TODO: Declare global constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

print(logo)
print("Welcome to the Number Guessing Game!!!")
print("I am thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "hard":
    attempt = HARD_LEVEL_ATTEMPTS

else:
    attempt = EASY_LEVEL_ATTEMPTS

for _ in range(attempt):
    print(f"You have {attempt} attempt(s) remaining to guess the number.")
    guess = int(input("Make a guess"))

    if guess == num:
        print(f"You got it! The answer was {num}")
        quit()
    elif guess < num:
        print("Too low. Guess again.")
    elif guess > num:
        print("Too high. Guess again.")

    attempt -= 1

if attempt == 0:
    print("You ran out of attempt(s). Better luck next time")
    quit()