def trajet(nbMarches, hauteur):

    longueur = ((nbMarches*hauteur)*10)*7

    print("Pour "+ str(nbMarches) + " marches de " + str(hauteur) + "cm,")
    print("le gardien parcours "+str(longueur/10)+"m par semaine.")

trajet(75, 28)