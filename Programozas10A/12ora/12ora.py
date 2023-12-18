# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input.txt"

file=open(filename, "r")
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
van = False
for i in range(len(pancake_list)):
    ossz = pancake_list[i][0]
    for j in range(12):
        if ossz < pancake_list[i][j]:
            if j == 11:
                continue
            elif pancake_list[i][j] > pancake_list[i][j+1]:
                van = True
                break
print(van)









