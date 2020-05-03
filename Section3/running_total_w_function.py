"""
File: dog_years.py
------------------
This program will ask the user for a human age, then print the equivalent
dog age using the fact that there are seven dog years per human year.
"""


def main():
    num = int(input("Enter a value: "))
    print("Running total is", num)
    print("")
    total = num
    while num != 0:
        total = running_total(total)
        print("Running total is", total)
        print("")


def running_total(total):
    num = int(input("Enter a value: "))
    total += num
    return total


if __name__ == '__main__':
    main()
