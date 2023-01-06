def premier(num):
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True


def boucle1000():
    i = 1
    while (i <= 1000):
        if (premier(i)):
            print(i)
        i+=1

boucle1000()