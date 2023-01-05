def doublons(liste):
    nouvelleListe = []
    for num in liste:
        if num not in nouvelleListe:
            nouvelleListe += [num]
    return nouvelleListe


L = [10,20,30,20,10,50,60,40,80,50,40]
print(doublons(L))