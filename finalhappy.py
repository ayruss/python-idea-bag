empty = []
inp = int(raw_input("Enter your number\n>"))


def square(n):
    return int(n) * int(n)


def prepare_number(n):
    print sum(map(square, map(int, list(str(n)))))
    return sum(map(square, map(int, list(str(n)))))


def happy_number(inp):
    print ""
    happy = False
    unhappy = False
    while True:
        empty.append(inp)
        if inp == 1:
            happy = True
            break
        if inp == 4:
            unhappy = True
            break
        inp = prepare_number(inp)
        if inp in empty:
            unhappy = True
            break
    if unhappy == True:
        print "Unhappy Number"
    elif happy == True:
        print "Happy Number"


happy_number(inp)
