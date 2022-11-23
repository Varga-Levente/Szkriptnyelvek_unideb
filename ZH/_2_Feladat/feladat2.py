#!/usr/bin/env python3

def main():
    odd = [x for x in range(0, 30) if x % 2 == 1]
    even = [x for x in range(0, 30) if x % 2 == 0]
    print("Páratlan számok: "+str(odd))
    print("Páros számok: "+str(even))

if __name__ == "__main__":
    main()
