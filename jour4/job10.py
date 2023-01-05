def produitListe(liste):

    produit = 0

    for num in liste:

        if 25 < num < 90:

            if produit == 0:
                produit = num
            else:
                produit *= num 
    return produit

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(produitListe(L))