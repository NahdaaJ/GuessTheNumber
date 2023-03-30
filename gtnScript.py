# Author: Nahdaa Jawed
# Date Started: 29/03/2023 22:30
# Date Finished: 30/03/2023 13:00
# Description:  A game where the user has to guess a randomly generated integer.
#               The program gives hints to the user whether they should go higher or lower.
#               Once the user guesses correctly, they are congratulated and shown how many guesses it took them to
#               reach the correct answer. The game gives the user the choice to play again or to end the program.

#Importing necessary libraries and modules.
import random

# Defining the game as a function
def guessNum():

    # Generating a random integer, and assigning initial values.
    randInt = random.randint(0,10)
    guess = 0
    playAgain = 0
    guessIteration = 0

    while playAgain != "N":


        print("\nGuess an integer between 1 and 10 inclusive: ")
        while guess!=randInt:
            guess = int(input())


            # Conditions based on the users incorrect guesses.
            if guess>randInt:
                print("\nToo high! Go lower!")
            elif guess<randInt:
                print("\nToo low! Go higher!")

            # Counts the number of iterations the while loop has looped through.
            guessIteration = guessIteration + 1


        # User guesses correct answer.
        print(f'\nCongratulations! {randInt} was the correct answer!\nYou guessed in {guessIteration} guesses!\n')


        # Asking the user if they would like to play again.
        playAgain = input("Would you like to play again? (Y/N) \n")
        if playAgain == "Y":
            guess = 0
            randInt = random.randint(0, 10)
            guessIteration = 0


    # If the user chooses not to play again, the program ends.
    print("Thanks for playing!")

# Running the function.
guessNum()