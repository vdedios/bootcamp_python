#!/usr/bin/env python3

import sys

def usage(err):
    if len(err): print(err)
    print('Usage: python operations.py <number1> <number2>\n'
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

def do_operations(args):
    sys.stdout.write(f'Sum:         {int(args[1]) + int(args[2])}\n'
                     f'Difference:  {int(args[1]) - int(args[2])}\n'
                     f'Product:     {int(args[1]) * int(args[2])}\n')
    if int(args[2]) == 0:
        sys.stdout.write(f'Quotient:    ERROR (div by zero)\n'
                         f'Remainder:   ERROR (modulo by zero)\n')
    else:
        sys.stdout.write(f'Quotient:    {int(args[1]) / int(args[2])}\n'
                         f'Remainder:   {int(args[1]) % int(args[2])}\n')

def main():
    check_input_error(sys.argv) and do_operations(sys.argv)

if __name__ == "__main__":
    main()