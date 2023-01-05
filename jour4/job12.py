def longueur(liste):
    compte = 0
    for i in liste:
        compte+=1
    return compte

def tri(liste):

    while True:
        
        echange = 0

        for i in range(longueur(liste)):

            if liste[i] < liste[i-1] and i > 0:

                x = liste[i]
                liste[i] = liste[i-1]
                liste[i-1] = x

                echange += 1

        if echange == 0:
            break

    return liste

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(tri(L))