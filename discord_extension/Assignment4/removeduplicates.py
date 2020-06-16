"""
File: removeduplicates.py
-------------------------
This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """
    user_list = []
    ready_more_input = True
    while ready_more_input is True:
        user_num = int(input('Enter Value (0 to stop): '))
        if user_num != 0:
            user_list.append(user_num)
        else:
            ready_more_input = False
    return user_list


def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.
    >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 1, 1])
    [1]
    >>> remove_duplicates([])
    []
    """
    no_duplicate_list = []
    for elem in num_list:
        # i need to check to see if elem is present in another location in list
        # if it is present somewhere else, don't append it?
        if elem not in no_duplicate_list:
            no_duplicate_list.append(elem)
    return no_duplicate_list


def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
