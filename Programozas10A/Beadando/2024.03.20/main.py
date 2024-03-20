# 1. feladat: Beolvasás
def read(filename): #Beolvasás
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close()
    return rows

def process(rows, first = 0, last = 0): #Adatok javítása
    numbers=[]
    for i in range(first,len(rows)-last):
        numbers.append(rows[i].strip())
    return numbers

def cut(text, separator=" ", first=0, last=0): #Adatok szeparálása
    row=text.split(separator)
    numbers=process(row[first:len(row)-last])
    return numbers

data = process(read("adat.txt"))
cutted = []
for i in range(len(data)):
    cutted.append(cut(data[i]))

# 2. feladat: Eladások
print(f"2. feladat\nA fájlban található tranzakciók (eladások) száma: {len(cutted)}")

# 3. feladat: Összegzés
szum = 0
for i in range(len(cutted)):
    szum += int(cutted[i][4])
print(f"3. feladat\nÖsszes eladott termék száma: {szum}")

# 4. feladat: Napi forgalom
while True:
    szam = int(input("Add meg a nap sorszámát [1...28]: "))
    if 1 <= szam <= 28:
        break

igaz = False
for i in range(len(cutted)):
    if int(cutted[i][0]) == szam:
        print(f"{cutted[i][1]} {cutted[i][2]} {cutted[i][3]} {cutted[i][4]}")
        igaz = True
if igaz == False:
    print("A megadott napon nem volt forgalma a cégnek.")

# 5. feladat: Bevételek munkatársanként
M1 = 0
M2 = 0
M3 = 0
M4 = 0
for i in range(len(cutted)):
    if cutted[i][2] == "M1":
        M1 += int(cutted[i][4])
    elif cutted[i][2] == "M2":
        M2 += int(cutted[i][4])
    elif cutted[i][2] == "M3":
        M3 += int(cutted[i][4])
    else:
        M4 += int(cutted[i][4])





# 6. feladat: 
hetek = []
napok = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
for i in range(len(cutted)):
    het = []
    for j in range(28):
        if not j+1 == int(cutted[j][0]):
            het.append(j)
            break
    hetek.append(het)
print(hetek)