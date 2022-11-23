#!/usr/bin/env python3

def diamond(h):
    for i in range(1, h, 2):
        print(" " * (h // 2 - i // 2), "*" * i)
    for i in range(h, 0, -2):
        print(" " * (h // 2 - i // 2), "*" * i)

def main():
    magassag = int(input("A gyémánt magassága: "))
    if(int(magassag)%2!=0):
        diamond(magassag)
    else:
        print("Páros szám nem elfogadott!")

########################################################x

if __name__ == '__main__':
    main()