# Programozás óra 2. óra 2023.09.11.

## címsor 2

### címsor 3

- első
- második
- harmadik

1. első
1. második
1. harmadik

```python
while True:
    szam=input("Adj meg egy számot: ")
    if szam.isdecimal():
        break

if int(szam) % 2 == 0:
    print("Páros")
else:
    print("Páratlan")
```