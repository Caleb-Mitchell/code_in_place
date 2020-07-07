"""
File: data_analysis.py
----------------------
This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""


def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """
    # create empty dict to return later
    data_dict = {}
    # read through data file
    with open(filename) as file:
        for line in file:
            # Test for name of city in line,
            # Make new str of name
            city_str = ''
            for char in line:
                if char.isalpha() or char == ' ':
                    city_str += char

            # strip leading/trailing spaces
            city_str = city_str.strip()

            # Make list out of line
            line = line.strip()
            line = line.split(',')

            # Remove city name from list
            line.pop(0)

            # Remove extra spaces in list elements
            line = [x.strip(' ') for x in line]

            # Change list numbers to ints
            for i in range(len(line)):
                line[i] = int(line[i])

            # add that str/list to dictionary
            data_dict[city_str] = line
        print(data_dict)


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """
    pass
    """
    You fill this in.  Don't forget to remove the 'pass' statement above.
    """


def main():
    filename = 'disease1.txt'

    data = load_data(filename)
    print("Loaded datafile " + filename + ":")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()
