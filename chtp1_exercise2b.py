#! /usr/bin/env

a = """ Write a function that takes a list of words (strings). 
It should return a tuple containing three integers, representing the length of the shortest word, 
the length of the longest word, and the average word length.
"""

x = [a.split(' ')]
f = []

for word in x:
    l = len(word)
    if l > 0:
        f.append(l)
    else:
        pass

f.sort()

print(f)


# if __name__ == "__main__":
  


"""
Write a function that takes a list of numbers. It should return the average (i.e., arithmetic mean) of those numbers.

Write a function that takes a list of words (strings). 
It should return a tuple containing three integers, representing the length of the shortest word, 
the length of the longest word, and the average word length.

Write a function that takes a list of Python objects. 
Sum the objects that either are integers or can be turned into integers, ignoring the others. 

"""