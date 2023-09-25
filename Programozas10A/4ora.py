import random
# 1. feladat
Elso = []
Masodik = []
Harmadik = []
Negyedik = []

for _ in range(7):
    Elso.append(random.randint(0, 9))
    Masodik.append(random.randint(0, 9))
    Harmadik.append(random.randint(0, 9))
    Negyedik.append(random.randint(0, 9))

# 2. feladat
sale = 0
for i in range(len(Elso)):
    sale = sale + Elso[i]
for i in range(len(Masodik)):
    sale = sale + Masodik[i]
for i in range(len(Harmadik)):
    sale = sale + Harmadik[i]
for i in range(len(Negyedik)):
    sale = sale + Negyedik[i]
print(sale)

# 3. feladat
A = sum(Elso)
B = sum(Masodik)
C = sum(Harmadik)
D = sum(Negyedik)
print(A)
print(B)
print(C)
print(D)

# 4. feladat
x = 0
if all(x >= 2 for x in (A, B, C, D)):
    if A == max(A, B, C, D):
        print("1. hét a legjobb")
    if B == max(A, B, C, D):
        print("2. hét a legjobb")
    if C == max(A, B, C, D):
        print("3. hét a legjobb")
    if D == max(A, B, C, D):
        print("4. hét a legjobb")

# 5. feladat
NullaEladas = 0
for i in range(len(Elso)):
    if Elso[i] == 0:
        NullaEladas += 1
for i in range(len(Masodik)):
    if Masodik[i] == 0:
        NullaEladas += 1
for i in range(len(Harmadik)):
    if Harmadik[i] == 0:
        NullaEladas += 1
for i in range(len(Negyedik)):
    if Negyedik[i] == 0:
        NullaEladas += 1
print("A héten", NullaEladas, "nap volt nulla eladás")

# 6. feladat
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0
Paratlanok = []
def minS():
    odds = []
    for i in Paratlanok:
        if i % 2 != 0:
            odds.append(i)
    return min(odds)

E += Elso[0]
E += Masodik[0]
E += Harmadik[0]
E += Negyedik[0]

F += Elso[1]
F += Masodik[1]
F += Harmadik[1]
F += Negyedik[1]

G += Elso[2]
G += Masodik[2]
G += Harmadik[2]
G += Negyedik[2]

H += Elso[3]
H += Masodik[3]
H += Harmadik[3]
H += Negyedik[3]

I += Elso[4]
I += Masodik[4]
I += Harmadik[4]
I += Negyedik[4]

J += Elso[5]
J += Masodik[5]
J += Harmadik[5]
J += Negyedik[5]

K += Elso[6]
K += Masodik[6]
K += Harmadik[6]
K += Negyedik[6]
Paratlanok.append(E)
Paratlanok.append(F)
Paratlanok.append(G)
Paratlanok.append(H)
Paratlanok.append(I)
Paratlanok.append(J)
Paratlanok.append(K)
if minS() == E:
    print("A hétfő volt a legrosszabb")
if minS() == F:
    print("A kedd volt a legrosszabb")
if minS() == G:
    print("A szerda volt a legrosszabb")
if minS() == H:
    print("A csütörtök volt a legrosszabb")
if minS() == I:
    print("A péntek volt a legrosszabb")
if minS() == J:
    print("A szombat volt a legrosszabb")
if minS() == K:
    print("A vasárnap volt a legrosszabb")