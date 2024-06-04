def strListToIntList(lista:list, start:int=0, end:int=0)->list:
    numbers = []
    for i in range(start, len(lista)-end):
        numbers.append(int(lista[i].strip()))
    return numbers


file = open("input3.txt", "r", encoding="utf-8")
rows = file.readlines()
file.close()
print(rows)

num = rows[0].split(" ")
print(num)
print(strListToIntList(num))
