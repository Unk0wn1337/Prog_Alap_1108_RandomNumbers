import  random
import math

def veletlenSzamok():
    # [10,30] közötti véletlen számokat generál
    index = 0
    while index < 10:
        szam:int = math.floor(random.random()*21 + 10)
        print(szam, end=" ")
        index+=1

    # Gyakroló feladatok
    # 1. Generálj 5 véletlen lottószámot [1,90]
    # 2. Generalj 1 veletlen kétjegyű egész számot, páros v páratlan
    # 3. Generálj 15 db egész számot [0,1] között
    # 4. Generálj egy véletelen számot 1 -10 között és szorozd meg 3-al vonj ki belőle 15-ot és szorozd be 2-vel
    # és vond ki belőle az eredeti számot eredményként és egyenlő e 5-tel
    # 5. Irj metódust, mely paraméterben kapott szövegnek kiirja a hosszát!
    # Az első 5 karakterét nagybetűvel


def gyakElso():
    index = 0
    while index < 5:
        randomSzam:int = math.floor(random.random()*90 + 1)
        print(f"Lottó számok: {randomSzam}")
        index+=1

def gyakMasodik():
    randomSzam:int = math.floor(random.random()*99 + 10)
    if randomSzam % 2 == 0:
        print(f"Páros szám {randomSzam}")
    if randomSzam % 2 == 1:
        print(f"Páratlan szám {randomSzam}")

def gyakHarmadik():
    index = 0
    osszeg = 0
    while index < 15:
        randomSzam:int = round(random.random()*1 + 0)
        print(randomSzam, end=",")
        if randomSzam == 1:
            osszeg += 1
        index+=1
    print(f"1-esek darabja: {osszeg}")

def negyedikFeladat():
    randomSzam = math.floor(random.random() * 10 + 1)
    muveletRandomSz = (((randomSzam * 3) -15 ) * 2)
    kivonasEredeti = muveletRandomSz - randomSzam
    print(kivonasEredeti)
    if kivonasEredeti == 5:
        print(f"Egyenlő 5-el {kivonasEredeti}")
    else:
        print(f"Nem egyenlő 5-el a {kivonasEredeti}")

def otodikFeladat(szoveg):
    szoveg = szoveg.upper()
    print(szoveg[:5])
