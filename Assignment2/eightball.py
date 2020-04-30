"""
Write a program to simulate a magic eight ball. The program should
prompt the user to type a yes or no question and give a random
answer from a set of predetermined answers.
"""

import random


def main():
    question = input("Ask a yes or no question: ")
    while question != '':
        i = random.randint(1, 5)
        if i == 1:
            print("As I see it, yes.")
        if i == 2:
            print("Ask again later.")
        if i == 3:
            print("Better not tell you now.")
        if i == 4:
            print("Cannot predict now.")
        if i == 5:
            print("Concentrate and ask again.")
        question = input("Ask a yes or no question: ")


if __name__ == '__main__':
    main()
