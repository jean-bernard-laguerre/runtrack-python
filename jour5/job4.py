def cesar(message, decalage):

    clé = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""

    for i in range(len(message)):

        if message[i] in clé:

            for x in range(len(clé)):

                if  message[i] == clé[x]:

                    if x+decalage > (len(clé)-1):
                        resultat += clé[(x+decalage)-len(clé)-1]

                    else:
                        resultat += clé[x+decalage]

                    break
        else:
            resultat += message[i]

    return resultat

print(cesar('les zombies',10))
print(cesar('les zombies',3))