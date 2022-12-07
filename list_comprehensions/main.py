def t1(list):
    return [x.upper()+"!" for x in list]

def t2(list):
    return [x.capitalize() for x in list]

def t3(n):
    return [0] * n

def t4(list):
    return [x*2 for x in list]

def t5(list):
    return [int(x) for x in list]

def t6(s):
    return [int(c) for c in s]

def t7(s):
    return [len(c) for c in s.split(" ")]

def t8(s):
    return [c[0] for c in s.split(" ")]

def t9(s):
    return list(zip([c for c in s.split(" ")], [len(c) for c in s.split(" ")]))

def t10(max):
    res = ""
    for x in range(max):
        if x<10 and x%2==0:
            res+=str(x)
    return [int(c) for c in res]

def t11(max):
    nums = ""
    for x in range(max):
        if x**2%2==0:
            nums+=str(x**2)+" "
    return [int(x) for x in nums.split()]

def t12(max):
    nums = ""
    for x in range(max):
        if str(x**2).endswith('4'):
            nums+=str(x**2)+" "
    return [int(x) for x in nums.split()]

def t13(fch):
    end = ord('Z')
    char = fch

    result = ""

    while chr(char) != chr(end + 1):
        result += chr(char)
        char = char + 1
    return result

def t14(list):
    return [x.strip() for x in list]

def t15(list):
    return ''.join(str(x) for x in list)

def check(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

def main():
    print("1. Feladat")
    check(t1(['auto', 'villamos', 'metro']), ['AUTO!', 'VILLAMOS!', 'METRO!'])

    print()
    print("2. Feladat")
    check(t2(['aladar', 'bela', 'cecil']), ['Aladar', 'Bela', 'Cecil'])

    print()
    print("3. Feladat")
    check(t3(10),[0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    print()
    print("4. Feladat")
    check(t4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    print()
    print("5. Feladat")
    check(t5(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print()
    print("6. Feladat")
    check(t6("1234567"), [1, 2, 3, 4, 5, 6, 7])

    print()
    print("7. Feladat")
    check(t7('The quick brown fox jumps over the lazy dog'), [3, 5, 5, 3, 5, 4, 3, 4, 3])

    print()
    print("8. Feladat")
    check(t8('python is an awesome language'),['p', 'i', 'a', 'a', 'l'])

    print()
    print("9. Feladat")
    check(t9('The quick brown fox jumps over the lazy dog'), [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)])

    print()
    print("10. Feladat")
    check(t10(10), [0, 2, 4, 6, 8])

    print()
    print("11. Feladat")
    check(t11(20), [0, 4, 16, 36, 64, 100, 144, 196, 256, 324])

    print()
    print("12. Feladat")
    check(t12(20), [4, 64, 144, 324])

    print()
    print("13. Feladat")
    check(t13(ord('A')), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    print()
    print("14. Feladat")
    check(t14([' apple ', ' banana ', ' kiwi']), ['apple', 'banana', 'kiwi'])

    print()
    print("15. Feladat")
    check(t15([1, 0, 1, 1, 0, 1, 0, 0]), '10110100')

if __name__ == '__main__':
    main()