# Author: Nahdaa Jawed
# Date Started: 29/03/2023 22:30
# Date Finished: 29/03/2023 23:30
# Description:  A game where the user has to guess a randomly generated integer.
#               The program gives hints to the user whether they should go higher or lower.
#               Once the user guesses correctly, the game gives the user the choice to play again or to end the program.

#Importing necessary libraries and modules.
import random

# Defining the game as a function
def guessNum():

    # Generating a random integer.
    randInt = random.randint(0,9)
    guess = 0
    playAgain = 0

    while playAgain != "N":
        while guess!=randInt:
            guess = int(input("Guess an integer between 1 and 10 inclusive: "))

            # Conditions based on the users guesses.
            if guess>randInt:
                print("Too high! Go lower!\n")

            elif guess<randInt:
                print("Too low! Go higher!\n")

        print(f'Congratulations! {randInt} was the correct answer!\n')

        # Asking the user if they would like to play again.
        playAgain = input("Would you like to play again? (Y/N) \n")
        if playAgain == "Y":
            guess = 0
            randInt = random.randint(0, 9)

    # If the user chooses not to play again, the program ends.
    print("Thanks for playing!")

guessNum()