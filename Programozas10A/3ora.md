# Programozás óra 3. óra 2023.09.18

## Egyszerű függvény

```Python
def Kiir(srt):
    print(srt)

def g_fv(x, y, z):
    return(x*x+y+z/2)

x=g_fv(5,3,4)
Kiir(x)
```

### Lista összegzés függvény

```Python
def lista_osszeg(lista):
    x = 0
    for i in range(len(lista)):
        x = lista[i] + x
    return x

l1 = [1, 3, 5, 7]
l2 = [7, 2, 9]
l3 = [6, 3, 0, 4]
print(lista_osszeg(l1))
print(lista_osszeg(l2))
print(lista_osszeg(l3))
```

### Lista átlag függvény

```Python
def lista_atlag(lista):
    x = 0
    for i in range(len(lista)):
        x = lista[i] + x
    x = x/len(lista)
    return x

l1 = [1, 3, 5, 7]
l2 = [7, 2, 9]
l3 = [6, 3, 0, 4]
print(lista_atlag(l1))
print(lista_atlag(l2))
print(lista_atlag(l3))
```

### A két függvény összevonása

```Python
def lista_osszeg(lista):
    x = 0
    for i in range(len(lista)):
        x = lista[i] + x
    return x

def lista_atlag(lista):
    x = lista_osszeg(lista)
    return x/len(lista)

l1 = [1, 3, 5, 7]
l2 = [7, 2, 9]
l3 = [6, 3, 0, 4]
print(lista_osszeg(l1))
print(lista_osszeg(l2))
print(lista_osszeg(l3))
```

### Egyszerű számológép

```Python
def szam():
    return (int(input("Adj meg egy számot: ")))

print("1. összeadás\n2. kivonás\n3. átlag")
tipus = input("Menüpontod: ")
if tipus == '1':
    print(szam()+szam())
elif tipus == '2':
    print(szam()-szam())
else:
    x=szam()+szam()
    print(x/2)
```
### Lista
```Python
gy=["Alma", "Citrom", "Barack", "Pomelo"]
gy[0] #Alma
gy[-1] #Pomelo
gy[1:3] #Citrom, Barack
gy[2:] #Barack, Pomelo
gy[] #Alma, Citrom, Barack, Pomelo
```
### Lista nagy
```Python
gy=["Alma", "Citrom", "Barack", "Pomelo"]
def nagybetus(lista):
    for i in range(len(lista)):
        lista[i]=lista[i].upper()
    return lista
print(gy)
print(nagybetus(gy[:]))
print(gy)
print(nagybetus(gy))
print(gy)
```
### Mappák
```Python
d1={}
d2=dict()
d3={"nev": "dobostorata",
    "szeletek": "12",
    "elfogyott": "Igen"
    }
print(d3["szeletek"])
```