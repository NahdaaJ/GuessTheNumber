# Author: Nahdaa Jawed
# Date Started: 29/03/2023 22:30
# Date Finished: -
# Description

#Importing necessary libraries and modules.
import random

def guessNum():
    randInt = random.randint(0,9)
    guess = 0
    playAgain = 0

    while playAgain != "N":
        while guess!=randInt:
            guess = int(input("Guess a number between 1 and 10 inclusive: "))
            if guess>randInt:
                print("Too high! Go lower!\n")

            elif guess<randInt:
                print("Too low! Go higher!\n")

        print(f'Congratulations! {randInt} was the correct answer!\n')
        playAgain = input("Would you like to play again? (Y/N) \n")
        if playAgain == "Y":
            guess = 0
            randInt = random.randint(0, 9)

    print("Thanks for playing!")

guessNum()