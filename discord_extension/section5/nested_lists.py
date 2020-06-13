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
    pass


def matrix_constant_multiply(c, m):
    """
    Multiplies the 2-dimensional matrix m (represented as a list of lists) 
    by a constant factor c and returns the result. m should not be modified.

    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix_constant_multiply(2, m)
    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    """
    pass


def matrix_add(m1, m2):
    """
    Adds matrices m1 and m2 together and returns the result. m1 and m2 are 
    guaranteed to be the same size. Neither m1 nor m2 should be modified.

    >>> m1 = [[1, 2], [3, 4], [5, 6]]
    >>> m2 = [[2, 3], [4, 5], [6, 7]]
    >>> matrix_add(m1, m2)
    [[3, 5], [7, 9], [11, 13]]
    """
    pass


def make_times_table(m, n):
    """
    Makes and returns a list of m rows, each with n columns. 
    Each element is found by multiplying its row number by 
    its column number, where we start counting rows and columns 
    from 1. 

    >>> make_times_table(3, 4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
    """
    pass
