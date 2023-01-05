def plus1(liste):
    i = 0

    while i < len(liste):

        liste[i] += 1
        i+=1

    return liste

L = [7, 11, 42, 39, 2]
print(plus1(L))