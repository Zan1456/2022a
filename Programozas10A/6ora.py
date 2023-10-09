'''
# Kérj be egy számot és ellenőrizd le, hogy páros-e vagy sem.
szam=int(input("Adj meg egy számot: "))

if szam%2==0:
    print("Páros szám")
else:
    print("páratlan szám")
'''

# Kérj be egy szót és ellenőrizd, hogy van-e benne a betű.
str="körte"
N=len(str)
i = 0
while i < N and not str[i] == "a":
    i=i+1
van=i<N