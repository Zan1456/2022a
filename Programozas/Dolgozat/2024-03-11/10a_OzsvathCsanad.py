"""
1. Fájl átnevezése: osztály_név.py ✔

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után ✔
2. A feladat1,2 stb fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet! ✔
3. feladat1(): számold ki a fájlban található számok összegét a tanult prog tétel segítségével! ✔
4. feladat2(): számold ki a fájlban található számok átlagát a tanult prog tétel segítségével! ✔
5. feladat3(): számold ki a fájlban található számok minimumát a tanult prog tétel segítségével! ✔
6. feladat4(): számold ki a fájlban található számok maximumát a tanult prog tétel segítségével! ✔

Kiírások:
feladat1: [eredmény] ✔
feladat2: [eredmény]
feladat3: [eredmény]
feladat4: [eredmény]
A ": " után csak az eremény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas2] név 
"""
def beolvas(fájlnév):
    fájl = open(fájlnév, encoding="utf-8")
    sorok = fájl.readlines()
    fájl.close()
    return sorok

def feladat1(első, utolsó):
    sorok = beolvas("input")
    számok=[]
    for i in range(len(sorok)):
        számok.append(sorok[i].split(","))
    összeg = 0
    for i in range(első, len(számok[0])-utolsó):
        összeg += int(számok[0][i])
    return összeg

def feladat2(első, utolsó):
    sorok = beolvas("input")
    számok=[]
    for i in range(len(sorok)):
        számok.append(sorok[i].split(","))
    összeg = 0
    for i in range(első, len(számok[0])-utolsó):
        összeg += int(számok[0][i])
    return összeg // len(számok[0])

def feladat3(első, utolsó):
    sorok = beolvas("input")
    számok=[]
    for i in range(len(sorok)):
        számok.append(sorok[i].split(","))
    minx = int(számok[0][1])
    for i in range(első, len(számok[0])-utolsó):
        if minx > int(számok[0][i]):
            minx = int(számok[0][i])
    return minx

def feladat4(első, utolsó):
    sorok = beolvas("input")
    számok=[]
    for i in range(len(sorok)):
        számok.append(sorok[i].split(","))
    maxx = int(számok[0][1])
    maxi = 0
    for i in range(első, len(számok[0])-utolsó):
        if maxx < int(számok[0][i]):
            maxx = int(számok[0][i])
            maxi = i
    return maxx

print(f"feladat1: {feladat1(1, 1)}")
print(f"feladat2: {feladat2(1, 1)}")
print(f"feladat3: {feladat3(1, 1)}")
print(f"feladat4: {feladat4(1, 1)}")