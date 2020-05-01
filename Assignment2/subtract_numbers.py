"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    This program subtracts one number from another, after asking the user
    for each number. We can assume that the user will enter valid real numbers!
    """
    print("This program subtracts one number from another.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("The result is " + (str(num1 - num2)))

# This provided line is required at the end of a Python file
# to call the main() function.


if __name__ == '__main__':
    main()
