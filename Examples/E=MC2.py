SPEED_OF_LIGHT = 299792458

def main():
    while True:
        kilos = float(input("Enter kilos of mass: "))
        print("e = m * c ^ 2...")
        print("m = " + str(kilos) + " kg")
        print("c = " + str(SPEED_OF_LIGHT) + " m/s")

        energy = kilos * (SPEED_OF_LIGHT ** 2)
        print("e = " + str(energy) + " joules")

        print("")


if __name__ == '__main__':
    main()
