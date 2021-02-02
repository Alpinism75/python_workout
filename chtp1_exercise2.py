#! /usr/bin/env

""" The challenge here is to write a mysum function that does the same thing as the built-in sum function. 
However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. 
Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).
"""

def my_sum(*argsv):
    f = 0
    for x in argsv[0]:
        f += x
        # g = len(argsv[0])

    print(f)

def input_value(): 
    all = []
    while True:
        add = input("Input all the numbers (no number to add, 'q' to quit): ")
        try:
            all.append(int(add))
        except:
            if add == 'q':
                break
            else:
                print("No Number received so we'll add all numbers so far")
                my_sum(all)
                all =[]

if __name__ == "__main__":
    input_value()


"""
Write a function that takes a list of numbers. It should return the average (i.e., arithmetic mean) of those numbers.

Write a function that takes a list of words (strings). 
It should return a tuple containing three integers, representing the length of the shortest word, 
the length of the longest word, and the average word length.

Write a function that takes a list of Python objects. 
Sum the objects that either are integers or can be turned into integers, ignoring the others. 

"""