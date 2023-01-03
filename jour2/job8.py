def alimentSaison(type, saison):

    match type:

        case "fruit":
            if(saison == "ete"):
                print("Poire, fraise, cassis")
            elif(saison == "hiver"):
                print("orange, mandarine et kiwi")
            else:
                print("\_(--)_/")

        case "legume":
            if(saison == "ete"):
                print("artichaut, aubergine,navet")
            elif(saison == "hiver"):
                print("carotte, topinambour, endive")
            else:
                print("\_(--)_/")
        
        case _:
            print("\_(--)_/")

alimentSaison("fruit", "ete")
alimentSaison("legume", "ete")
