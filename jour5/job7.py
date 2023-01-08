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
    
    print(mot[0:len(mot)])

    x = len(mot)-1
    nouveauMot = list(mot)

    while x > 0:

        if(mot[x] > mot[x-1]):

            y = x
            min = x

            while y < len(mot):

                if mot[x-1] < mot[y] < mot[min]:
                    min = y 

                y +=1

            nouveauMot[x-1], nouveauMot[min] = nouveauMot[min], nouveauMot[x-1]
            return ''.join(nouveauMot[0:x]) + ''.join(sorted(nouveauMot[x:]))

        x -= 1

    return mot
    

print(plusLoin())