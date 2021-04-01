#!/usr/bin/env python3

import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': ' / '}

def main():
    for message in sys.argv[1:]:
        if all(l.isalnum() or l.isspace() for l in message):
            for letter in message:
                sys.stdout.write(MORSE_CODE_DICT[letter.upper()])
        else:
           print('ERROR')
        if message is not sys.argv[-1]:
            print(' / ', end = '')

if __name__ == '__main__':
    main()