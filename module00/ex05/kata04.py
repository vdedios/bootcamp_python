#!/usr/bin/env python3

t = (0, 4, 132.42222, 10000, 12345.67)

def main():
    print(f'module_0{t[0]}, ex_0{t[1]}: {format(t[2], "5.2f")}, {format(t[3], ".2E")}, {format(t[4], ".2E")}')

if __name__ == "__main__":
    main()