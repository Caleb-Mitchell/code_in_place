LEXICON = 'dictionary.txt'


def main():
    user_word = input("Word: ")     # user_input = listen
    user_word = user_word.lower()

    while user_word != '':
        words_list = []
        with open(LEXICON) as file:
            for line in file:
                line = line.strip()
                if sorted(user_word) == sorted(line):
                    words_list.append(line)
        print(words_list)
        user_word = input("Word: ")  # user_input = listen
        user_word = user_word.lower()


if __name__ == "__main__":
    main()
