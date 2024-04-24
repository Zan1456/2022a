# 20. óra, 2024.03.18. 10:00-11:45

## Végrehajtás

```Powershell
PS C:\...\20. óra> & C:/.../python.exe C:/.../main.py
```

## Mappa tartalmának kiírása

```Powershell
dir
```

## Mappák közötti navigálás

```Powershell
cd C:\Users\local\Desktop\Ozsváth Csanád 10A\2022a\Programozas10A\Órák\20. óra
```

## Python fájl futtatása

```Powershell
py main.py
```

## Adatok kivétele a py argument után

```Powershell
py main.py Géza
```

```Python
import sys
print("Hello ", end="")
print(sys.argv[1])
```

## Fájl beolvasás

```Powershell
py main.py name.txt
```

```Python
import sys
import os
if len(sys.argv) <= 1:
    print("Nem érkezett adat!")
    print("Usage: py filename.py filename.txt")
elif os.path.exists(sys.argv[1]):
    filename = sys.argv[1]
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close
    for i in range(len(rows)):
        print(f"Hello {rows[i]}")
else:
    print("Nem létezik ilyen fájl.")
```
