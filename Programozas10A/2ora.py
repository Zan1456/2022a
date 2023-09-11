szamok = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # Elfogadott karakterek
ism = True
'''while ism == True:
    ism = False
    szam=str(input("Adj meg egy számot: ")) # Szám bekérés
    for i in szam:
        if not i in szamok:
            ism = True #Ez akkor fut le, ha van olyan karakter, ami nem jó.
'''
while True:
    szam=input("Adj meg egy számot: ")
    if szam.isdecimal():
        break

if int(szam) % 2 == 0: #Ellenőrzi, hogy a szám páros vagy páratlan
    print("Páros")
else:
    print("Páratlan")