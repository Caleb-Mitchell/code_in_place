"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy, where players
alternate taking stones until there are zero left.
"""

STARTING_STONES = 20        # number of stones in the starting pile
STARTING_TURN = 1           # sets it so that Player 1 goes first


def main():
    """
    This program initiates a game of Nimm between two human players,
    with a set number of starting stones and with the game first
    turn taken by Player 1. Players turns alternate, with each player
    taking either 1 or 2 stones per turn. The game ends when there
    are zero stones left, and whoever takes the last stone is the
    loser.
    """
    num_stones = STARTING_STONES
    turn = STARTING_TURN
    while num_stones > 0:
        # ask the user if they would like to remove 1 or 2 stones
        print("There are " + str(num_stones) + " stones left")
        remove_stones = input("Player " + str(turn) + " would you like to remove 1 or 2 stones? ")
        print("")
        # validate that the user typed '1' or '2', and remove that many stones from the total
        if remove_stones == '1' or remove_stones == '2':
            remove_stones = int(remove_stones)
            num_stones -= remove_stones
            # add to the counter to keep track of whose turn it is
            if turn == 1:
                turn += 1
            else:
                turn -= 1
        else:
            # if the user doesn't type '1' or '2', ask them again to type '1' or '2'
            while remove_stones != '1' or remove_stones != '2':
                remove_stones = input("Please enter 1 or 2: ")
                print("")
                if remove_stones == '1' or remove_stones == '2':
                    remove_stones = int(remove_stones)
                    num_stones -= remove_stones
                    if turn == 1:
                        turn += 1
                        break
                    else:
                        turn -= 1
                        break
    # announce the winner based on who took the last stone
    print("Player " + str(turn) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
