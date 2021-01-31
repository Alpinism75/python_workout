#! /usr/bin/env

""" The challenge here is to write a mysum function that does the same thing as the built-in sum function. 
However, instead of taking a single sequence as a parameter, it should take a variable number of arguments. 
Thus, although you might invoke sum([1,2,3]), you’d instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).
"""

def my_sum(**args):
    params = []
    f = 0

    for x in args:
        params.append(x)
        f += x
    
    print(f)


def input_value(): 

    all = []

    while True:
        add = input("input all the numbers (no number to quit): ")
        try:
            all.append(int(add))
        except:
            print("No Number received so we'll add all numbers so far")
            break
    my_sum(all)

if __name__ == "__main__":
    input_value()
