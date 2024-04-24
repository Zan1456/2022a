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

def szum(lista):
    mszum = []
    for i in range(len(lista)):
        szum = 0
        for j in range(len(lista[i])):
            szum += int(lista[i][j])
        mszum.append(szum)
    return mszum
        

print(read("input1"))
print(read("input2", 1))
print(read("input3", 1, 1))
print(read("input4", 1, cut = ";", remove = True))

print(szum(read("input1")))
print(szum(read("input2", 1)))
print(szum(read("input3", 1, 1)))

