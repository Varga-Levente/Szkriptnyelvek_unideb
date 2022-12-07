def main():
    #Endless loop get the input from the user and check if is a number and contains digit 1 else print error message can exit with q
    print("Szám ellernőrző")
    while True:
        number = input("Please enter a number: ")
        #Check number variable type is int or float

        if number == "exit":
            break

        if number.isdigit():
            if number.isdigit() and "1" in number:
                print("OK")
            else:
                print("NEM")
        else:
            if type(number) == int or type(number) == float:
                print("OK")
            else:
                #number variable replace "." with "" and convert it to int
                numberv2 = str(number.replace(".", ""))
                if numberv2.isdigit() and "1" in numberv2:
                    print("OK")
                else:
                    print("Kérem, egy számot adjon meg!")

if __name__ == '__main__':
    main()