"""
File: word_guess.py
-------------------
Fill in this comment.
"""

# maybe i could cut up an image of cloud and use that?

import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    # random.seed(1)

    word_list = []
    for line in open(LEXICON_FILE):
        line = line.strip()
        word_list.append(line)

    random_word = random.choice(word_list)
    # print(random_word)
    return random_word

    # index = random.randrange(3)
    # if index == 0:
    #     return 'HAPPY'
    # elif index == 1:
    #     return 'PYTHON'
    # else:
    #     return 'COMPUTER'


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    current_guesses = INITIAL_GUESSES           # needs to be set before game loop

    unknown_word = hide_characters(secret_word)   # create hidden word changing letters to '-'
    display_word = ''.join(unknown_word)          # create string to display from unknown word

    while True:
        print("The word now looks like this: " + str(display_word))

        # next display INITIAL_GUESSES
        print("You have " + str(current_guesses) + " guesses left.")

        # ask for input from user as a guess
        letter_guess = input("Type a single letter here, then press enter: ")
        letter_guess = letter_guess.upper()

        if letter_guess == '':
            print("Please guess a letter.")
        elif (letter_guess in secret_word) and (letter_guess not in display_word):
            print("That guess is correct.")
            # add correct guess to display_word while preserving dashes
            display_word = add_letters(secret_word, display_word, letter_guess)
            display_word = ''.join(display_word)
        elif (letter_guess in secret_word) and (letter_guess in display_word):
            print("You have already guessed: " + str(letter_guess) + ", please guess a new letter.")
        elif len(letter_guess) > 1:
            print("Guess should only be a single character.")
        else:
            current_guesses -= 1
            print("There are no " + str(letter_guess) + "'s in the word.")

        if current_guesses == 0:
            print("Sorry, you lost. The secret word was: " + str(secret_word))
            break

        # end game and exit loop
        if display_word == secret_word:
            print("")
            print("Congratulations, the word is: " + str(secret_word))
            break


def add_letters(secret_word, display_word, letter_guess):
    new_string = []
    for letter in secret_word:
        if letter_guess == letter:
            new_string.append(letter)
        elif letter in display_word:
            new_string.append(letter)
        else:
            new_string.append("-")
    return new_string


def hide_characters(secret_word):
    hidden_word = []
    for letter in secret_word:
        if letter != "-":
            hidden_word.append('-')
        else:
            hidden_word.append(letter)
    return hidden_word


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
