import random
import sys
import time


def display_hangman(limit):
    print()
    if limit == 5:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    elif limit == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    elif limit == 3:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    elif limit == 2:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")

    elif limit == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |       \n"
              "__|__\n")

    elif limit == 0:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("You couldn't guess in provided attempts \t\tYou are hanged!!!\n")


def select_word(file_path):
    """ Opens file and select return a random word from file"""
    words = None
    with open(file_path, 'r') as textfile:
        words = list(textfile.read().split())

    return random.choice(words)


def user_input(word, limit, tested_alphabet):
    print(f"Word is : {word}\n"
          f"You have {limit} attempts remaining\n")

    user_alphabet = 'Alias'
    # alphabet once checked
    while len(user_alphabet) != 1:
        user_alphabet = input('Enter your alphabet from a-z : ')
        if len(user_alphabet) != 1 or user_alphabet.isalpha() == False:
            user_alphabet = input(
                "Wrong Input! Enter your alphabet from a-z  ")
        if user_alphabet in tested_alphabet:
            user_alphabet = input(
                'Alphabet once entered! type another alphabet : ')

    return user_alphabet


def check_and_replace(alphabet, word, word_hidden, limit):
    check_position = [n for (n, e) in enumerate(word) if e == alphabet]
    if len(check_position) != 0:
        print("Right Guess! :) ")
        word_hidden = list(word_hidden)
        for position in check_position:
            word_hidden[position] = alphabet

        return ''.join(word_hidden), limit
    else:
        print('\nWrong Guess! :( Lost an attempt\n')
        display_hangman(limit-1)
        return word_hidden, limit - 1


def play_game(word):
    limit = 6
    word_hidden = len(word) * '*'
    tested_alphabet = []
    while limit != 0:
        alphabet = user_input(word_hidden, limit, tested_alphabet)
        tested_alphabet.append(alphabet)
        word_hidden, limit = check_and_replace(
            alphabet, word, word_hidden, limit)
        if word_hidden == word:
            print('\n\n\t\t\tHurahh'
                  '\t\tCongratulations U Guessed it Right '
                  f'\t\tThe word is "{word_hidden}"')
            break


def main(file_path):
    word = select_word(file_path)

    # attempts remaining with the player
    condition = True
    while condition:
        condition = play_game(word)


if __name__ == '__main__':
    main(sys.argv[1])
