"""
File: dog_years.py
------------------
This program will ask the user for a human age, then print the equivalent
dog age using the fact that there are seven dog years per human year.
"""


def main():
    num = int(input("Enter a value: "))
    running_total = num
    while num != 0:
        print("Running total is", running_total)
        print("")
        num = int(input("Enter a value: "))
        running_total = update_running_total(num, running_total)


def update_running_total(num, running_total):
    running_total += num
    return running_total


if __name__ == '__main__':
    main()
