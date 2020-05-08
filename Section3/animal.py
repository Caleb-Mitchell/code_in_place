
import random


def main():
    is_phase_1 = True
    print_intro(is_phase_1)
    run_single_test(is_phase_1)


def run_single_test(is_phase_1):
    print("")
    animal = random_animal()
    print(animal)
    res = input("Type the association: ")
    correct_association = get_association(animal, is_phase_1)
    if (is_phase_1 is True) and (res != correct_association):
        print("Correct answer was " + str(correct_association))
    else:
        print("")


def print_intro(is_phase_1):
    if is_phase_1:
        print('Association test, standard')
    else:
        print('Association test, flipped')
    print('You will be asked to answer three questions.')
    print('You should associate animals as follows:')
    print('puppy', get_association('puppy', is_phase_1))
    print('panda', get_association('panda', is_phase_1))
    print('spider', get_association('spider', is_phase_1))
    print('bat', get_association('bat', is_phase_1))
    input('Press enter to start... ')


def random_animal():
    return random.choice(['puppy', 'panda', 'spider', 'bat'])


def get_association(animal, is_phase_1):
    if is_phase_1 is True:
        if animal == 'puppy' or animal == 'panda':
            return 'cute'
        if animal == 'bat' or animal == 'spider':
            return 'scary'
    else:
        if animal == 'puppy' or animal == 'panda':
            return 'scary'
        if animal == 'bat' or animal == 'spider':
            return 'cute'


if __name__ == '__main__':
    main()




