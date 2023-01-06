alphabet = "abcdefghijklmnopqrstuvwxyz"*10


def pyramide():
    
    i=1 
    x=0

    while i <= 15:
        print(alphabet[x:(x+i)])

        x += i
        i += 1


def pyramide2():

    i=1
    x=0

    while i <= 15:

        y = x+i

        while x < y:
            print(alphabet[x],end="")
            x += 1

        print("")

        x = y
        i += 1
        

pyramide()
pyramide2()