"""
Algoritmus:

- Lista készítése a beírt kódszavakból
- Fennmaradó utótagok (suffixek) ellenőrzése
- Ha nem talál utótagot - akkor egyértelműen dekódolható
- Ha talál utótagot, akkor listához adás
- Ha bármely utótag megegyezik a bármely kódszóval - akkor nem egyértelműen dekódolható
- Ha nem egyezik meg kódszóval - akkor a fennmaradó utótag listához adása (ha nincs duplikáció)
- Addig ismétli amíg nem marad egyedi fennmaradó utótag
                

"""
import sys
def stopScript():
    x = input()
    sys.exit()

intCodeWord = int(input("Hany kodszot szeretne hasznalni? [integer valtozoban]  --> "))
listCodeWord = []   # lista ami csak a beírt kódszavakat tartalmazza
listCombined = []   # lista ami tartalmazza a kódszavakat és a fennmaradó utótagokat

i = 0
while(i<intCodeWord):
    cw = input(f"Irja be a(z) {i+1}. kodszot: ")
    listCodeWord.append(cw)
    listCombined.append(cw)
    i += 1


print("Ellenorzes, hogy a kodszavak egyertelmuen dekodolhatoak-e (Sardinas-Patterson modszer)...")

flag = True
while(flag):

    # fennmaradó utótagok ellenőrzése a listában
    for cw1 in listCombined:
        initlength = len(listCombined)
        tmpList = []
        for cw2 in listCombined:
            if cw2.startswith(cw1) and cw1 != cw2:
                danglingSuffix = cw2[len(cw1):]
                if danglingSuffix in listCodeWord:
                   print("Nem egyertelmuen dekodolhato!")
                   stopScript()
                else:
                    tmpList.append(danglingSuffix)

    # utótagok hozzáadás az ideiglenes listából a kombinált listába
    for item in tmpList:
        listCombined.append(item)

        # duplikációk törlése
    newList = []
    for i in listCombined:
        if i not in newList:
            newList.append(i)
    listCombined = newList

    # Ha nem lett új egyedi utótag hozzádva a listához - vége, egyértelműen dekódolható
    if len(listCombined) == initlength:
        print("Egyertelmuen dekodolhato!")
        flag = False
        stopScript()