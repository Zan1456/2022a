'''
# Kérj be egy számot és ellenőrizd le, hogy páros-e vagy sem.
szam=int(input("Adj meg egy számot: "))

if szam%2==0:
    print("Páros szám")
else:
    print("páratlan szám")
'''

'''
# Kérj be egy szót és ellenőrizd, hogy van-e benne a betű.
str="körte"
N=len(str)
i = 0
while i < N and not str[i] == "a":
    i=i+1
van=i<N
'''

'''
# Ellenőrizd, hogy a sztring egy vagy több mondatból áll.
mondat = "Ez egy példa mondat. Illetve ez is egy mondat."
N = len(mondat)
Mszam = 0
i = 0
while i < N:
    if "." == (mondat[i]) or "!" == (mondat[i]) or "?" == (mondat[i]):
        Mszam = Mszam + 1
    i += 1
if Mszam > 1:
    print("Több mondatból áll")
else:
    print("Nem áll több mondatból")
'''

# Hogy hívták az első nőt, aki megérkezet
lista = [
    ["Béla", "f", "18:00"],
    ["Judit", "n", "18:01"],
    ["Zoli", "f", "18:05"],
    ["Mari", "n", "18:15"]
]
i = 0

while not lista[i][1] == "n":
    i += 1
print(lista[i][0])


'''
for i in range(len(lista)):
    egysor=""
    for j in range(len(lista[i])):
        egysor += lista[i][j]+ " "
    print(egysor)
'''