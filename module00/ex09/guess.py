#!/usr/bin/env python3

import random, textwrap

def is_match(number, guess, it):
    if number == guess:
        if number == 42:
            print('The answer to the ultimate question of life, the universe and everything is 42.')
        print(f'You won in {it} attempts!') if it > 1 else print(f'Congratulations! You got it on your first try!')
        return True
    print('Too high!') if number > guess else print('Too low')
    return False

def main():
    guess = random.randint(1, 99)
    it = 0
    print(textwrap.dedent("""
        This is an interactive guessing game!
        You have to enter a number between 1 and 99 to find out the secret number.
        Type 'exit' to end the game.
        Good luck!
        """))
    while True:
        number = input("What's your guess between 1 and 99?\n")
        if number == 'exit':
            print('Goodbye!')
            break
        elif not number.isdecimal():
            print("That's not a number.")
        elif is_match(int(number), guess, it):
            break
        it += 1

if __name__ == '__main__':
    main()