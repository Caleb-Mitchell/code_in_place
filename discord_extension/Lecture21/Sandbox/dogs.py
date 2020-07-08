class Dog:
    def __init__(self):
        self.times_barked = 0

    def bark(self):
        print('woof')
        self.times_barked += 1


def main():
    simba = Dog()
    juno = Dog()
    simba.bark()
    juno.bark()
    simba.bark()
    print(simba.__dict__)
    print(juno.__dict__)

