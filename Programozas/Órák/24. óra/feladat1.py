def AdatokBe(fájlnév):
    file = open(fájlnév, encoding="utf-8")
    rows = file.readlines()
    file.close()
    data = []
    for i in range(len(rows)):
        data.append(rows[i].strip().split())
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j > 0:
                data[i][j] = int(data[i][j])
    return data

def Összegzés(lista, sorszám):
    összeg = 0
    for i in range(len(lista[sorszám])-1):
        összeg += lista[sorszám][i+1]
    return összeg

def NapiÖsszegzés(lista, nap, karakter):
    összeg = 0
    for i in range(len(lista)):
        if lista[i][0][0] == karakter:
            összeg += lista[i][nap]
    return összeg

def Maximum(lista, nap):
    érték = lista[0][nap]
    ind = 0
    for i in range(1, len(lista)):
        if lista[i][nap] > érték:
            érték = lista[i][nap]
            ind = i
    return lista[ind][0]

def Irás(lista, fájlnév):
    összeg = 0
    for i in range(len(lista)):
        for j in range(1, len(lista[i])):
            összeg += lista[i][j]
    file = open(fájlnév, "a", encoding="utf-8")
    file.write(f"\n{str(összeg)}")
    file.close()

data = AdatokBe("feladat1.txt") # 1. feladat
print(Összegzés(data, 1)) # 2. feladat
print(NapiÖsszegzés(data, 1, "Z")) # 3. feladat
print(Maximum(data, 2)) # 4. feladat
Irás(data, "feladat1.txt")

