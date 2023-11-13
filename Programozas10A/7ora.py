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

x=43
# 16-os számrendszerbe váltás
y="0x"+x