#!/usr/bin/env python3

def Palindrom(s):
    return s == s[::-1]

def main():
    s = input("Adj meg egy szót: ")
    if Palindrom(s):
        print("Palindróm")
    else:
        print("Nem Palindróm")

if __name__ == '__main__':
    main()