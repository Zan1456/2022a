# 1. feladat: Beolvasás
file = open("adat.txt", encoding="utf-8")
rows = file.readlines()
file.close()
data = []
for i in range(len(rows)):
    data.append(rows[i].strip().split())

# 2. feladat: Eladások
print(f"2. feladat\nA fájlban található tranzakciók (eladások) száma: {len(data)}")

# 3. feladat: Összegzés
szum = 0
for i in range(len(data)):
    szum += int(data[i][4])
print(f"3. feladat\nÖsszes eladott termék száma: {szum}")

# 4. feladat: Napi forgalom
print("4. feladat")
while True:
    number = int(input("Add meg a nap sorszámát [1...28]: "))
    if 1 <= number <= 28:
        break

f = False
for i in range(len(data)):
    if int(data[i][0]) == number:
        print(f"{data[i][1]} {data[i][2]} {data[i][3]} {data[i][4]}")
        f = True
if f == False:
    print("A megadott napon nem volt forgalma a cégnek.")

# 5. feladat: Bevételek munkatársanként
print("5. feladat")
prices = {"T1": 600, "T2": 750, "T3": 550, "T4": 650, "T5": 450}
income = {"M1": 0, "M2": 0, "M3": 0, "M4": 0, "M5": 0}
for i in range(len(data)): # Bevételek kiszámítása
    income[data[i][2]] += int(data[i][4]) * prices[data[0][3]]

for name,value in income.items(): # Bevételek kiírása
    print(f"{name}: {value} Ft")

for name,value in income.items(): # Legtöbb bevétel kiírása
    if max(income.values()) == value:
        print(f"A legtöbb bevételt az {name} kódú munkatárs generálta.")

# 6. feladat: 
print("6. feladat\nTranzakciómentes napok:")
days = {"1": False,"2": False,"3": False,"4": False,"5": False,"6": False,"7": False,"8": False,"9": False,"10": False,"11": False,"12": False,"13": False,"14": False,"15": False,"16": False,"17": False,"18": False,"19": False,"20": False,"21": False,"22": False,"23": False,"24": False,"25": False,"26": False,"27": False,"28": False}
day_names = ["hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap"]
for i in range(len(data)): #Napok behatárolása
    days[f"{data[i][0]}"] = True

for week in range(4): #Lefuttatás hetente és naponta
    without = []
    for day in range(7):
        if days[f"{(week*7)+(day+1)}"] == False:
            without.append(day)
    print(f"{week+1}. hét: ", end="")
    for j in range(len(without)):
        print(day_names[without[j]], end=" ")
    print()