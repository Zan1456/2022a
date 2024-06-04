import random
# 1. feladat
kokuszgolyo = {"het1": [], "het2": [], "het3": [], "het4": []}

def feltolt(lista, nev):
    for _ in range(7):
        lista[nev].append(random.randint(0, 9))

    #[lista.append(random.randint(0, 9)) for _ in range(7)]

# 2. feladat
def eladas(lista):
    return sum(lista.values())

# 3. feladat

# 4. feladat

# 5. feladat

# 6. feladat

feltolt(kokuszgolyo, "het1")
feltolt(kokuszgolyo, "het2")
feltolt(kokuszgolyo, "het3")
feltolt(kokuszgolyo, "het4")