def main():
    start = ord('a')
    end = ord('z')
    char = start

    result = ""

    while chr(char)!=chr(end+1):
        result+=chr(char)+" "
        char=char+1
    Test(result[0:-1], "a b c d e f g h i j k l m n o p q r s t u v w x y z")

def Test(got, expected):
    """

    :param got: a value received from a function
    :param expected: a value we expect to receive
    :return: True if got == expected, False otherwise
    """
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

if __name__ == '__main__':
    main()

