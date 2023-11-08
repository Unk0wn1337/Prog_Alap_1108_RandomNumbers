def kettesFeladat(szam:int):
    print("szám: ",szam)
    while (szam>9):
        print("Következő számjegy", szam%10)
        szam = szam // 10
        print("Az aktuális szám ",szam)

    print("Az utolsó számjegy",szam)

def kettesFeladatMasikMegoldas(szam:int):
    szovegSzam:str = str(szam)
    index = 0
    while index <= len(szovegSzam):
        print(szovegSzam[index])
        index+=1

def ermedobas():
    index:int = 0
    f:int = 0
    fHossz:int = 0
    maxHossz:int = 0
    elozoStringF = False

    while index < 10:
        jel:str = input("F/I: ")
        while not (jel == 'f' or jel == 'f' or jel == 'i' or jel == 'I'):
            jel: str = input("nem jó, F/I-t adj meg: ")
        if jel == 'f' or jel == 'F':
            f += 1
            if elozoStringF:
                fHossz += 1
            elozoStringF = True
        else:
            print("Aktuális hossz",fHossz)
            elozoStringF = False
            #Itt összehasonlitjuk a max hosszt az aktuális hosszal!
            if(maxHossz<fHossz):
                maxHossz = fHossz
            fHossz = 0
        index += 1

    print(f"F-ek száma: {f}")
    if(maxHossz<fHossz):
        maxHossz =fHossz
    print(f"F-ek leghosszabika: {fHossz}")

