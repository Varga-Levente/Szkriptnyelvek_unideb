#!/usr/bin/env python3

from operator import*

def product(list):
    m = 1
    for i in list:
        m = mul(i, m)
    return m

def main():
    lista = [1, 2, 3]
    print(product(lista))

if __name__ == '__main__':
    main()