'''
def fejlec(cim):
    szelesseg = 30
    csillagok = "*"*szelesseg
    kozepso_csillag = "*"*(((szelesseg-len(cim))//2)-1)
    print(csillagok)
    if len(cim) % 2 == 0:
        print(kozepso_csillag+" "+cim+" "+kozepso_csillag)
    else:
        print(kozepso_csillag+" "+cim+" "+kozepso_csillag+"*")
    print(csillagok)
teszt=""
for i in range(2,20):
    teszt+="C"
    fejlec(teszt)
'''
x=11_222_231
print(x+1)

print(0o123) #8-as számrendszer
print(0xABBA) #16-os számrendszer
print(0b11000000) #2-es számrendszer

x = int("345", 8) # Átváltás 10-es számrendszerbe
print(x)

x = oct(321) # Átváltás 8-as számrendszerbe
print(x)

x = hex(40096) # Átváltás 16-os számrendszerbe
print(x)

x = bin(192) # Átváltás 2-es számrendszerbe
print(x)

x = 1e-08 # 10 8. hatványára való emelés

str = 'Anya azt mondta, hogy: "Érj haza időben"'
print(str)
str = "Anya azt mondta, hogy: \"Érj haza időben\""

print(9 % 6 % 2)
a = 1
A = 2
print(a, A) # 1, 2

def abba():
    print("asd")
abba = "sss"
print(abba)
print(abba())