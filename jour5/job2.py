def drawRectangle(hauteur, largeur):
    for x in range(hauteur):
        for y in range(largeur):
            if (y == 0 or y == largeur-1):
                print("|", end="")
            elif (x == 0 or x == hauteur-1) and (y != 0 and y != largeur-1):
                print("-", end="")
            else:
                print(" ", end="")
        print("")
            
drawRectangle(5,10)