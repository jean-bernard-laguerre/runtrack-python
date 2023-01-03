def testNombre(nombre):
    if (nombre > 0):
        print("positif")
    elif (nombre < 0):
        print("negatif")
    else:
        print("zero")

testNombre(15)
testNombre(-15)
testNombre(0)