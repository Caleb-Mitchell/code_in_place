"""
File: hailstones.py
-------------------
This is a program exploring the famous 'Hailstone Sequence'
created by Douglas Hofstadter in his book 'Gödel, Escher, Bach.'
"""


def main():
    """
    This program reads a number chosen by the user, displays the hailstone
    sequence for that number, as well as displaying the number of steps
    that were necessary to eventually get that number to 1.
    """
    # start at 0 steps taken, keeping a counter
    steps = 0
    # ask user for a number
    hailstone_number1 = int(input("Enter a number: "))
    # loop will continue until the number reaches the value 1
    while hailstone_number1 != 1:
        # if number is currently even, divide by two, and add one step to counter
        if hailstone_number1 % 2 == 0:
            hailstone_number2 = int(hailstone_number1 / 2)
            steps += 1
            print(str(hailstone_number1) + " is even, so I take half: " + str(hailstone_number2))
            hailstone_number1 = hailstone_number2
        # if number is currently odd, multiply by three and add one, and add one step to counter
        elif hailstone_number1 % 2 == 1:
            hailstone_number2 = int((hailstone_number1 * 3) + 1)
            steps += 1
            print(str(hailstone_number1) + " is odd, so I make 3n + 1: " + str(hailstone_number2))
            hailstone_number1 = hailstone_number2
    # when the value is eventually one and the loop has ended, print how many steps it took to get there
    if hailstone_number1 == 1:
        print("The process took " + str(steps) + " steps to reach 1")

# This provided line is required at the end of a Python file
# to call the main() function.


if __name__ == '__main__':
    main()
