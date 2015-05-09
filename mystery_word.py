import random
import re
import os


######################################
#           """ Dictionary Import """
# imports dictionary from computer and breaks
# it into a list to be used in game

with open("/usr/share/dict/words") as sample:
    words_dict = sample.read()
    words_dict = words_dict.split()
    lowered_words_dict = []
    for word in words_dict:
        lowered_words_dict.append(word.lower())
    words_dict_list = lowered_words_dict


######################################
#       """ GAME_WELCOME """

def welcome():
    print("Welcome to Mystery Word!")

######################################
#       """ CHOOSE_LEVEL """
# Allows the user to choose a level where
# the difficulty is based on the length of
# the word

def choose_level():
    print("Choose your level. Enter [E] for Easy, [M] for Medium, [H] for Hard.")

    level = input('> ').lower()

    if level not in 'emh' :
        print('You entered the wrong letter, try again!')
        choose_level()
    elif len(level) > 1:
        print('You tried to many characters, try again!')
    else:
        print("You will get 8 letter-guesses to find out what word is given. Good Luck!")
        return level

######################################
#            """ EASY_MODE """

""" Evaluate if word has between 4-6 letters """

def easy_words(words):

    easy_mode_words = []

    for word in words:
        if len(word) >= 4 and len(word) < 7:
            easy_mode_words.append(word)
    return easy_mode_words

######################################
#            """ NORMAL_MODE """
""" Evaluate if word has between 6-8 letters """


def medium_words(words):
    medium_mode_words = []

    for word in words:
        if len(word) >= 6 and len(word) < 9:
            medium_mode_words.append(word)
    return medium_mode_words

######################################
#            """ HARD_MODE """
""" Evaluate if word has 8 or more letters """

def hard_words(words):
    hard_mode_words = []

    for word in words:
        if len(word) >= 8:
            hard_mode_words.append(word)
    return hard_mode_words

######################################
#            """ GO_TO_LEVEL """
# Takes the input from the user and
# starts the level chosen

def level_word_list(level,dict_list):
    if level == 'e':
        print("Welcome to EASY mode")
        return easy_words(dict_list)
    if level == 'm':
        print("Welcome to MEDIUM mode")
        return medium_words(dict_list)
    else:
        print("Welcome to HARD mode")
        return hard_words(dict_list)

######################################
#            """ RANDOM_WORD """
# Chooses a random word from the level
# the user chose

def random_word(words):
    random_word = random.choice(words)
    return random_word

######################################
#            """ DISPLAY_WORD """
# Displays the letters in the word if
# the letter guessed is in the word from
# Random Word function

def display_word(word, guessed_letters):

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display = display + letter.upper() + " "
        else:
            display = display + "_" + " "
    print(display[:-1])

######################################
#            """ IS_WORD_COMPLETE """
# Checks to see if word is complete

def is_word_complete(word, guessed_letters):

    for letter in word:
        if letter not in guessed_letters:
            return
    return True

######################################
#            """ GUESS_INPUT """
# Checks the input given from user and
# adds the guess to a list. Gives feedback
# if user didn't follow rule. Clears screen

def guess_input(word, guessed_letters):

    guess = input("Guess a letter: ").lower()

    if len(guess) > 1:
        print("You typed too many letters, try again")
        guess_input(word)
    elif not guess.isalpha():
        print("You typed something weird, type letters, try again")
        guess_input(word)
    elif guess in guessed_letters:
        print("You guessed that letter already! Try again")
        guess_input(word)

    os.system('clear')
    guessed_letters.append(guess)
    display_word(word, guessed_letters)

    return guess

######################################
#            """ GUESSES """
# Keeps count of the guesses and keeps
# the list of guesses. Determines if
# user wins or not

def the_game(word):

    guess_counter = 8
    guessed_letters = []

    while guess_counter > 0:
        guess = guess_input(word, guessed_letters)
        print("Guessed letters: {}".format(', '.join(guessed_letters).upper()))

        if guess not in word:
            guess_counter -= 1
            print("That's not a letter :( ")
            print('')
            print("Number of guesses left: {}".format(guess_counter))
        else:
            print("That's a letter!")
            print('')
            print("Number of guesses left: {}".format(guess_counter))

        if is_word_complete(word, guessed_letters):
            print("You win! The word was {}.".format(word.upper()))
            return

    print("You ran out of guesses! Play Again!"
    "The word was {}".format(word.upper()))

######################################
#       RUN_GAME

def run_game():
    welcome()
    level = choose_level()
    list_from_level = level_word_list(level,words_dict_list)
    the_word = random_word(list_from_level)
    the_game(the_word)
    play_again()

######################################
#       PLAY_AGAIN
# Allows the user to play again

def play_again():

    play_again_answer = input("""Do you want to play again? [Y] fo Yes, [N] for No. >  """).lower()
    if play_again_answer == 'y':
        run_game()
    else:
        print("Goodbye!")
        return

######################################

run_game()

######################################
if __name__ == "__main__":
    pass
