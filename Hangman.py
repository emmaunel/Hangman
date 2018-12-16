from random import randrange, random, seed
import time




HANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']

def make_game_board(blanks, numguesses, boardimages):
    print(boardimages[numguesses])
    print(blanks)


def load_words(filename):
    lst = []
    with open(filename) as filename:
        for line in filename:
            lst.append(line.rstrip())
    return lst


def get_word(lst):
    stuff = randrange(0, len(lst), 1)
    return lst[stuff]

def make_list(mystring):
    lst = []
    for i in mystring:
        lst.append(i)
    return lst


def make_space(string):
    lst = []
    spaces = '_'
    for i in string:
        lst.append(spaces)
    return lst

def get_guess():
    return input("Guess a letter: ")


def check_in_word(guess_letter, word):
    counter = 0
    index_list = []
    a = word
    word = list(a)

    for i in word:
        if i == guess_letter:
            index_list.append(word.index(guess_letter, counter))
        counter += 1
    return index_list

def replace_letters(indexes, blanks, word):
    count = 0
    while count != len(indexes):
        for i in indexes:
            blanks.pop(indexes[count])
            blanks.insert(indexes[count], word)
            count += 1
    return blanks

def end_game(numguesses, guessword, blanks):
    if numguesses > 7:
        return False
    elif guessword == blanks:
        return True


word_from_list = get_word(load_words('words.txt'))
make_spaces = make_space(word_from_list)

answer = make_list(word_from_list)

print('Press "Y" to play or "N" to quit')
choice = input("what is your choice? ")
guesses = 0

while choice != 'exit':
    if choice == 'y':
        make_game_board(make_spaces, guesses, HANGMANPICS)
        g = get_guess()

        if check_in_word(g, answer):
            make_game_board(make_spaces, guesses, HANGMANPICS)
            fill_space = replace_letters(check_in_word(g, answer), make_spaces, g)

        else:
            guesses += 1

        if guesses == 7:
            print("\nYou guess the word wrong")

            print("The answer was " + ''.join(answer))
            break

        if answer == make_spaces:
            print("\nYou guess the answer right")
            break


        if choice == 'n':
            print("loser")
            break