# -*- coding: utf-8 -*-
def main():
    print("a,")
    adatok = []
    with open('adatok.csv', 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(',')
            adatok.append((line[0], int(line[1]), line[2]))
    print("\tAdatok beolvasva és eltárolva.")

    print("\nb,")
    esik = [data for data in adatok if data[2] == 'esik']

    with open('kimenet.csv', 'w') as f:
        for data in esik:
            f.write('{},{},{}\r'.format(data[0], data[1], data[2]))
    print("\tFájlba lett írva: " + str(esik))

    print("\nc,")
    print("\tPáratlan hőmérsékletű napok: ")
    for data in adatok:
        if data[1] % 2 == 1:
            print("\t\t" + str(data))

    print("\nd,")
    adatok.sort(key=lambda x: x[1])
    print("\tMedian: "+str(adatok[len(adatok) // 2][1])+" fok")

if __name__ == '__main__':
    main()
