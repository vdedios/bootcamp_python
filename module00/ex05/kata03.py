#!/usr/bin/env python3

phrase = "The right format"

def main():
    print(phrase.rjust(42, '-'), end = '')

if __name__ == "__main__":
    main()