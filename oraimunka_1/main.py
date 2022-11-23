#!/usr/bin/env python3

def szamlista():
    parts = []
    for i in range(1, 15+1):
        parts.append(str(i))
    res = "".join(parts)
    return res

def main():
    print(szamlista())

#############################################################################

if __name__ == '__main__':
    main()