"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

COUNTDOWN_START = 10


def main():
    """
    This program starts at 10, counts down by 1 10 times,
    and finally prints "Liftoff!" calling for the spaceship to launch!
    """
    count_down = COUNTDOWN_START    # sets the beginning of the count down
    for i in range(COUNTDOWN_START):
        print(str(count_down))
        count_down -= 1             # counts down by 1 each time
    print("Liftoff!")


# This provided line is required at the end of a Python file
# to call the main() function.


if __name__ == "__main__":
    main()
