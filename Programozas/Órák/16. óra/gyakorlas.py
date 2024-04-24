"""
Feladatok:
1. Hány darab számunk van?
2. Számok összege
3. Számok szorzata
4. Legnagyobb szám
5. 3. szám értéke
6. Páratlan számok közül a legkisebb
"""

def Read(filename):
    file = open(filename, "r", encoding="utf-8")
    rows = file.readlines()
    file.close()
    return rows

def strListToIntList(lista:list, start:int=0, end:int=0)->list:
    numbers = []
    for i in range(start, len(lista)-end):
        numbers.append(int(lista[i].strip()))
    return numbers
sorok = Read("input2.txt")
szamok = strListToIntList(sorok, 1, 1)

print(f"1. feladat: {len(szamok)}")
print(f"2. feladat: {sum(szamok)}")
print(f"3. feladat:")