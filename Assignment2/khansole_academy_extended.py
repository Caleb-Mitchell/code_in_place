"""
File: khansole_academy.py
-------------------------
This program is meant to help a user learn basic arithmetic,
generating basic math quizzes for the user to answer, letting
them know if their answer is correct or not, and asking until they
get a sufficient number correct in a row.
"""

import random

NUM_TO_WIN = 5

RANDOM_MIN = 10
RANDOM_MAX = 99
DIVIDE_RANDOM_MIN = 1
DIVIDE_RANDOM_MAX = 99
MULTIPLY_RANDOM_MIN = 1
MULTIPLY_RANDOM_MAX = 9

def main():
    """
    This function randomly generates simple math quizzes with
    double digit integers. It first generates two random double digit
    numbers, asks the user for the answer, and checks the result to
    see if the user is correct, letting them know if their answer
    is right or wrong. The program also keeps track of how many answers
    the user gets correct in a row, and continues to ask new quizzes
    until the user gets three correct in a row.
    """
    quiz_counter = 0
    while quiz_counter < NUM_TO_WIN:
        generate_quiz()
        quiz_counter += 1
    if quiz_counter == NUM_TO_WIN:
        print("Congratulations, you mastered all math!")


def generate_quiz():
    quiz = random.randint(1, 4)
    if quiz == 1:
        addition_quiz()
    if quiz == 2:
        subtraction_quiz()
    if quiz == 3:
        division_quiz()
    if quiz == 4:
        multiply_quiz()


def addition_quiz():
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


def subtraction_quiz():
    num_correct = 0
    while num_correct != 3:
        # random.seed(1)
        num1 = random.randint(RANDOM_MIN, RANDOM_MAX)
        num2 = random.randint(RANDOM_MIN, num1)
        total = num1 - num2
        print("What is " + str(num1) + "-" + str(num2) + "?")
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
        print("Congratulations!  You mastered subtraction.")


def division_quiz():
    num_correct = 0
    while num_correct != 3:
        # random.seed(1)
        num1 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
        num2 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
        while (num1 % num2) != 0:
            num1 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
            num2 = random.randint(DIVIDE_RANDOM_MIN, DIVIDE_RANDOM_MAX)
        total = num1 // num2
        print("What is " + str(num1) + "/" + str(num2) + "?")
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
        print("Congratulations!  You mastered division.")



def multiply_quiz():
    num_correct = 0
    while num_correct != 3:
        # random.seed(1)
        num1 = random.randint(MULTIPLY_RANDOM_MIN, MULTIPLY_RANDOM_MAX)
        num2 = random.randint(MULTIPLY_RANDOM_MIN, MULTIPLY_RANDOM_MAX)
        total = num1 * num2
        print("What is " + str(num1) + "x" + str(num2) + "?")
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
        print("Congratulations!  You mastered multiplication.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
