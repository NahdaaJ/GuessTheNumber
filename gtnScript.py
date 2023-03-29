# Author: Nahdaa Jawed
# Date Started: 29/03/2023 22:30
# Date Finished: -
# Description

#Importing necessary libraries and modules.
import random

def guessNum():
    randInt = random.randint(0,9)
    guess = 0

    while guess!=randInt:
        guess = int(input("Guess a number between 1 and 10 inclusive: "))
        if guess>randInt:
            print("Too high! Go lower!")

        elif guess<randInt:
            print("Too low! Go higher!")

    print("Congratulations! You guessed correctly!")

guessNum()