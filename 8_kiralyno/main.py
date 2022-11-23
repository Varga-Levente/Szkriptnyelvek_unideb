#!/usr/bin/env python3

def chess(queens):
    '''
    Kapunk egy int tömböt majd a tömb alapján módosítjuk a mátrixunk elemeit Q-ra
    :param queens:
    :return:
    '''
    rows, cols = (8, 8)
    table = [["." for i in range(cols)] for j in range(rows)]
    i = 0
    for q in queens:
        table[7-q][i] = "Q"
        i=i+1
    print("+-----------------+")
    for row in table:
        print("| "+" ".join(row)+" |")
    print("+-----------------+")

def main():
    queens = [7,3,0,2,5,1,6,4]
    queens2 = [0,4,7,5,2,6,1,3]
    print(queens)
    chess(queens)
    print("#####################################################")
    print(queens2)
    chess(queens2)

########################################################

if __name__ == '__main__':
    main()