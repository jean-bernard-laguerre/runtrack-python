def longueur(liste):

    long = 0
    for i in liste:
        long+=1
    return long

def plusLong(str, n):
    
    mots = []
    mot = ""
    longMots = ""
    
    for lettre in str:
        if lettre == " ":
            mots += [mot]
            mot = ""
        else:
            mot += lettre
    if mot:
        mots += [mot]
    
    for m in mots:
        if  longueur(m) > n:
            longMots += m +" "

    return longMots

phrase = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"

print(plusLong(phrase, 3))