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
    convert_dog_years(humanyears)
    print(dog_years)

def convert_dog_years():
    human_age = input("Enter an age in human years: ")
    return human_age * DOG_AGE_CONVERSION

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
