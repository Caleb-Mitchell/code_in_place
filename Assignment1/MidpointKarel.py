from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    This tells Karel to find the width of her world by placing beepers at its boundaries,
    then if there are any empty corners in between those boundary beepers to find the midpoint
    between them using additional beepers to narrow down the distance, pick up the additional beepers,
    and ultimately place a single beeper at that midpoint. If there are no empty corners and therefore
    no midpoint, then Karel will simply pick up one of the two boundary beepers so that only one remains.
    If the width of her word is only one corner, she will leave the single beeper.
    """

    determine_width()
    if no_beepers_present():
        find_midpoint()
    else:
        no_midpoint()

def determine_width():
    '''
    pre: Karel is facing east at 1st street and 1st avenue,
    and there are no beepers in the street.
    post: Karel has put beepers at both ends of her world, is facing west,
    and has taken one step west from the eastern boundary.
    '''
    put_beeper()
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()
    turn_around()
    if front_is_clear():
        move()

def find_midpoint():
    # pre: Karel has placed beepers on either boundary of the street.
    # post: Karel has finished cleaning up, standing on single beeper on midpoint.
    narrow_down()
    remove_ends()
    clean_up()

def no_midpoint():
    # pre: The width of the world is only one or two corners, so there is no true midpoint.
    # post: Karel is standing on a single beeper, whether the width the of world is one or two corners.
    pick_beeper()
    turn_around()
    if front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()

def narrow_down():
    '''
    pre: facing away from the opposite wall, one beeper at
    either end of the street (or one beeper only if street is
    one corner wide).
    post: facing away from the opposite wall, with
    street narrowed down by one beeper on opposite side.
    '''
    while beepers_present():
        if front_is_clear():
            move()
    if no_beepers_present():
        put_beeper()
    # fencepost
    if front_is_clear():
        move()
    # break out of loop here
    if beepers_present():
        turn_around()
        if front_is_clear():
            move()
    else:
        while front_is_clear():
            move()
        turn_around()
        narrow_down()

def remove_ends():
    '''
    pre: The street is full of beepers, karel is standing
    on the beeper at the midpoint.
    post: Karel is standing by a wall facing the middle
    of the beeper-filled street, with no beeper on either end.
    '''
    for i in range(2):
        while front_is_clear():
            move()
        pick_beeper()
        turn_around()

def clean_up():
    '''
    pre: Karel has just finished removing the beepers on the ends
    of the street, she is facing toward the midpoint.
    post: Karel is standing on a beeper, in the middle of
    street, and it is the only beeper present.
    '''
    while no_beepers_present():
        if front_is_clear():
            move()
    # get to the first beeper in the line of beepers
    pick_beeper()
    if front_is_clear():
        move()
    if beepers_present():
        while front_is_clear():
            move()
        turn_around()
        clean_up()
    else:
        turn_around()
        move()
        put_beeper()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
