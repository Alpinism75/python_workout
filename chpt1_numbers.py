#! /usr/bin/env

"""     Write a function (guessing_game) that takes no arguments.

        When run, the function chooses a random integer between 0 and 100 (inclusive).

        Then ask the user to guess what number has been chosen.

        Each time the user enters a guess, the program indicates one of the following:

            Too high

            Too low

            Just right

        If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.

        The program only exits after the user guesses correctly.
"""
import random

def guessing_game():
    rand_int = random.randint(0, 101)
    x = 0
    print(rand_int)
    while x < 5:
        guess = input("Try guessing what the random number is?  ")
        try:
            if rand_int > int(guess):
                print("Too low")
            elif rand_int < int(guess):
                print("Too high")
            elif rand_int == int(guess):
                print("Just right")
                x = 10
            else:
                print("Input not recognised") 
        except:
            print("Input not recognised")

if __name__ == "__main__":
    guessing_game()   