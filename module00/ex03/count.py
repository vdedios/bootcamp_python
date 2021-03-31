#!/usr/bin/env python3

import string

def summary(info):
    statement = (f'The text contains {info["length"]} characters\n'
                f'- {info["upper"]} upper letters\n'
                f'- {info["lower"]} lower letters\n'
                f'- {info["marks"]} punctuation marks\n'
                f'- {info["spaces"]} spaces')
    print(statement)

def text_analyzer(*args):

    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""

    if len(args) == 1:
        info = {'length' : len(args[0]), 'upper' : 0, 'lower' : 0, 'spaces' : 0, 'marks' : 0}
        for letter in args[0]:
            if letter.isupper(): info['upper'] += 1
            elif letter.islower(): info['lower'] += 1
            elif letter.isspace(): info['spaces'] += 1
            elif letter in string.punctuation: info['marks'] += 1
        summary(info)
    else :
        print('ERROR')