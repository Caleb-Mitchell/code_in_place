"""
File: dog_years.py
------------------
This program will ask the user for a human age, then print the equivalent
dog age using the fact that there are seven dog years per human year.
"""


def main():
    num = int(input("Enter a value: "))
    total = 0
    while num != 0:
        total += num
        print("Running total is", total)
        print("")
        num = int(input("Enter a value: "))


if __name__ == '__main__':
    main()
