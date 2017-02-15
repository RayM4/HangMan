################################
# Main Application             #
################################

import random

from list_reader import get_default_list
from defaults import DEFAULT_LIVES, DEFAULT_LIFE_RENDER


class Hangman:
    def __init__(self):
        self.word_bank = get_default_list()
        self.current_word = self.__get_random_word()
        self.guesses = {}
        self.current_guess_string = self.__get_guess_string()
        self.max_lives = DEFAULT_LIVES
        self.current_lives = 0

    def render(self):
        self.__draw_man()
        # print(self.current_word)
        print('\n')
        self.__draw_guesses()
        print(self.current_guess_string)

    def update(self):
        self.render()
        if self.__check_game_over():
            print("GAME OVER")
            print("Word was: " + self.current_word)
            print("Press any key to continue")

        if self.__check_win():
            print('You Win')
            print("Press any key to continue")

    def guess(self, character):
        if self.__check_game_over() or self.__check_win():
            self.__reset()
        else:
            self.__check_guess(character)
        self.update()

    # internal helper functions
    def __get_guess_string(self):
        word = ''
        for c in self.current_word:
            if self.guesses.get(c):
                word += ' ' + c
            else:
                word += ' _'
        return word

    def __get_random_word(self):
        index = random.randint(0, len(self.word_bank)-1)
        return self.word_bank[index]

    def __draw_man(self):
        man = ''
        for i in range(0, self.current_lives):
            man += DEFAULT_LIFE_RENDER.get(i)
        print(man)

    def __draw_guesses(self):
        keys = list(self.guesses.keys())
        correct = '[ '
        wrong = '[ '
        for k in keys:
            if self.guesses.get(k):
                correct += k + ' '
            else:
                wrong += k + ' '
        print('Correct: ' + correct+']')
        print('Wrong: ' + wrong + ']')

    def __check_guess(self, character):
        guess = str(character).lower()
        if self.current_word.find(guess) > -1:
            self.guesses[guess] = True
        else:
            self.guesses[guess] = False
            self.current_lives += 1
        self.current_guess_string = self.__get_guess_string()

    def __check_game_over(self):
        return self.current_lives >= self.max_lives

    def __check_win(self):
        return self.current_guess_string.find('_') == -1

    def __reset(self):
        self.word_bank = get_default_list()
        self.current_word = self.__get_random_word()
        self.guesses = {}
        self.current_guess_string = self.__get_guess_string()
        self.max_lives = DEFAULT_LIVES
        self.current_lives = 0

        print("------------------------------")


if __name__ == "__main__":
    h = Hangman()
    h.render()
    while True:
        c = input('Input: ')
        h.guess(c)
