def in_common(l1, l2):
    # find the number of elements present in both lists (same_elements)
    # return same_elements / (sum of lengths of both lists)
    same_elements = 0
    for elem in l1:
        if elem in l2:
            same_elements += 1
    print(same_elements)
    return same_elements / (len(l1) + len(l2))


def calc_score(netflix_history1, netflix_history2, fav_books1, fav_books2):
    """
    >>> percent_in_common(['a', 'b', 'c', 'd'], ['c', 'd', 'm', 'n', 'x', 'z'])
    0.2
    """
    pass


def new_friend(name_list, compatibility_scores):
    """
    >>> name_list = ['Michelle', 'Joe']
    >>> compability_scores = [1, 0.8]
    >>> new_friend(name_list, compatibility_scores)
    ['Michelle', 1]
    """
    pass

def main():
    l1 = []
    l2 = []
    while True:
        user_input = input('User 1. Please enter your favorite books, one at a time. Press enter when finished: ')
        if user_input == '':
            break
        else:
            l1.append(user_input)
    while True:
        user_input = input('User 2. Please enter your favorite books, one at a time. Press enter when finished: ')
        if user_input == '':
            break
        else:
            l2.append(user_input)

    percent_in_common = in_common(l1, l2)
    print(percent_in_common)



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
