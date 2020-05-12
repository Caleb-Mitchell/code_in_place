
SHEETS_PER_ROLL = 160
SHEETS_PER_VISIT = 6


def main():
    current_tp = float(input("Enter the amount of rolls you have: "))
    toilet_visits = float(input("Enter the number of toilet visits per day: "))

    print("How long = " + str(SHEETS_PER_ROLL) + " sheets per roll * number of rolls / "
          "(" + str(SHEETS_PER_VISIT) + " sheets per toilet visit * toilet visit per day)...")

    print("Number of rolls = " + str(current_tp) + " rolls")
    print("Toilet visits = " + str(toilet_visits) + " per day")

    days_to_last = int(round(SHEETS_PER_ROLL * current_tp / (SHEETS_PER_VISIT * toilet_visits)))

    print("You will last " + str(days_to_last) + " days!")
    print("")


if __name__ == '__main__':
    main()
