#!/usr/bin/env python3

def isAnagram(str1, str2):
    '''
    :param str1:
    :type str1: String
    :param str2:
    :type str2: String
    :return: True or False

    Lowercase strippelt szringek összehasonlítása a sorted
    függfény használatával, ami rendezi a stringeket majd
    visszaad egy igaz vagy hamis értéket.
    '''
    if (sorted(str1.lower().strip()) == sorted(str2.lower().strip())):
        return True
    else:
        return False

def isAnagram2(str1, str2):
    '''
    :param str1:
    :type str1: String
    :param str2:
    :type str2: String
    :return: True or False

    Rendezem a két stringet külön külön majd a rendezett
    stringeket összehasonlítom és visszatérek az értékkel.
    '''
    x = [str1[i] for i in range(0, len(str1))]
    x.sort()
    y = [str2[i] for i in range(0, len(str2))]
    y.sort()

    if (x == y):
        return True
    else:
        return False


def main():
    string1 = "listen";
    string2 = "silent";
    print(isAnagram(string1, string2))
    print(isAnagram.__doc__)
    print(isAnagram2(string1, string2))
    print(isAnagram2.__doc__)

########################################################x

if __name__ == '__main__':
    main()