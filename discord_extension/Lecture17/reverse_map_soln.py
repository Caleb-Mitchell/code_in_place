def main():
    print('hello world')
    ages = {
        'Mehran':50,
        'Gary':70,
        'Chris':32,
        'Brahm':23,
        'Adele':32,
        'Lionel':32,
        'Rihanna':32,
        'Stephen':32,
        'Skrillex':32
    }
    reversed = reverse(ages)

    print('Reversed:')
    for key in reversed:
        print(key, reversed[key])

def reverse(original):
    # should create and return a new dictionary where
    # the values of the original are now keys!
    reversed = {}
    for key in original:
        value = original[key]
        if not value in reversed:
            reversed[value] = []
        reversed[value].append(key)
    return reversed

if __name__ == '__main__':
    main()