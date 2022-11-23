#!/usr/bin/env python3

def hamming(w1, w2):
    '''
    Bemenetként kapunk két szrringet majd ellenőrizzük a hosszát,
    ha egyezik akkor végigmegyünk a karaktereken és ha eltérés van,
    akkor növeljük a d(distance) változót, majd kiírjuk az eredményt
    :param w1:
    :param w2:
    :return:
    '''
    if(len(w1)!=len(w2)):
        print("A két szó hosszúsága nem egyenlő")

    l = len(w1)
    i = 0
    d = 0
    while(i<l):
        if(w1[i]!=w2[i]):
            d=d+1
        i=i+1

    print("A két szó hamming távolsága: "+str(d))

def main():
    w1 = "toned"
    w2 = "roses"
    hamming(w1, w2)
########################################################

if __name__ == '__main__':
    main()