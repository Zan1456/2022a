import random

# 1. feladat 
ismetles = True
jegyek = []
while ismetles: # Adatok bekérése
    jegy = input("Add meg a diák jegyét [0...100]: ")
    if jegy == "vége":
        ismetles = False
    elif 0 <= int(jegy) <= 100:
        jegyek.append(int(jegy))
    else:
        print("Hibás adatbevitel!")

legrosszabb = 101
legjobb = -1
for i in range(len(jegyek)): # Legjobb és legrosszabb meghatározása
    if jegyek[i] < legrosszabb:
        legrosszabb = jegyek[i]
    if jegyek[i] > legjobb:
        legjobb = jegyek[i]

print(f"Legjobb jegy: {legjobb}")
print(f"Legrosszabb jegy: {legrosszabb}")
# 2. feladat
minimum = -1
maximum = -1
while not 100 >= minimum >= 0 or not 100 >= maximum >= 0:
    minimum = int(input("Add meg a legkisebb értéket, amit látni szeretnél: "))
    maximum = int(input("Add meg a legnagyobb értéket, amit látni szeretnél: "))

megfelelo = []
megfelel = 0
for i in range(len(jegyek)):
    if maximum >= jegyek[i] >= minimum:
        megfelelo.append(jegyek[i])
        megfelel += 1

print(f"Az intervallumon belül {megfelel} db jegy van ezek:", end=" ")
for i in range(len(megfelelo)):
    print(megfelelo[i], end=" ")
print()

# 3. feladat
osszeg = 0
for i in range(len(jegyek)):
    osszeg += jegyek[i]
atlag = osszeg / len(jegyek)
print(f"Az osztályátlag: {atlag}")

# 4. feladat
jegyek2 = []
for i in range(len(jegyek)):
    jegyek2.append(random.randint(0, 100))
osszeg2 = 0
for i in range(len(jegyek2)):
    osszeg += jegyek2[i]
atlag2 = osszeg2 / len(jegyek2)
if atlag > atlag2:
    print("Az első osztály átlaga a nagyobb.")
elif atlag < atlag2:
    print("A második osztály átlaga a nagyobb.")
else:
    print("A két oszátly átlaga egyenlő.")