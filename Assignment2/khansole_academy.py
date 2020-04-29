"""
File: khansole_academy.py
-------------------------
This program is meant to help a user learn basic arithmetic,
generating basic math problems for the user to answer, letting
them know if their answer is correct or not, and asking until they
get a sufficient number correct in a row.
"""

import random

NUM_TO_WIN = 3
RANDOM_MIN = 10
RANDOM_MAX = 99

def main():
    """
    This function randomly generates simple addition problems with
    double digit integers. It first generates two random double digit
    numbers, asks the user for the answer, and checks the result to
    see if the user is correct, letting them know if their answer
    is right or wrong. The program also keeps track of how many answers
    the user gets correct in a row, and continues to ask new problems
    until the user gets three correct in a row.
    """

    addition_problem()

def addition_problem():

    num_correct = 0
    while num_correct != 3:
        # random.seed(1)
        num1 = random.randint(RANDOM_MIN, RANDOM_MAX)
        num2 = random.randint(RANDOM_MIN, RANDOM_MAX)
        total = num1 + num2
        print("What is " + str(num1) + "+" + str(num2) + "?")
        guess = int(input())
        if guess == total:
            num_correct += 1
            if num_correct != 3:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(total))
            num_correct = 0
    if num_correct == 3:
        print("Correct!  You've gotten " + str(num_correct) + " correct in a row.")
        print("Congratulations!  You mastered addition.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
