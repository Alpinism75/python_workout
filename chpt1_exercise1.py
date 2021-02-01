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
    rand_int = random.randint(0, 100)   # note this is inclusive - unusual!!  will include 100
    x = 0 
    # practice input and using f'ormat {strings}'
    name = input('Enter your name: ')   # just return will be an empty string
    print(f'Hello, {name}!')
    
    while True:    # initially I put a x value to control the while loop this is cleaner
        guess = input("Try guessing what the random number is?  ")
        x += 1
        try:         # could use str.isdigit(guess) to check string is integers, but went for a try, except block instead
            if rand_int > int(guess):
                print("Too low")
            elif rand_int < int(guess):
                print("Too high")
            elif rand_int == int(guess):
                print(f"""Just right
                {name}, you guessed {x} times to get the answer""")
                break
            else:
                print("Input not recognised") 
        except:
            print("Input not recognised")

if __name__ == "__main__":
    guessing_game()   


""" Modify this program, such that it gives the user only three chances to guess the correct number. 
If they try three times without success, the program tells them that they didn’t guess in time and then exits.

Not only should you choose a random number, but you should also choose a random number base, from 2 to 16, 
in which the user should submit their input. If the user inputs “10” as their guess, 
you’ll need to interpret it in the correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16 (hexadecimal).

Try the same thing, but have the program choose a random word from the dictionary, and then ask the user to guess the word. 
(You might want to limit yourself to words containing two to five letters, to avoid making it too horribly difficult.) 
Instead of telling the user that they should guess a smaller or larger number, have them choose an earlier or later word in the dict.
"""