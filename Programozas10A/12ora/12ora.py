from collections import Counter
# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input.txt"

file=open(filename, "r", encoding="utf-8")
file_lista=file.readlines()
file.close()

name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    _lista=file_lista[i].strip()
    _lista_parts=_lista.split()

    # így is lehet: _lista_parts=file_lista[i].strip().split()
    name_list.append(_lista_parts[0])

    _l=[]
    for j in range(1,len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    pancake_list.append(_l)

# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
fejlec="Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
print(fejlec)

# 3) Add meg, hogy márciusban ki sütötte a legtöbb palacsintát!
legtobb = 0
ind = 0
for i in range(len(pancake_list)):
    if legtobb < pancake_list[i][2]:
        legtobb = pancake_list[i][2]
        ind = i
print(name_list[ind])

# 4) Add meg, hogy ki sütötte az évben a legkevesebb palacsintát!
osszes = []
for i in range(len(pancake_list)):
    adde = 0
    for j in range(12):
        adde += pancake_list[i][j]
    osszes.append(adde)
legtbb = 0
inde = 0
for i in range(len(osszes)):
    if legtbb < osszes[i]:
        legtbb = osszes[i]
        inde = i
print(name_list[inde])

# 5) Add meg, hogy az a személy, akinek B-vel kezdődik a neve, Májusban hány palacsintát sütött.
for i in range(len(name_list)):
    if name_list[i][0] == "B":
        print(pancake_list[i][4])

# 6) Volt-e olyan személy, akinek az évben változó teljesítménye volt?
#       Pl: sütött valamennyit, majd a következő hónapban többet, a következőben az előzőnél kevesebbet stb
#       írd ki a személy nevét!
elemzes = []
for i in range(len(pancake_list)):
    lista = []
    for j in range(10):
        if pancake_list[i][j] < pancake_list[i][j+1] and pancake_list[i][j+1] > pancake_list[i][j+2]:
            liste = 0
        elif pancake_list[i][j] < pancake_list[i][j+1] and pancake_list[i][j+1] < pancake_list[i][j+2]:
            liste = 1
        elif pancake_list[i][j] > pancake_list[i][j+1] and pancake_list[i][j+1] > pancake_list[i][j+2]:
            liste = 2
        lista.append(liste)
    elemzes.append(lista)

def most_frequent(List):
    return max(set(List), key = List.count)

for i in range(len(elemzes)):
    esd = most_frequent(elemzes[i])
    if esd == 0:
        print(name_list[i] + " Változó")
    elif esd == 1:
        print("Növekvő")
    else:
        print("Csökkenő")
