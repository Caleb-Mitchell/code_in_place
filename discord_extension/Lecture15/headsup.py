import random

FILE_NAME = "headsup.txt"

def main():

    while True:
        word_list = []
        with open(FILE_NAME) as f:
            for line in f:
                line = line.strip()
                word_list.append(line)
        game_word = random.choice(word_list)
        input('Press enter for next word:')
        print('')
        print(game_word)
        # print('Karel')

if __name__ == '__main__':
    main()