def Read(filename):
    file = open(filename, "r", encoding="utf-8")
    rows = file.readlines()
    file.close()
    return rows

def strListToIntList(lista:list, start:int=0, end:int=0)->list:
    """
    - Lefut a listán
    - Kiveszi a /n végződést
    - Intigerré alakítja
    """
    numbers = []
    for i in range(start, len(lista)-end):
        numbers.append(int(lista[i].strip()))
    return numbers
