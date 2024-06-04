import random

#
while True:
    érték = int(input("Add meg a lista hosszát [3..25]: "))
    if 3 <= érték <= 25:
        break
    print("Hibás bemenet, próbáld újra!")

#
számok = []
for i in range(érték):
    számok.append(random.randint(-10, 10))
print("Lista tartalma:", számok)

#
összeg = 0
for i in range(len(számok)):
    összeg += számok[i]
print("A lista összege:", összeg)

#
nulla = 0
negatív = 0
for i in range(len(számok)):
    if számok[i] == 0:
        nulla += 1
    elif számok[i] < 0:
        negatív += 1
print(f"Negatív számok: {negatív}")
print(f"Nullák száma: {nulla}")
if nulla > negatív:
    print("Igaz állítás")
elif nulla <= negatív:
    print("Hamis állítás")