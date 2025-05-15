# Imports
import random

movie_list = ["INTERSTELLAR", "WHIPLASH", "BATMAN"]

print("Let's Start!!!\n")

# TODO - Randomly choose a movie from the movie_list and assign it to a variable named chosen_movie. Then print it.
chosen_movie = random.choice(movie_list)

# TODO - Create a place holder with the same number of blanks as the chosen_movie
placeholder = len(chosen_movie) * "_"
print(placeholder)
print()

corrected_letters = []

# TODO - Ask the user to guess a letter and assign the letter into a variable. Make the letter uppercase
# TODO - Use a loop so that user can guess again and again
game_over = False

while not game_over: # As not game_over = True, loop starts running
    guess = input("Guess a letter please").upper()

    # TODO - Create a variable and use it to display the guessed letters that are right and show blanks for wrong letters.
    # TODO - Update the for loop to store previously corrected letters.
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

    if "_" not in movie:
        game_over = True
        print("You Won!!!")


