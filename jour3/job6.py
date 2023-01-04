alphabet = "abcdefghijklmnopqrstuvwxyz"*10


def pyramide():
    i=1 
    x=0

    while i <= 15:
        print(alphabet[x:(x+i)])

        x = x+i
        i += 1

pyramide()