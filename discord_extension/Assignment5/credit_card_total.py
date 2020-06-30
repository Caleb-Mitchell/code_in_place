"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


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
            line = line.split()     # FIXME split correctly, or join together certain indexes?
            # add correct indices to dictionary

            print(line)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
