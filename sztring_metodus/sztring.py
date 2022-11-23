#!/usr/bin/env python3
#A program bekér egy nevet csupa kis betűkkel és a név első karakterét nagybetűre cseréli.
def main():
    s = input("Kérek egy nevet kis betűkkel: ")
    print("Hello "+s.strip().capitalize()+"!")

if __name__ == '__main__':
    main()