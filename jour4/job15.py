def longueur(liste):
    compte = 0
    for i in liste:
        compte+=1
    return compte

def arrondi(liste):

    round = []
    chiffre = ""
    
    for n in range(longueur(liste)):
        liste[n] = str(liste[n])

        i=0

    while i < longueur(liste):

        for l in liste[i]:

            if l == ".":
                round += [int(chiffre)]
                chiffre = ""
                break
                
            else:
                chiffre += l
        i+=1

    return round

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(arrondi(L))