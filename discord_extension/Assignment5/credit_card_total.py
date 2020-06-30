"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill2.txt'


def main():
    """
    Add your code (remember to delete the "pass" below)
    """
    # create empty dictionary
    records = {}

    # read from file
    with open(INPUT_FILE) as file:
        for line in file:
            # strip and split
            line = line.strip()
            line = line.split()

            # if index[1] does NOT end with ']', add index[2] to end of index[1]?
            while line[1][-1] != ']':
                new_str = ''.join(line[1]) + ' ' + str(line[2])
                line[1] = new_str
                line.pop(2)

            # remove punctuation        TODO: should later use a loop like in the CIP notes
            line[1] = line[1].replace('[', '')
            line[1] = line[1].replace(']', '')
            line[2] = line[2].replace('$', '')

            # add correct indices to dictionary
            # print(line)
            if line[1] in records:
                records[line[1]] += int(line[2])
            if line[1] not in records:
                records[line[1]] = int(line[2])

    for key in records.keys():
        print(str(key) + ': $' + str(records[key]))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
