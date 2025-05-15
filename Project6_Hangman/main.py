# Imports
import random
from hangman_dependencies import movie_list
from hangman_dependencies import hangman_pics, hangman_logo

print(hangman_logo)

# TODO - Randomly choose a movie from the movie_list and assign it to a variable named chosen_movie. Then print it.
chosen_movie = random.choice(movie_list)

# TODO - Create a place holder with the same number of blanks as the chosen_movie
placeholder = len(chosen_movie) * "_"
print(placeholder)
print()

corrected_letters = []

# TODO - Ask the user to guess a letter and assign the letter into a variable. Make the letter uppercase
# TODO - Use a loop so that user can guess again and again
# TODO - Assign a variable to keep track of the number of lives left. Let max. number be 6
health_tonic_used = 0
game_over = False

while not game_over: # As not game_over = True, loop starts running
    print("\nxxxxxxxxxx     You have used", health_tonic_used, "health tonic(s)     xxxxxxxxxx\n")
    guess = input("Guess a letter please").upper()

    # TODO - Create a variable and use it to display the guessed letters that are right and show blanks for wrong letters.
    # TODO - Update the for loop to store previously corrected letters.
    # TODO - Lives should be reduced by 1 for every wrong guesses and the game should be lost once the life gets to 0
    movie = ""
    for letter in chosen_movie:
        if letter == guess:
            movie += letter
            corrected_letters.append(guess)
        elif letter in corrected_letters:
            movie += letter
        else:
            movie += "_"

    print(movie)
    print()
    if guess not in movie:
        health_tonic_used += 1

    if "_" not in movie:
        game_over = True
        print("**********   YOU WON!!!   **********")

    elif health_tonic_used == 6:
        game_over = True
        print("You finished all your health tonics")
        print("The name of the movie was", chosen_movie)
        print("**********   YOU LOSE!!!   **********")

    print(hangman_pics[health_tonic_used])