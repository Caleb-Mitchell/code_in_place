

AGE_LIMIT = 18


def main():
    age = int(input("Enter your age: "))
    if age >= AGE_LIMIT:
        print("You can vote!")
    else:
        print("Sorry, you can't vote yet!")



if __name__ == '__main__':
    main()
