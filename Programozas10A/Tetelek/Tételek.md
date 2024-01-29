# Programozási tételek

> Frissítve 2024.01.22. 19:00

## Összegzés tétele

- Elemek száma: N
- Számok: X N db elem
- Változó: S (Tárolja az összeget)

```Python
S := 0
Ciklus I=1-től N-ig
    S:=S+X[I]
Ciklus vége
```

![asd](osszegzes.png)

## Megszámlálás

- Elemek száma: N
- Számok: X N db elem
- Változó: C (Tárolja, hogy hány db-ra igaz a T feltétel)
- T: Igaz/Hamis értékű feltétel

```Python
C:=0
Ciklus I=1-től N-ig
    Ha T(X[I])
        C:=C+1
Ciklus vége
```

![asd](megszamlalas.png)

## Legnagyobb érték

- Elemek száma: N
- Számok: X N db elem
- MAX: Legnagyobb érték indexe
- MAXERT: Legnagyobb érték

```Python
MAX := 1
MAXERT := X[1]
Ciklus I=2-től N-ig
    Ha MAXERT<X[I]
        MAX := I
        MAXERT := X[I]
    Elágazás vége
Ciklus vége
```

![kep](legnagyobb.png)

## Keresés

- Elemek száma: N
- Számok: X N db elem
- VAN: változó I/H értékkel
- T: Hamis értékű változó

```Python
I:=1
Ciklus I≤N és nem T(X[I])
    I:=I+1
Ciklus vége
VAN:=(I≤N)
Ha VAN
    SORSZ:=I
```

![kep](kereses.png)

## Eldöntés

- Elemek száma: N
- Számok: X N db elem
- VAN: változó I/H értékkel
- T: Hamis értékű változó

```Python
I := 1
Ciklus I <= N és nem T(x[i])
    I := I + 1
Ciklus vége
VAN := I <= N
```

![asd](eldontes.png)

## Kiválasztás

- Számok: X N db elem
- VAN: változó I/H értékkel
- T: Hamis értékű változó

```Python
I := 1
Ciklus amíg nem T(X[I])
    I := I + 1
Ciklus vége
SORSZ := I
ÉRTÉK := x[i]
```

![asd](kivalasztas.png)

[Forrás](http://progalap.elte.hu/downloads/seged/eTananyag/lecke13_lap1.html)
