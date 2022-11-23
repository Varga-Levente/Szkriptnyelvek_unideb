#!/usr/bin/env python3
MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def hangrend(word):
    """
    Kapunk egy szót, amiben megnézzük, hogy van e mély és magas magánhangzó,
    majd a két boolean változót ellenőrizve visszatérünk a megelelő válasszal.

    :param word:
    :return:
    """
    melymagan =['a','á','o','ó','u','ú']
    magasmagan=['e','i','í','ü','ű','ö','ő','é']
    voltmely = False
    voltmagas = False
    for betu in word:
        if betu in melymagan:
            voltmely = True
        elif betu in magasmagan:
            voltmagas = True
    if voltmely and not voltmagas:
        return('mély')
    elif not voltmely and voltmagas:
        return('magas')
    elif voltmely and voltmagas:
        return('vegyes')
    else:
        return('semmilyen')


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for w in words:
        print(w+" → "+hangrend(w))

########################################################x

if __name__ == '__main__':
    main()