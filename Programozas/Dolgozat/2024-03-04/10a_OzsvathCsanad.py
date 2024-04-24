"""
1. Fájl átnevezése: osztály_név.py ✔

Feladatok:
1. A beolvas fv-ben valósítsd meg, hogy a paraméterben megadott fájlt beolvassa, és térjen vissza a szám listával az átalakítások után. ✔
2. A feladat1,2 stb. fv-ben valósítsd meg a kért eljárásokat! A fájl beolvasásához használd a beolvas() függvényedet! ✔
3. feladat1(): számold ki a fájlokban található számok összegét a tanult prog tétel segítségével! ✔
4. feladat2(): számold ki a fájlokban található számok átlagát a tanult prog tétel segítségével! ✔
5. feladat3(): számold ki a fájlokban található számok minimumát a tanult prog tétel segítségével! ✔
6. feladat4(): számold ki a fájlokban található számok maximumát a tanult prog tétel segítségével! ✔

Input fájlok használata:
feladat1() -> input1 ✔
feladat2() -> input2 ✔
feladat3() -> input3 ✔
feladat4() -> input3 ✔

Kiírások:
feladat1: [eredmény] ✔
feladat2: [eredmény] ✔
feladat3: [eredmény] ✔
feladat4: [eredmény] ✔
A ": " után csak az eremény szerepeljen

A dolgozat python fájlját küldd el a andrasi.norbert@puskas.hu-ra az alábbi tárggyal:
[osztály][filebeolvasas1] név 
"""
def beolvas(fájlnév):
    fájl = open(fájlnév, encoding="utf-8")
    sorok = fájl.readlines()
    fájl.close()
    return sorok

def feladat1(név):
    lista = beolvas(név)
    összeg = 0
    for i in range(len(lista)):
        összeg += int(lista[i])
    return összeg
def feladat2(név, első, utolsó):
    lista = beolvas(név)
    számok = []
    for i in range(első,len(lista)-utolsó):
        számok.append(int(lista[i].strip()))
    átlag = 0
    for i in range(len(számok)):
        átlag += számok[i]
    return átlag // len(lista)
def feladat3(név, első, utolsó):
    lista = beolvas(név)
    számok = []
    for i in range(első,len(lista)-utolsó):
        számok.append(int(lista[i].strip()))
    mini = 0
    minx = számok[0]
    for i in range(len(számok)):
        if minx > számok[i]:
            mini = i
            minx = számok[i]
    return mini, minx
def feladat4(név, első, utolsó):
    lista = beolvas(név)
    számok = []
    for i in range(első,len(lista)-utolsó):
        számok.append(int(lista[i].strip()))
    maxi = 0
    maxx = számok[0]
    for i in range(len(számok)):
        if maxx > számok[i]:
            maxi = i
            maxx = számok[i]
    return maxi, maxx

print(f"feladat1: [{feladat1("input1")}]")
print(f"feladat2: [{feladat2("input2", 2, 0)}]")
print(f"feladat3: [{feladat3("input3", 1, 1)}]")
print(f"feladat4: [{feladat4("input3", 1, 1)}]")