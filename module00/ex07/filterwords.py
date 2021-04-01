#!/usr/bin/env python3

import sys, string

def check_format(args):
    if len(args) != 2 or args[0].isdecimal() or not args[1].isdecimal():
        print('ERROR')
        return False
    return True

def filter_words(text, n):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split(' ')
    output = []
    for word in text:
        if len(word) > int(n):
            output.append(word)
    print(output)

def main():
    check_format(sys.argv[1:]) and filter_words(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()