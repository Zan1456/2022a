def Adatbeolvasás(fájlnév):
    fájl = open(fájlnév)
    sorok = fájl.readlines()
    fájl.close()
    adatok = []
    for i in range(len(sorok)):
        adatok.append(sorok[i].strip().split())
    for i in range(len(adatok)):
        for j in range(len(adatok[i])):
            if not j == 0:
                adatok[i][j] = int(adatok[i][j])
    return adatok

def nullakm(lista):
    nulla = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if not j == 0:
                if lista[i][j] == 0:
                    nulla += 1
    return nulla

print(Adatbeolvasás("input.txt"))
print(f"Az elmúlt időszakban {nullakm(Adatbeolvasás("input.txt"))}db 0km megtett hónap volt.")