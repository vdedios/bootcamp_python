#!/usr/bin/env python3

import sys

def whois(string):
    num = int(string)
    if num == 0:
        return "I'm Zero."
    if num % 2 == 0:
        return "I'm Even."
    return "I'm Odd."

def main ():
    print(whois(sys.argv[1]) if len(sys.argv) == 2 and sys.argv[1].isdecimal()
        else 'ERROR')

if __name__ == "__main__":
    main()