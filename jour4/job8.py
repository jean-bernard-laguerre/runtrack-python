def sommeListe(liste):
    somme = 0
    for num in liste:
        somme += num
    return somme

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
print(sommeListe(L))