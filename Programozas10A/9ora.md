# 9. óra 2023.11.27

## Intervallum ellenőrzése

```Python
intervallum_min = 3
intervallum_max = 15

x = input(f"Adj meg egy értéket [{intervallum_min}...{intervallum_max}]")
if x > intervallum_min and x < intervallum_max:
    print("Jó számot adtál meg")
else:
    print("Nem jó számot adtál meg")
```

## Szám bekérése addig, ameddig nem lesz a feltételnek megfelelő érték

```Python
intervallum_min = 3
intervallum_max = 15
Feltetel = False

while not Feltetel:
    x = int(input(f"Adj meg egy értéket [{intervallum_min}...{intervallum_max}]"))
    if x >= intervallum_min and x <= intervallum_max:
        Feltetel = True
    else:
        print("Nem jót adtál meg")
```

## Lista feltöltése elemekkel

```Python
hetnapjai = ["hetfo", "kedd"]
hetek = []
for hetszama in range(x):
    lista = []
    for nap in hetnapjai:
        ert = int(input(f"Add meg, hogy hány támadás érte az állatkertet {hetszama+1}. hét({nap}): "))
        lista.append(ert)
    hetek.append(lista)

print(hetek)
```

## 2. faladat

```Python
hetek_str = []
for i in range(len(hetek)):
    lista = []
    for j in range(len(hetek[i])):
        lista.append(str(hetek[i][j]))
    hetek_str.append(lista)

for het_szamlalo in range(len(hetek)):
    tamadasok = " ".join(hetek_str[het_szamlalo])
    print(f"{het_szamlalo}. hét: {tamadasok}")
```

## Megoldás másképp

```Python
for het_szamlalo in range(len(hetek)):
    str_ = str(f"{het_szamlalo}. hét: ")
    for nap_szamlalo in range(len(hetek[het_szamlalo])):
        str_ += str(hetek[het_szamlalo]+ " " +[nap_szamlalo])
    print(str)
```
