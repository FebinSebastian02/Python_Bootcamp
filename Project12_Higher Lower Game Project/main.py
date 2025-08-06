import art
from game_data import data
import random

score = 0
should_continue = True
account_B = random.choice(data)  # Account A needs to be replaced by account B

# TODO: Display welcome logo
print(art.logo1)

def format_data(account):
    """Takes account data and returns a printable format"""
    account_name = account["name"]
    account_profession = account["profession"]
    return f"{account_name}, {account_profession}"

def check_guess(user_guess, a_count, b_count):
    """Takes user's guess and determines whether the result is true / false"""
    if a_count > b_count:
        return user_guess == "A"
    else:
        return user_guess == "B"

while should_continue:
    # TODO: Generate a random account from the data
    account_A = account_B
    account_B = random.choice(data)
    if account_A == account_B:
        account_B = random.choice(data)

    # TODO: Format the account data into a printable format
    print(f"Compare A: {format_data(account_A)}")
    print(art.logo2)
    print(f"Against B: {format_data(account_B)}")

    # TODO: Ask user for guess
    guess = input("Who has more ig followers? Type 'A' or 'B': ").upper()

    # TODO: Clear the screen
    print("\n" * 20)
    print(art.logo1)

    # TODO: Check if user is correct. Get followers account
    account_A_count = account_A["followers"]
    account_B_count = account_B["followers"]
    is_correct = check_guess(guess, a_count=account_A_count, b_count=account_B_count)

    # TODO: Give user feed back on their guess and increment the score
    if is_correct:
        score += 1
        print(f"You are right!Current score: {score}")
    else:
        print(f"Sorry, You are wrong. Final score: {score}")
        should_continue = False
