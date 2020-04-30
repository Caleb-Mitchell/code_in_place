"""
File: nimm.py
-------------------------
Add your comments here.
"""

STARTING_STONES = 20


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    num_stones = STARTING_STONES

    while True:
        while num_stones > 0:
            if num_stones == STARTING_STONES:
                print("")
                print("")
                print("-" * 50)
                print("There are " + str(STARTING_STONES) + " stones, The last player to take a stone loses..")
                print("I'll start, taking 1. Now there are 19.")
                print("")
                num_stones -= 1
            elif num_stones == 1:
                print("There is only 1 stone left, the computer wins.")
                print("")
                play_again = input("Play again? 'y' or 'n': ")
                if play_again == 'n' or play_again == '':
                    break
                elif play_again == 'y':
                    num_stones = STARTING_STONES
                    print("")
                    print("")
                    print("-" * 50)
                    print("There are " + str(STARTING_STONES) + " stones, The last player to take a stone loses..")
                    print("I'll start, taking 1. Now there are 19.")
                    print("")
                    num_stones -= 1
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

            take_two = [3, 6, 9, 12, 15, 18]

            if num_stones in take_two:
                print("I will take 2 stones.")
                num_stones -= 2
                print("")
            else:
                print("I will take 1 stone.")
                num_stones -= 1
                print("")
        if play_again == 'n':
            break


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
