#!/usr/bin/env python3

def decode(char, dist):
    """
    :param char:
    :param dist:
    :return:
    """
    ascii = ord(char) + dist
    if ascii > 122:
        ascii = ascii - 26
    if ascii > 90 and ascii < 97:
        ascii = ascii - 26
    if ascii < 48 or ascii > 57 and ascii < 65:
        ascii = ascii - 2

    return chr(ascii)

def main():
    msg = """
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!
    
    Aqmimjjyi:
    
    Ynyb
    """
    ascii = [decode(c, 2) for c in msg]
    print (''.join([str(elem) for elem in ascii]))

########################################################x

if __name__ == '__main__':
    main()