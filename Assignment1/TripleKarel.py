from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    """
    This program will tell Karel to paint the exterior of
    the three buildings using beepers! To meet the goal Karel must
    place beepers along three of the sides of each of the
    three buildings.
    """

    paint_triple_world()


def paint_triple_world():
    '''
    pre: Karel is facing west at the upper right corner of the leftmost building.
    post: The buildings each have three walls painted, with Karel one step west of the
    upper left corner of the rightmost building.
    '''
    for i in range(3):
        paint_building()
        building_transfer()

def paint_building():
    '''
    This tells Karel to paint three walls of a building, turning after each one
    to paint the next.
    pre: The unpainted wall is on her left.
    post: Three walls are painted, Karel is ready to turn the corner to the next building.
    '''
    for i in range(2):
        paint_wall()
        turn_corner()
    paint_wall()

def paint_wall():
    '''
    This tells Karel to paint a wall until the
    wall ends, and move one step past it.
    pre: Karel has an unpainted wall to her left.
    post: Karel is one step past an unpainted wall, left now clear.
    '''
    while left_is_blocked():
        put_beeper()
        move()

def turn_corner():
    turn_left()
    move()

def building_transfer():
    '''
    This tells Karel to transfer to the next
    building when she runs into it, and to position
    herself to meet the pre-condition that the wall be on her left.
    pre: front is blocked by a new building.
    post: Karel has a new unpainted wall to her left, of the next building.
    '''
    if front_is_blocked():
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
