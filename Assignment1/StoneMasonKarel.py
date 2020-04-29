from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    This code tells Karel to repair all columns in her world so that they each contain
    a beeper every corner up to the arch. Karel does this from west to east with
    a column in her initial location, as well every four subsequent corners until the end of the world.
    """
    repair_column()
    repair_remaining_columns()

def repair_column():
    # pre: Karel is at the base of a column facing east.
    # post: Karel has repaired the column, and is back at its base facing east.
    turn_left()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
    # to prevent a fencepost bug
    if no_beepers_present():
        put_beeper()
    descend_column()

def descend_column():
    # pre: Karen has repaired the column and is at its northernmost point, just beneath a wall.
    # post: Karen is back to the base of the column, facing east.
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def repair_remaining_columns():
    # pre: Karel is at the base of a repaired column.
    # post: Karel is at the end of her world, with all columns repaired that are able to fit every four corners.
    while front_is_clear():
        for i in range(3):
            if front_is_clear():
                move()
        if front_is_clear():
            move()
            repair_column()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
