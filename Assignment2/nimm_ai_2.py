"""
File: nimm.py
-------------------------
Add your comments here.
"""

STARTING_STONES = 19

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    num_stones = STARTING_STONES

    while num_stones > 0:
        if num_stones == STARTING_STONES:
            print("There are 20 stones, I'll start, now there are 19.")
            print("The last player to take a stone loses.")
        else:
            print("There are " + str(num_stones) + " stones left.")
        remove_stones = input("Human, " + "would you like to remove 1 or 2 stones? ")

        if remove_stones == '1' or remove_stones == '2':
            remove_stones = int(remove_stones)
            num_stones -= remove_stones
        else:
            while remove_stones != '1' or remove_stones != '2':
                remove_stones = input("Please enter 1 or 2: ")
                if remove_stones == '1' or remove_stones == '2':
                    remove_stones = int(remove_stones)
                    num_stones -= remove_stones
                    break

        # take_two = [3, 4, 6, 8, 10, 12, 14, 16]
        take_two = [3, 5, 7, 9, 11, 13, 15, 17, 19]
        if num_stones in take_two:
            print("I will take 2 stones.")
            num_stones -= 2
            hit_enter = input("Hit Enter.")
            while hit_enter != '':
                hit_enter = input("Hit Enter.")
        else:
            print("I will take 1 stone.")
            num_stones -= 1
            hit_enter = input("Hit Enter.")
            while hit_enter != '':
                hit_enter = input("Hit Enter.")
    print("Game over, the computer wins!!!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
