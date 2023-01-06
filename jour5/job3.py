def diagonale(taille):
    for x in range(taille+2):
        for y in range(taille+2):

            if (y == 0 or y == taille+1):
                print("|", end="")

            elif (x == 0 or x == taille+1) and (y != 0 and y != taille+1):
                print("-", end="")

            else:
                if y == ((taille+1) - x):
                    print(" ", end="")
                else:
                    print("#", end="")
        print("")

diagonale(10)