#!/usr/bin/env python3


def is_tridrome(word):
    """
    Returns whether or not word is a tridrome, i.e., the first three letters
    are the same as the last three letters.

    Arguments:
        word -- The word to check

    >>> is_tridrome('ENTERTAINMENT')
    True
    >>> is_tridrome('UNDERGROUND')
    True
    >>> is_tridrome('DEFENESTRATION')
    False
    >>> is_tridrome('PYTHON')
    False
    >>> is_tridrome('')
    False
    """
    pass


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def is_peaceful(word):
    """
    Returns whether a word is peaceful, i.e., whether its letters appear in
    sorted order.

    Arguments:
        word -- The word to check
    >>> is_peaceful('ABORT')
    True
    >>> is_peaceful('FIRST')
    True
    >>> is_peaceful('')
    True
    >>> is_peaceful('PYTHON')
    False
    >>> is_peaceful('CHOCOLATE')
    False
    """
    pass


def is_stacatto(word):
    """
    Returns whether a word is a stacatto word, i.e., whether the letters in
    even positions are vowels.

    Arguments:
        word -- The word to check

    >>> is_stacatto('AUTOMATIC')
    True
    >>> is_stacatto('POPULATE')
    True
    >>> is_stacatto('')
    True
    >>> is_stacatto('PYTHON')
    False
    >>> is_stacatto('SPAGHETTI')
    False
    """
    pass


def count_tridromes(filename):
    """
    Return the number of tridromes in the file
    """
    pass


def count_peaceful(filename):
    """
    Return the number of peaceful words in the file
    """
    pass


def count_stacatto(filename):
    """
    Return the number of stacatto words in the file
    """
    pass


if __name__ == "__main__":
    WORDS_FILE = "words.txt"

    print("Number of tridromes in English language: " +
          str(count_tridromes(WORDS_FILE)))
    print("Number of peaceful words in English language: " +
          str(count_peaceful(WORDS_FILE)))
    print("Number of stacatto words in English language: " +
          str(count_stacatto(WORDS_FILE)))
