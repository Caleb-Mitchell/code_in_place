def read_dict_from_file(filename):
    """
    Takes in the name of a file containing a recipe or
    pantry list and reads it into a dictionary.

    An example doctest using the file above:
    >>> read_dict_from_file('recipe.txt')
    {'flour': 200.0, 'salt': 2.5}
    """
    blank_dict = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line = line.split(':: ')        # ["flour, "200]
            blank_dict[line[0]] = float(line[1])
    return blank_dict


def can_make(recipe, pantry):
    """
    Given the contents of the pantry, returns a boolean indicating
    whether or not it is possible to follow the recipe. Note that
    the parameters to this function are dictionaries, and not
    filenames. The pantry should not be modified in this function
    """
    for ingredient in recipe:
        if (ingredient in pantry) and (recipe[ingredient] <= pantry[ingredient]):
            print("You can make the recipe, yay!")
            return True
        print("Uh oh, looks like you can't make it! :(")
        return False


def make_recipe(recipe, pantry):
    for ingredient in recipe:
        pantry[ingredient] -= recipe[ingredient]
    print(pantry)


def main():
    user_pantry = input("Enter pantry file: ")
    pantry = read_dict_from_file(user_pantry)
    user_recipe = input("What should we cook today?!")
    recipe = read_dict_from_file(user_recipe)
    while user_recipe != '':
        recipe = read_dict_from_file(user_recipe)
        if can_make(recipe, pantry):
            make_recipe(recipe, pantry)
        user_recipe = input("What should we cook today?!")


if __name__ == "__main__":
    main()
