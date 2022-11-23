import sys
import time
def main():
    # if no args provided exit
    if len(sys.argv) == 1:
        print("Nem adott meg argomentumot")
        time.sleep(5)
        sys.exit(1)
    # get numbers from args and print char for each
    for arg in sys.argv[1:]:
        print("#"*int(arg))

if __name__ == '__main__':
    main()
