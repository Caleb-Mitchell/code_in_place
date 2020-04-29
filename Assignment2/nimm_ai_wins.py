"""
File: nimm.py
-------------------------
Add your comments here.
"""

STARTING_STONES = 20
STARTING_TURN = 1


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    num_stones = STARTING_STONES
    turn = STARTING_TURN

    while num_stones > 0:
        if num_stones == STARTING_STONES:
            print("There are 20 stones, and you may start.")
            print("The last player to take a stone loses.")
        else:
            print("There are " + str(num_stones) + " stones left.")
        remove_stones = input("Human, " + "would you like to remove 1 or 2 stones? ")
        if remove_stones == '1' or remove_stones == '2':
            remove_stones = int(remove_stones)
            num_stones -= remove_stones
            if turn == 1:
                turn += 1
            else:
                turn -= 1
        else:
            while remove_stones != '1' or remove_stones != '2':
                remove_stones = input("Please enter 1 or 2: ")
                if remove_stones == '1' or remove_stones == '2':
                    remove_stones = int(remove_stones)
                    num_stones -= remove_stones
                    if turn == 1:
                        turn += 1
                        break
                    else:
                        turn -= 1
                        break
        if num_stones == 2 or num_stones % 2 == 1:
            print("I will take 1 stone.")
            num_stones -= 1
            hit_enter = input("Hit Enter.")
            while hit_enter != '':
                hit_enter = input("Hit Enter.")
        if num_stones == 3 or num_stones % 2 == 0:
            print("I will take 2 stones.")
            num_stones -= 2
            hit_enter = input("Hit Enter.")
            while hit_enter != '':
                hit_enter = input("Hit Enter.")
        # elif remove_stones % 2 == 0:
        #     print("I will take 2 stones.")
        #     num_stones -= 2
        #     hit_enter = input("Hit Enter.")
        #     while hit_enter != '':
        #         hit_enter = input("Hit Enter.")
        # elif remove_stones % 2 == 1:
        #     print("I will take 1 stone.")
        #     num_stones -= 1
        #     hit_enter = input("Hit Enter.")
        #     while hit_enter != '':
        #         hit_enter = input("Hit Enter.")
# zero-nimsum (unpaired multiples of 1,2,4) numbers from 1-20, these are the numbers I want the computer to make
    #1, not 2, not 3, 4, not 5, 6, not 7, 8, not 9,
    #10, not 11, 12, not 13, 14, not 15, 16, not 17, 18, not 19,
    '''
 if 19 make 18
 if 18 make 16
 if 17 make 16
 if 16 make 14
 if 15 make 14
 if 14 make 12
 if 13 make 12
 if 12 make 10
 if 11 make 10
 if 10 make 8
 if 9 make 8
 if 8 make 6
 if 7 make 6
 if 6 make 4
 if 5 make 4
 if 4 make 2
 if 3 make 1
 if 2 make 1
    '''
        # if remove_stones == 3:
        #     print("I will take 2 stones.")
        #     num_stones -= 2
        #     hit_enter = input("Hit Enter.")
        #     while hit_enter != '':
        #         hit_enter = input("Hit Enter.")
        # elif remove_stones % 2 == 0:
        #     print("I will take 1 stone.")
        #     num_stones -= 1
        #     hit_enter = input("Hit Enter.")
        #     while hit_enter != '':
        #         hit_enter = input("Hit Enter.")
        # else:
        #     print("I will take " + str(remove_stones) + " stones as well.")
        #     hit_enter = input("Hit Enter.")
        #     while hit_enter != '':
        #         hit_enter = input("Hit Enter.")
        #     num_stones -= remove_stones
    print("Game over, the computer wins!!!")

# def stone_collection:


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
