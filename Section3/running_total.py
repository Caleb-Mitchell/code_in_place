

# def main():
#     num = int(input("Enter a value: "))
#     total = 0
#     while num != 0:
#         total += num
#         print("Running total is", total)
#         print("")
#         num = int(input("Enter a value: "))

def main():
    num = int(input("Enter a value: "))
    print("Running total is", num)
    while num != 0:
        total = running_total(num)
        print("Running total is", total)
        print("")


def running_total(num):
    num = int(input("Enter a value: "))
    num += num
    return num


if __name__ == '__main__':
    main()
