# py main.py input1
import sys

def read(filename, first = 0, last = 0, nameloc = 0): # Inp1 es Inp2, fel2 ✔
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close()
    data = []
    for i in range(first, len(rows)-last):
        data.append(rows[i].strip().split(","))
    names = []
    for i in range(len(data)):
        names.append(data[i][nameloc])
        data[i].pop(nameloc)
    return names, data

def maxi(lista): #inp1, fel3 ✔
    maxx = int(lista[1][0][1])
    maxi = 0
    for i in range(len(lista[1])):
        if maxx < int(lista[1][i][1]):
            maxi = i
            maxx = int(lista[1][i][1])   
    return lista[0][i]

def atlag(lista): #inp1, fel4 ✔
    osszeg = 0
    for i in range(len(lista[1])):
        osszeg += int(lista[1][i][2])
    got = []
    for i in range(len(lista[1])):
        if osszeg // len(lista[1]) <= int(lista[1][i][2]):
            got.append(lista[0][i])
    return got

def osszatlag(lista): #inp1, fel5 es fel6 / inp2, fel4 ✔
    egesz = []
    for i in range(len(lista[1])):
        osszeg = 0
        for j in range(len(lista[1][i])):
            osszeg += int(lista[1][i][j])
        egesz.append(osszeg // int(len(lista[1][i])))
    return egesz

def maxim(lista): #inp2, fel3
    egesz = []
    for i in range(len(lista[1])):
        osszeg = 0
        for j in range(2):
            osszeg += int(lista[1][i][j])
        egesz.append(osszeg // int(len(lista[1][i])))
    return egesz

# Input1 fájl
input1=read(sys.argv[1], 1)
print(maxi(input1))
print(atlag(input1))
print(osszatlag(input1))
print(osszatlag(input1)[3])

# Input2 fájl
input2=read(sys.argv[2], 1, nameloc=12)

print(osszatlag(input2)[0])