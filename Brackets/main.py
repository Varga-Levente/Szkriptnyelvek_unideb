open_list = ["[","{","("]
close_list = ["]","}",")"]

def test(str):
    '''
    Beneneti stringen végigmegyünk, figyeljük a bracketeket
    és a stack segéd tömbünkben tároljuk a nyitott bracketeket,
    ha van bezárása akkor pop-oljuk a    tömb utolsó elemét,
    ha a stack a végén üres, akkor nincs nyitott zárójel és jó volt a sorrend,
    ha nagyobb mint nulla akkor volt bezáratlan vagy rossz helyen levő bracket
    :param str:
    :return:
    '''
    stack = []
    for i in str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
    if len(stack) == 0:
        print(str," - ", True)
    else:
        print(str, "-" , False)

def main():
    test("((5+3)*2+1)")
    test("{[(3+1)+2]+}")
    test("(3+{1-1)}")
    test("[1+1]+(2*2)-{3/3}")
    test("(({[(((1)-2)+3)-3]/3}-3)")

###########################################################

if __name__ == '__main__':
    main()

