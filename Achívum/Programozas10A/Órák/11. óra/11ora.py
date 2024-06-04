# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!
file = open("input.txt", "r")
file_lista = file.readlines()
file.close

# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"

name_lista = []
palacsinta_lista = []
for i in range(len(file_lista)):
    lista = file_lista[i].strip()
    lista_reszek = lista.split()
    # lista_reszek=file_lista[i].strip().split()

    name_lista.append(lista_reszek[0])

    l = []
    for j in range(1, len(lista_reszek)):
        l.append(int(lista_reszek[j]))
    palacsinta_lista.append(l)

print("Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember")