#!/usr/bin/env python3

import math


def distance(p1, p2):
    res = "{:.8f}".format(math.sqrt( (p1[1] - p1[0])**2 + (p2[1] - p2[0])**2 ))
    return res


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()