import sys
import os
## Adatok kivétele a py argument után
'''
print("Hello ", end="")
print(sys.argv[1])
'''

## Fájl beolvasás
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