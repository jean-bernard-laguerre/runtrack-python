def inverseur(str):
    i=len(str)
    while i>0:
        print(str[i-1], end="")
        i-=1
    print("")

inverseur("Anakin")
inverseur("Obi Wan")
