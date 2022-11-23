#!/usr/bin/env python3

def xor(str1, str2):
    if (bool(str1) != bool(str2)):
        print("XOR")
    else:
        print("NOT XOR")

def main():
    str1 = "python"     #Sztring
    str2 = None         #Üres szring
    print(str1+" -> "+str(bool(str1)))          #Segéd kiiratás str1
    print(str(str2)+" -> "+str(bool(str2)))     #Segéd kiiratás str2
    print()
    xor(str1, str2)

########################################################

if __name__ == '__main__':
    main()