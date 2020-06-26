"""
File: encoded_string.py
-----------------------
This program expands strings encoded with run-length encoding.
"""


def expand_encoded_string(encoded):
    """
    This function is passed a run-length encoded string and
    returns the expanded version of that string.
    >>> expand_encoded_string('B4')
    'BBBB'
    >>> expand_encoded_string('m1e2t1')
    'meet'
    >>> expand_encoded_string('B1o2k2e2p1e1r1!3')
    'Bookkeeper!!!'
    """
    # split every two characters into a list
    new_string = [encoded[i:i+2] for i in range(0, len(encoded), 2)]
    # print(new_string)

    # loop through each string in list
    new_list = []
    for i in range(0, len(new_string)):
        num = new_string[i][1]
        letter = new_string[i][0]
        # multiply the char by the number
        new_letters = int(num) * letter
        new_list.append(new_letters)
    # print(new_list)

    # return list to a string
    final_word = ''.join(new_list)
    return final_word

def main():
    result = expand_encoded_string('B4')
    print(result)      # should print: BBBB

    result = expand_encoded_string('m1e2t1')
    print(result)      # should print: meet

    result = expand_encoded_string('B1o2k2e2p1e1r1!3')
    print(result)      # should print: Bookkeeper!!!


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
