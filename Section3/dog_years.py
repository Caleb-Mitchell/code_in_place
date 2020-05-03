"""
File: dog_years.py
------------------
This program will ask the user for a human age, then print the equivalent
dog age using the fact that there are seven dog years per human year.
"""

DOG_AGE_CONVERSION = 7

def main():
    """

    """
    human_age = int(input("Enter an age in human years: "))
    dog_age = convert_dog_years(human_age)
    print("The age in dog years is , ", dog_age)

def convert_dog_years(human_age):
    return human_age * DOG_AGE_CONVERSION


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
