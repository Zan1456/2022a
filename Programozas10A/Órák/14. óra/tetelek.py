def osszegzes_tetel(l:list)->int:
    """
        Összegzés programozási tétel
        return elemek összege
    """
    szum = 0
    for i in range(len(l)):
        szum += l[i]
    return szum

def megszámlálás(l:list)->int:
    """
        Megszámlálás programozási tétel
        return feltételre igaz elemeknek a száma
    """
    count = 0
    for i in range(len(l)):
        if l[i] == 0:
            count += 1
    return count

def legnagyobb_ertek(l:list)->tuple:
    """
        Legnagyobb érték programozási tétel
        return a listában található legnagyobb érték
    """
    max = 0
    maxert = l[0]
    for i in range(len(l)-1):
        if l[i+1] > maxert:
            max = i
            maxert = l[i]
    return max, maxert

def keresés(l:list):
    """
        Keresés programozási tétel
        return a feltételre igaz elem van e a listában és ha van, akkor hol
    """
    for i in range(len(l)):
        if l[i] == 0:
            return True, i
    return False

def eldöntés(l:list)->bool:
    """
        Eldöntés programozási tétel
        return a feltételre igaz elem van e a listában
    """
    for i in range(len(l)):
        if l[i] == 0:
            return True
    return False

def kiválasztás(l:list)->int:
    """
        Eldöntés programozási tétel
        return a feltételre igaz elem hol van és milyen értékkel rendelkezik
    """
    for i in range(len(l)):
        if l[i] == 0:
            return l[i], i