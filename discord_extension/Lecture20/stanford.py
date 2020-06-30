"""
File: stanford.py
-----------------
This program provides an example of using Student objects
"""


from student import Student


CS106A_UNITS = 5


def print_units(s):
    """
    Prints the name and number of units that student s has,
    as well as whether the student can graduate.
    """
    print(s.get_name() + " has " + str(s.get_units()) + " units")
    print(s.get_name() + " can graduate: " + str(s.can_graduate()))


def take_cs106a(s):
    """
    States that student s takes CS106A and increments number of units
    """
    print(s.get_name() + " takes CS106A!!")
    s.increment_units(CS106A_UNITS)


def main():
    mehran = Student("Mehran Sahami", 38000000)
    mehran.set_units(3)
    print_units(mehran)

    chris = Student("Chris Piech", 55000000)
    chris.set_units(179)
    print_units(chris)

    take_cs106a(mehran)
    take_cs106a(chris)

    print_units(mehran)
    print_units(chris)


if __name__ == '__main__':
    main()
