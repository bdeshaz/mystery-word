import random
import re


######################################
#           """ Dictionary Import """

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

def choose_level():
    print("Choose your level. Enter [E] for Easy, [M] for Medium, [H] for Hard.")

    level = input('> ').lower()

    for letter in level:
        if letter not in 'emh' :
            print('You entered the wrong letter, try again!')
            choose_level()
        if letter == 'h':
            print("You will get as many guesses as letters in word.")
            return level
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

def level_word_list(level,dict_list):
    if level == 'e':
        return easy_words(dict_list)
    if level == 'm':
        return medium_words(dict_list)
    else:
        return hard_words(dict_list)

######################################
#            """ RANDOM_WORD """
def random_word(words):
    random_word = random.choice(words)
    return random_word

######################################

#            """ DISPLAY_WORD """
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
def is_word_complete(word, guessed_letters):

    for letter in word:
        if letter in guessed_letters:
            pass
        else:
            return False
    return True

######################################

#            """ GUESSES """
def guesses(word):


    guessed_letters = []

    if len(word) < 9:

        while len(guessed_letters) < 9:
            guess = input("Guess a letter: ").lower()

            if len(guess) > 1:
                print("You typed too many letters, try again")
            elif not guess.isalpha():
                print("You typed something weird, type letters, try again")
            elif guess in guessed_letters:
                print("You guessed that letter already! Try again")
            else:
                guessed_letters.append(guess)
                display_word(word, guessed_letters)

                if is_word_complete(word, guessed_letters) == True:
                    print("You win! The word was {}.".format(word.title()))
                    return
                else:
                    pass
    else:

        while len(guessed_letters) <= len(word):
            guess = input("Guess a letter: ").lower()

            if len(guess) > 1:
                print("You typed too many letters, try again")
            elif not guess.isalpha():
                print("You typed something weird, type letters, try again")
            elif guess in guessed_letters:
                print("You guessed that letter already! Try again")
            else:
                guessed_letters.append(guess)
                display_word(word, guessed_letters)

                if is_word_complete(word, guessed_letters) == True:
                    print("You win! The word was {}.".format(word.title()))
                    return
                else:
                    pass


######################################
#       RUN_GAME
welcome()
level = choose_level()
list_from_level = level_word_list(level,words_dict_list)
the_word = random_word(list_from_level)
print(the_word)
guessed_letters = guesses(the_word)

######################################
if __name__ == "__main__":
    pass
