def enumerate(lst):
    """
    returns a nested list where each element is a list containing 
    the index of an element in the original list and the element itself. 
    These lists should appear in increasing order of indices.

    >>> enumerate(['cs106a', 'is', 'super', 'fun'])
    [[0, 'cs106a'], [1, 'is'], [2, 'super'], [3, 'fun']]
    >>> enumerate(['hello'])
    [[0, 'hello']]
    >>> enumerate([])
    []
    """
    # new_lst = []
    # for i in range(len(lst)):
    #     new_lst.append([i])
    #     new_lst[i].append(lst[i])
    # return new_lst

    # in list comprehension form
    return [[i, lst[i]] for i in range(len(lst))]


def matrix_constant_multiply(c, m):
    """
    Multiplies the 2-dimensional matrix m (represented as a list of lists) 
    by a constant factor c and returns the result. m should not be modified.

    >>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix_constant_multiply(2, m)
    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    """
    new_list = []
    for y in range(len(m)):
        inner_list = []
        for x in range(len(m[y])):
           inner_list.append(m[y][x] * c)
        new_list.append(inner_list)
    return new_list


def matrix_add(m1, m2):
    """
    Adds matrices m1 and m2 together and returns the result. m1 and m2 are 
    guaranteed to be the same size. Neither m1 nor m2 should be modified.

    >>> m1 = [[1, 2], [3, 4], [5, 6]]
    >>> m2 = [[2, 3], [4, 5], [6, 7]]
    >>> matrix_add(m1, m2)
    [[3, 5], [7, 9], [11, 13]]
    """
    # new_list = []
    # for y in range(len(m1)):
    #     inner_list = []
    #     for x in range(len(m1[y])):
    #         inner_list.append(m1[y][x] + m2[y][x])
    #     new_list.append(inner_list)
    # return new_list

    # new_list = []
    # for y in m1:
    #     inner_list = []
    #     for x in m1[y]:
    #         inner_list.append(m1[y][x] + m2[y][x])
    #     new_list.append(inner_list)
    # return new_list

    new_matrix = [[m1[y][x] + m2[y][x] for x in range(len(m1[y]))] for y in range(len(m1))]
    return new_matrix

def make_times_table(m, n):
    """
    Makes and returns a list of m rows, each with n columns. 
    Each element is found by multiplying its row number by 
    its column number, where we start counting rows and columns 
    from 1. 

    >>> make_times_table(3, 4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
    """
    x_list = []
    for y in range(m):
        inner_list = []
        for x in range(n):
            inner_list.append((x + 1) * (y + 1))
        x_list.append(inner_list)
    return x_list
