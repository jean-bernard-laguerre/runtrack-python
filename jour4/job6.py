L = [8,4,15,67,2]

def inverse(liste):
    x = liste[0]
    liste[0] = liste[4]
    liste[4] = x

print(L)
inverse(L)
print(L)