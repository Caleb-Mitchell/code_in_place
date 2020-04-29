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
        print("There are " + str(num_stones) + " stones left.")
        remove_stones = input("Player " + str(turn) + " would you like to remove 1 or 2 stones? ")
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
    print("Game over, the winner is Player " + str(turn) + "!!!")

# def stone_collection:


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
