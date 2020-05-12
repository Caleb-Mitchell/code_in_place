#!/usr/bin/env python3



def main():
    print("Enter choice (1/2):")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = int(input())
    if choice == 1:
        temp1 = float(input("Enter temperature in Fahrenheit: "))
        temp2 = (temp1 - 32) * (5/9)
        print("Temperature: " + str(temp1) + " F = " + str(temp2) + " C")
    elif choice == 2:
        temp1 = float(input("Enter temperature in Celsius: "))
        temp2 = (temp1 * (9/5)) + 32
        print("Temperature: " + str(temp1) + " C = " + str(temp2) + " F")
    else:
        print("Please enter 1 or 2")


if __name__ == '__main__':
    main()
