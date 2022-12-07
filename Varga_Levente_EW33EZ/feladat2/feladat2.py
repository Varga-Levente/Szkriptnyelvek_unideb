import sys

def main():
    #get command line arguments
    args = sys.argv[1:]
    #if no arguments are given, print usage
    if len(args) == 0:
        return
    elif len(args) == 1:
        #Print all chars no duplicates
        print("".join(set(args[0])))
    else:
        #Print all chars wich conatins all in the arguments
        for i in range(0, len(args[0])):
            for j in range(1, len(args)):
                if args[0][i] not in args[j]:
                    break
                if j == len(args)-1:
                    print(args[0][i], end='')

if __name__ == '__main__':
    main()