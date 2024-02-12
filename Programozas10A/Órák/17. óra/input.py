def read(filename):
    file = open(filename)
    rows = file.readlines()
    file.close()
    return rows

def process(sorok, elsosor=0, a_vegerol_ennyi_sor_nem_kell=0):
    szamok=[]
    for i in range(elsosor,len(sorok)-a_vegerol_ennyi_sor_nem_kell):
        szamok.append(int(sorok[i].strip()))
    return szamok

data=read("input.txt")
numbers=process(data, 2, 2)
print(sum(numbers))