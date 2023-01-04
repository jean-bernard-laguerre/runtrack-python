def boucle100():
    i = 0
    while (i <= 100):
        if ((i%5 == 0) and (i%3 == 0)):
            print("fizzbuzz")
        elif (i%3 == 0):
            print("buzz")
        elif (i%5 == 0):
            print("fizz")
        i+=1

boucle100()