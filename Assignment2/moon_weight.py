"""
File: moon_weight.py
--------------------
Add your comments here.
"""

WEIGHT_CONVERSION = 0.165

def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    earth_weight = int(input("Enter a weight on Earth: "))
    moon_weight = earth_weight * WEIGHT_CONVERSION
    print("Equivalent weight on moon: " + str(moon_weight))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
