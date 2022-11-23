def main():
    print("a,")
    for i in range(0, 72):
        num = str(i)
        if(i%12==0 or num[len(num)-1] == "5"):
            print("\t"+num)

    lista = ["NAGYBETUSSZO", "rEszLegESENNAGYbetusszo", "kisbetusszo"]
    nagylista = []

    print("\nb,")
    for i in lista:
        if(i.isupper()):
            nagylista.append(i)

    for element in nagylista:
        print("\t"+element)


    tuple = {(1, 2): "start", (2, 2): "akadály", (2, 1): "akadály", (0, 2): "cél"}
    coords = []

    print("\nc,")
    for key, value in tuple.items():
        if(value == "akadály"):
            coords.append(key)

    for coord in coords:
        print("\t"+str(coord))



if __name__ == '__main__':
    main()
