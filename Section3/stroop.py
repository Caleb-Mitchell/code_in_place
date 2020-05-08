
# windows only
# from colorama import init
# init(autoreset=True)


import time
import random

from termcolor import colored

PHASE_TIME_S = 10


def main():
    print_intro()
    is_phase_1 = True  # color printed will be same as font-color
    run_phase(is_phase_1)
    is_phase_1 = False
    run_phase(is_phase_1)


def run_phase(is_phase_1):
    print("-" * 80)
    if is_phase_1 is True:
        test_number = 1
        start_test(test_number)
    elif is_phase_1 is False:
        test_number = 2
        start_test(test_number)

    test(is_phase_1)


def test(is_phase_1):
    time1 = time.time()
    answers_correct = 0
    while True:
        time2 = time.time()
        if (time2 - time1) < PHASE_TIME_S:
            time2 = time.time()
            test_result = single_run_test(is_phase_1)
            if test_result is True:
                print("it worked!")
                print("")
                answers_correct += 1
            if test_result is False:
                print("it worked, but wrong answer!")
                print("")
        if (time2 - time1) >= PHASE_TIME_S:
            print("Time is up. You got " + str(answers_correct) + " questions correct in " +
                  str(PHASE_TIME_S) + " seconds.")
            print("")
            input("Press enter to continue.")
            print("")
            break


def start_test(test_number):
    print("Test " + str(test_number) + " will last " + str(PHASE_TIME_S) + " seconds, hit enter to begin.")
    print("-" * 80)
    input("Press enter to continue")
    print("")


def single_run_test(is_phase_1):
    if is_phase_1 is False:
        font_color = random.randint(1, 3)
        if font_color == 1:
            print_in_color(random_color_name(), 'red')
        if font_color == 2:
            print_in_color(random_color_name(), 'blue')
        if font_color == 3:
            print_in_color(random_color_name(), 'pink')
    else:
        font_color = random.randint(1, 3)
        if font_color == 1:
            print_in_color('red', 'red')
        if font_color == 2:
            print_in_color('blue', 'blue')
        if font_color == 3:
            print_in_color('pink', 'pink')
    print("What color is the word written in? ", end='')
    answer = str(input())
    if (answer == "red") and font_color == 1:
        return True
    elif (answer == "blue") and font_color == 2:
        return True
    elif (answer == "pink") and font_color == 3:
        return True
    else:
        return False


def print_intro():
    '''
    Function: print intro
    Prints a simple welcome message
    '''
    print('This is the Stroop test! Name the font-color used:')
    print_in_color('red', 'red')
    print_in_color('blue', 'blue')
    print_in_color('pink', 'pink')
    print("")


def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'pink'])


def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'pink': # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))


if __name__ == '__main__':
    main()
