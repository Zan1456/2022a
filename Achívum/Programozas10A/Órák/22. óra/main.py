'''

import sys

filename = sys.argv[1]
file = open(filename, encoding="utf-8")
rows = file.readlines()
file.close

data = []
for i in range(len(rows)):
    data.append(rows[i].strip().split())
print(data)

lista = [[1,2,3],[4,5,6],[7,8,9]]

def Vektorkedd(matrix, oszlop):
    mondat = l[0][oszlop]
    for i in range(1, len(matrix)):
        if mondat < matrix[i][oszlop]:
            mondat = matrix[i][oszlop]
            return i

def sorösszeg(lista):
    s = 0
    for i in range(len(lista)):
        s += lista[i]
    return s
def maxsorösszeg(m):
    maxérték = sorösszeg(m[0])
    maxindex = 0
    for i in range(1, len(m)):
        if maxérték < sorösszeg(m[i]):
            maxérték = sorösszeg(m[i])
            maxindex = i
'''

def read(filename, first = 0, last = 0, cut = " ", remove = False):
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close()
    data = []
    for i in range(first, len(rows)-last):
        data.append(rows[i].strip().split(cut))
    if remove:
        names = []
        for i in range(len(data)):
            names.append(data[i][0])
            data[i].pop(0)
        return names, data
    return data

print(read("input1", 1, cut = ";", remove = True))

def maxi(lista):
    s = 0
    for i in range(len(lista)):
        s += int(lista[i])
    return s

osszeg = 0
for i in range(len(read("input1", 1, cut = ";", remove = True)[1])):
    osszeg += int(maxi(read("input1", 1, cut = ";", remove = True)[1][i]))
print(osszeg)