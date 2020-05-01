"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

NUM_RANDOM = 10     # number of random numbers generated
MIN_RANDOM = 0      # minimum range for random numbers
MAX_RANDOM = 100    # maximum range for random numbers

def main():
    """
    This program prints out a series of random numbers. The number of numbers printed is
    defined by constant NUM_RANDOM, and the range of the random numbers printed is defined
    by MIN_RANDOM and MAX_RANDOM respectively.
    """
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM, MAX_RANDOM))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
