alphabet = "abcdefghijklmnopqrstuvwxyz"

def testMot(mot):
    for lettre in mot:
        if(lettre not in alphabet):
            print("Mot Invalide")
            return False
    return True

def plusLoin():
    
    while True:
        mot = input("Entrez un mot: ")
        if testMot(mot):
            break

    x = len(mot)-1
    nouveauMot = list(mot)

    while x > 0:

        y = x-1

        while y > 0:

            if(mot[x] > mot[y]):
                nouveauMot[y], nouveauMot[x] = nouveauMot[x], nouveauMot[y]
                return(''.join(nouveauMot))

            y-=1
        x -= 1

    return mot
    

print(plusLoin())