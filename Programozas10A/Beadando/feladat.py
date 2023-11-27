'''
# 1. feladat
x = 0
while not x > 1 and not x < 5:
    x = int(input("Add meg a hetek számát [1...5]: 3 "))
    if not 1 > x or not x < 5:
        print("Hibás adatbevitel! Próbáld meg újra...")
'''
intervallum_min = 3
intervallum_max = 15
Feltetel = False
while not Feltetel:
    x = int(input(f"Adj meg egy értéket [{intervallum_min}...{intervallum_max}]"))
    if x >= intervallum_min and x <= intervallum_max:
        Feltetel = True
    else:
        print("Nem jót adtál meg")

hetnapjai = ["hetfo", "kedd"]
hetek = []
for hetszama in range(x):
    lista = []
    for nap in hetnapjai:
        ert = int(input(f"Add meg, hogy hány támadás érte az állatkertet {hetszama+1}.hét({nap}): "))
        lista.append(ert)
    hetek.append(lista)

print(hetek)

hetek_str = []
for i in range(len(hetek)):
    lista = []
    for j in range(len(hetek[i])):
        lista.append(str(hetek[i][j]))
    hetek_str.append(lista)

for het_szamlalo in range(len(hetek)):
    tamadasok = " ".join(hetek_str[het_szamlalo])
    print(f"{het_szamlalo}. hét: {tamadasok}")