from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    This program tells Karel to draw the characters of my name, "CALEB", and to continue looping
    those characters for the full length of the world.
    """

    loop_my_name()

# Characters should take up one full 4x5 grid, and there are single corner gaps in between characters.

def loop_my_name():
    while front_is_clear():
        if front_is_clear():
            write_letter_c()
        if front_is_clear():
            move_east_next_char()
        if front_is_clear():
            write_letter_a()
        if front_is_clear():
            move_east_next_char()
        if front_is_clear():
            write_letter_l()
        if front_is_clear():
            move_east_next_char()
        if front_is_clear():
            write_letter_e()
        if front_is_clear():
            move_east_next_char()
        if front_is_clear():
            write_letter_b()
        if front_is_clear():
            move_east_next_char()

def write_letter_a():
    # pre: Karel is in corner 1x1 of the 4x5 individual character grid, facing east.
    # post: Karel is back at the original corner, facing east.
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_east()
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_west()
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLUE)
    north_one_row_east()
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_west()
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    return_to_start()

def write_letter_b():
    # pre: Karel is in corner 1x1 of the 4x5 individual character grid, facing east.
    # post: Karel is back at the original corner, facing east.
    for i in range(3):
        paint_corner(BLUE)
        move()
    north_one_row_east()
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_west()
    for i in range(3):
        paint_corner(BLUE)
        move()
    north_one_row_east()
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_west()
    for i in range(3):
        paint_corner(BLUE)
        move()
    return_to_start()

def write_letter_c():
    # pre: Karel is in corner 1x1 of the 4x5 individual character grid, facing east.
    # post: Karel is back at the original corner, facing east.
    for i in range(2):
        move()
        paint_corner(BLUE)
    move()
    north_one_row_east()
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_west()
    paint_corner(BLUE)
    move_three()
    north_one_row_east()
    paint_corner(BLUE)
    move_three()
    paint_corner(BLUE)
    north_one_row_west()
    move()
    for i in range(2):
        paint_corner(BLUE)
        move()
    return_to_start()

def write_letter_e():
    # pre: Karel is in corner 1x1 of the 4x5 individual character grid, facing east.
    # post: Karel is back at the original corner, facing east.
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLUE)
    return_to_start()
    turn_left()
    for i in range(4):
        move()
        paint_corner(BLUE)
    return_to_start()
    turn_left()
    move_two()
    turn_right()
    for i in range(3):
        move()
        paint_corner(BLUE)
    return_to_start()
    turn_left()
    move_four()
    turn_right()
    for i in range(3):
        move()
        paint_corner(BLUE)
    return_to_start()

def write_letter_l():
    # pre: Karel is in corner 1x1 of the 4x5 individual character grid, facing east.
    # post: Karel is back at the original corner, facing east.
    for i in range(3):
        paint_corner(BLUE)
        move()
    paint_corner(BLUE)
    return_to_start()
    turn_left()
    for i in range(4):
        move()
        paint_corner(BLUE)
    return_to_start()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def move_two():
    for i in range(2):
        move()

def move_three():
    for i in range(3):
        move()

def move_four():
    for i in range(4):
        move()

def north_one_row_east():
    # pre: Karel is at the eastern end of a row, facing east.
    # post: Karel moves north one row, facing west.
    turn_left()
    move()
    turn_left()

def north_one_row_west():
    # pre: Karel is at the western end of a row, facing west.
    # post: Karel moves north one row, facing east.
    turn_right()
    move()
    turn_right()

def return_to_start():
    # pre: Karel has finished a character, facing east, and is in corner(4,5) of the grid
    # post: Karel will be back to corner(1,1) of that character, facing east
    turn_around()
    if facing_south():
        move_four()
    if facing_west():
        for i in range(3):
            move()
        turn_left()
        if front_is_clear():
            for i in range(4):
                while front_is_clear():
                    move()
    turn_left()

def move_east_next_char():
    '''
    pre: Karel is at the starting corner of any given character, corner (1,1)
    post: Karel is one 4x5 grid to the east, in corner(1,1), facing east, ready to write another character,
    with one additional free corner left to leave a single corner gap in between characters
    '''
    for i in range(5):
        if front_is_clear():
            move()
        else:
            turn_around()
            turn_around()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
