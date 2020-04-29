"""
File: liftoff.py
----------------------
This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""


def main():
    """
    This program starts at 10, counts down by 1 10 times,
    then prints "Liftoff!" calling for the spaceship to launch!
    """
    count_down = 10
    for i in range(10):
        print(str(count_down))
        count_down -= 1
    print("Liftoff!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
