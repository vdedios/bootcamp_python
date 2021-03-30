#! /usr/bin/env python3
import sys


def main():
    if len(sys.argv) == 1:
        print('No args')
    else :
        aux = ''.join(sys.argv[1:])
        for letter in aux[::-1]:
            print(letter.lower() if letter.isupper() else letter.upper(), end = '')
        print('')

if __name__ == "__main__":
    main()