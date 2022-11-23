#!/usr/bin/env python3
import os
import shutil

def main():

    print("-" * 27)
    print("Create an empty source file")
    print("-" * 27)
    print("1) Python [py]")
    print("2) C      [c]")
    print("q) quit")

    workingDir = os.getcwd()
    inp = input()

    match inp :
        case '1':
            with open(workingDir +'/' + "base.py", "w") as newAlap:
                shutil.copy(workingDir + "/" + "base_python.py", "base.py")
        case '2':
            with open(workingDir +'/' + "base.c", "x") as newC:
                # We can make a base file for each language
                #shutil.copy(workingDir + "/" + "base_C.py", "base.py")
                pass
        case 'q':
            return 0

if __name__ == "__main__":
    main()