"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy, where players
alternate taking stones until there are zero left.
This game is set between one human player, and the computer.
The computer will win every time.
"""

STARTING_STONES = 20        # sets the number of stones to start the game with


def main():
    """
    This program initiates a game of Nimm between the user and the
    computer, with a set number of starting stones and with the game
    first turn taken by the computer. Turns alternate, with each player
    taking either 1 or 2 stones per turn. The game ends when there are
    zero stones left, and whoever takes the last stone is the loser.
    The computer will always win, by starting first and maintaining
    a 'winning position', by always forcing the user to a 'losing position.'
    """
    num_stones = STARTING_STONES

    while True:         # creates a loop for the player to play again if they would like
        while num_stones > 0:
            if num_stones == STARTING_STONES:
                # explains the rules briefly, and the computer takes the first turn taking 1 stone
                print("")
                print("")
                print("-" * 50)
                print("There are " + str(STARTING_STONES) + " stones, The last player to take a stone loses..")
                print("I'll start, taking 1. Now there are 19.")
                print("")
                num_stones -= 1
            elif num_stones == 1:
                # tells the user they have lost the game, asks if they would like to play again
                print("There is only 1 stone left, the computer wins.")
                print("")
                play_again = input("Play again? 'y' or 'n': ")
                if play_again == 'n' or play_again == '':
                    # if they respond with 'n' or anything else, it breaks the loop and the program ends
                    break
                elif play_again == 'y':
                    # if they would like to play again, starts the game over and resets the number of stones
                    num_stones = STARTING_STONES
                    print("")
                    print("")
                    print("-" * 50)
                    print("There are " + str(STARTING_STONES) + " stones, The last player to take a stone loses..")
                    print("I'll start, taking 1. Now there are 19.")
                    print("")
                    num_stones -= 1
            else:
                # play continues with the computer asking the user how many stones they would like to take
                print("There are " + str(num_stones) + " stones left.")
            remove_stones = input("Human, " + "would you like to remove 1 or 2 stones? ")
            # validates that the user typed '1' or '2'
            if remove_stones == '1' or remove_stones == '2':
                remove_stones = int(remove_stones)
                num_stones -= remove_stones
            else:
                # if the user types anything other than '1' or '2' they are asked to try again
                while remove_stones != '1' or remove_stones != '2':
                    remove_stones = input("Please enter 1 or 2: ")
                    if remove_stones == '1' or remove_stones == '2':
                        remove_stones = int(remove_stones)
                        num_stones -= remove_stones
                        break
            # these are the numbers at which the computer must always take two stones
            # in order to always maintain a 'winning position.' the computer must always
            # take 1 stone if the remaining number of stones is any other number not
            # present in the list
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
