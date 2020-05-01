"""
File: khansole_academy.py
-------------------------
This program is meant to help a user learn basic arithmetic,
generating basic math problems for the user to answer, letting
them know if their answer is correct or not, and asking until they
get a sufficient number correct in a row.
"""

import random

NUM_TO_WIN = 3          # sets the number of questions necessary to answer correctly in a row to win
RANDOM_MIN = 10         # sets the minimum for random numbers used in math problems
RANDOM_MAX = 99         # sets the maximum for random numbers used in math problems

def main():
    """
    This function randomly generates a quiz composed of simple addition
    problems with double digit integers. It first generates two random
    double digit numbers, asks the user for the answer, and checks the
    result to see if the user is correct, letting them know if their answer
    is right or wrong. The program also keeps track of how many answers
    the user gets correct in a row, and continues to ask new problems
    until the user gets three correct in a row.
    """
    addition_quiz()


def addition_quiz():
    num_correct = 0         # set a counter to keep track so that user wins with 3 correct in a row
    while num_correct != NUM_TO_WIN:
        # random.seed(1)
        num1 = random.randint(RANDOM_MIN, RANDOM_MAX)       # generate random numbers for arithmetic
        num2 = random.randint(RANDOM_MIN, RANDOM_MAX)
        total = num1 + num2
        print("What is " + str(num1) + "+" + str(num2) + "?")   # ask the user the question and take a guess
        guess = int(input())
        if guess == total:                            # if they're right, add to the counter, if not reset it
            num_correct += 1
            if num_correct != NUM_TO_WIN:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(total))
            num_correct = 0
    if num_correct == NUM_TO_WIN:                    # when they get 3 correct in a row they win
        print("Correct!  You've gotten " + str(num_correct) + " correct in a row.")
        print("Congratulations!  You mastered addition.")

# This provided line is required at the end of a Python file
# to call the main() function.


if __name__ == '__main__':
    main()
