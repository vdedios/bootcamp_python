#!/usr/bin/env python3

import sys

def usage(err):
    print(err + 'Usage: python operations.py <number1> <number2>\n'
           'Example:\n'
            '   python operations.py 10 3')

def check_input_error(args):
    if len(args) == 1:
        usage('')
        return False
    if len(args) > 3:
        usage('too many arguments')
        return False
    if len(args) < 3:
        usage('missing argument')
        return False
    if not (args[1].isdecimal() and args[2].isdecimal()):
        usage('only numbers')
        return False
    return True

def calc(a, b):
    print(f'Sum:         {a + b}')
    print(f'Difference:  {a - b}')
    print(f'Product:     {a * b}')
    if b == 0:
        print(f'Quotient:    ERROR (div by zero)')
        print(f'Remainder:   ERROR (modulo by zero)')
    else:
        print(f'Quotient:    {a / b}')
        print(f'Remainder:   {a % b}')

def main():
    check_input_error(sys.argv) and calc(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == "__main__":
    main()