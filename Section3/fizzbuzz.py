

def main():
    user_input = int(input("Number to count to: "))
    fizzbuzz(user_input)


def fizzbuzz(given_number):
    for i in range(1, given_number + 1):
        # if i % 15 == 0:
        if (i % 3 == 0) and (i % 5 == 0):
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    main()
