def testLangage(langage):
    match langage:
        case "javascript":
            print("tu es un developpeur web")
        case "python":
            print("tu es un developpeur IA")
        case "java":
            print("tu es un developpeur logiciel")
        case "reactjs":
            print("tu es un developpeur mobile")
        case _:
            print("“un jour, je serai le meilleur developpeur...")

testLangage("javascript")
testLangage("lkkjgml")
testLangage("python")