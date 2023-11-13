def fejlec(cim):
    szelesseg = 30
    csillagok = "*"*szelesseg
    kozepso_csillag = "*"*((szelesseg-len(cim))//2)
    print(csillagok)
    if len(cim) % 2 == 0:
        print(kozepso_csillag+cim+kozepso_csillag)
    else:
        print(kozepso_csillag+cim+kozepso_csillag+"*")
    print(csillagok)
teszt=""
for i in range(2,20):
    teszt+="C"
    fejlec(teszt)