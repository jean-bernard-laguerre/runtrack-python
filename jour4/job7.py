def compte3(liste):
    compte = 0
    for num in liste:
        if(num%3 == 0):
            compte += 1
    return compte

L = [8, 24,48,2,16]

print(compte3(L))