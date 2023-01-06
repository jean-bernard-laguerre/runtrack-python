def notesMath(notes):
    x=0
    while x < len(notes):

        if notes[x]%5 > 2:

            notes[x] += 5 - notes[x]%5
        x+=1
    return notes

L = [8, 34, 38, 48, 2, 76, 9, 83, 7, 84, 91]
print(notesMath(L))