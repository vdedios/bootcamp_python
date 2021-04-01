#!/usr/bin/env python3

import datetime

d = (3,30,2019,9,25)

def main():
    print(datetime
          .datetime(d[2], d[3], d[4], d[0], d[1])
          .strftime("%d/%m/%Y %H:%M"))

if __name__ == "__main__":
    main()