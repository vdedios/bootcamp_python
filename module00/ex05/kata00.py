#!/usr/bin/env python3

t = (10, 42, 21)

def main():
    print('The 3 numbers are: ', end = '')
    for item in t[:-1]:
        print(f'{item}, ', end = '')
    print(f'{t[-1]}')

if __name__ == "__main__":
    main()