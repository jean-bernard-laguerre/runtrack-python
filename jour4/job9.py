def minMax(liste):

    min = liste[0]
    max = liste[0]

    i=1
    
    while i < len(liste):

        if liste[i] < min:
            min = liste[i]

        elif liste[i] > max:
            max = liste[i]

        i+=1


    print ("min: ",min)
    print ("max: ",max)

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
minMax(L)