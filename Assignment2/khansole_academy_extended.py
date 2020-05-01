"""
File: khansole_academy.py
-------------------------
This program is meant to help a user learn basic arithmetic,
generating basic math quizzes for the user to answer, letting
them know if their answer is correct or not, and asking until they
get a sufficient number correct in a row.

Currently addition, subtraction, division, and multiplication
problems are included, chosen at random.
"""

import random

NUM_TO_WIN = 5                  # number of total quizzes necessary to complete to win

RANDOM_MIN = 10                 # random numbers generated for addition/subtraction problems
RANDOM_MAX = 99                 # random numbers generated for addition/subtraction problems
DIVIDE_RANDOM_MIN = 1           # random numbers generated for division problems
DIVIDE_RANDOM_MAX = 99          # random numbers generated for division problems
MULTIPLY_RANDOM_MIN = 1         # random numbers generated for multiplication problems
MULTIPLY_RANDOM_MAX = 9         # random numbers generated for multiplication problems


def main():
    """
    This function randomly generates simple math quizzes of a random type
    with random numbers within a set range relative to the type of arithmetic.
    It first generates two random double digit numbers, asks the user for the answer,
    and checks the result to see if the user is correct, letting them know
    if their answer is right or wrong. The program also keeps track of how
    many answers the user gets correct in a row, and continues to ask new quizzes
    until the user gets three correct in a row.
    """
    quiz_counter = 0
    while quiz_counter < NUM_TO_WIN:    # continues to generate quizzes until you complete a set number
        generate_quiz()
        quiz_counter += 1
    if quiz_counter == NUM_TO_WIN:
        print("Congratulations, you mastered all math!")


def generate_quiz():
    quiz = random.randint(1, 4)         # random number generator determines type of arithmetic per quiz
    if quiz == 1:
        addition_quiz()
    if quiz == 2:
        subtraction_quiz()
    if quiz == 3:
        division_quiz()
    if quiz == 4:
        multiply_quiz()


def addition_quiz():
    num_correct = 0                         # set a counter to keep track so that user wins with 3 correct in a row
    while num_correct != NUM_TO_WIN:
        # random.seed(1)
        num1 = random.randint(RANDOM_MIN, RANDOM_MAX)       # generate random numbers for arithmetic
        num2 = random.randint(RANDOM_MIN, RANDOM_MAX)
        total = num1 + num2
        print("What is " + str(num1) + "+" + str(num2) + "?")   # ask the user the question and take a guess
        guess = int(input())
        if guess == total:                                   # if they're right, add to the counter, if not reset it
            num_correct += 1
            if num_correct != NUM_TO_WIN:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(total))
            num_correct = 0
    if num_correct == NUM_TO_WIN:                            # when they get a set number correct in a row they win
        print("Correct!  You've gotten " + str(num_correct) + " correct in a row.")
        print("Congratulations!  You mastered addition.")


# subsequent quiz types operate the same way, with slightly different changes per arithmetic type

def subtraction_quiz():
    num_correct = 0
    while num_correct != NUM_TO_WIN:
        # random.seed(1)
        num1 = random.randint(RANDOM_MIN, RANDOM_MAX)
        num2 = random.randint(RANDOM_MIN, num1)     # ensures that the answer is never a negative integer
        total = num1 - num2
        print("What is " + str(num1) + "-" + str(num2) + "?")
        guess = int(input())
        if guess == total:
            num_correct += 1
            if num_correct != NUM_TO_WIN:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(total))
            num_correct = 0
    if num_correct == NUM_TO_WIN:
        print("Correct!  You've gotten " + str(num_correct) + " correct in a row.")
        print("Congratulations!  You mastered subtraction.")


def division_quiz():
    num_correct = 0
    while num_correct != NUM_TO_WIN:
        # random.seed(1)
        num1 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
        num2 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
        while (num1 % num2) != 0:           # ensures that the random numbers always divide evenly
            num1 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
            num2 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
        total = num1 // num2
        print("What is " + str(num1) + "/" + str(num2) + "?")
        guess = int(input())
        if guess == total:
            num_correct += 1
            if num_correct != NUM_TO_WIN:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(total))
            num_correct = 0
    if num_correct == NUM_TO_WIN:
        print("Correct!  You've gotten " + str(num_correct) + " correct in a row.")
        print("Congratulations!  You mastered division.")


def multiply_quiz():
    num_correct = 0
    while num_correct != NUM_TO_WIN:
        # random.seed(1)
        num1 = random.randint(MULTIPLY_RANDOM_MIN, MULTIPLY_RANDOM_MAX)
        num2 = random.randint(MULTIPLY_RANDOM_MIN, MULTIPLY_RANDOM_MAX)
        total = num1 * num2
        print("What is " + str(num1) + "x" + str(num2) + "?")
        guess = int(input())
        if guess == total:
            num_correct += 1
            if num_correct != NUM_TO_WIN:
                print("Correct! You've gotten " + str(num_correct) + " correct in a row.")
        else:
            print("Incorrect. The expected answer is " + str(total))
            num_correct = 0
    if num_correct == NUM_TO_WIN:
        print("Correct!  You've gotten " + str(num_correct) + " correct in a row.")
        print("Congratulations!  You mastered multiplication.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
