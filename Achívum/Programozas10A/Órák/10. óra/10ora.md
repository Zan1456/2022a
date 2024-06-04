# 10. óra 2023.12.04

## Műveletek billentyűkombinációi

- & - Alt Gr + C
- | - Alt Gr + W
- ^ - Alt Gr + 3
- ~ - Alt Gr + 1

## Műveletek használatban

```Python
x = 4
y = 1

a = x & y # and / és
b = x | y # or / vagy
c = ~x  # not / nem (Trükkös)
d = x ^ 5 # xor / tagadó vagy
e = x >> 2 # right shift - Jobbra tolás
f = x << 2 # left shift - Balra tolás

print(a, b, c, d, e, f)
```

> [Advent of code](https://adventofcode.com/2023)

## Lista műveletek

```Python
l1 = [2,3,4]
l1.append(6) # [2,3,4,6]
print(l1[1]) # 3
print(len(l1)) # 4
l1[2] = 10 # [2, 3, 10, 6]
del l1[2] # [2, 3, 6]
print(l1[-1]) # 6
print(l1[-2]) # 3
l1.insert(0, 222) # [222, 2, 3, 6]

# ?
l1 = [2, 3, 4]
l2 = l1
l1[1] = 10
print(l2)

# ?
l1 = [2, 3, 4]
l2 = l1[:]
l1[1] = 10
print(l2)

# ?
l1 = [2, 3, 4, 6, 12, 28]
print(l1[1:3]) # [3, 4]
print(l1[4:]) # [12, 28]
print(l1[:2]) # [2, 3]
print(l1[::3]) # [2, 6]

l2 = [2,3]
del l2
print(l2)

if 3 in l1: # True
    print()
if 120 in l1: # False
    print()
```

## Fájból olvasás

```Python
filename = "input.txt"
f = open(filename, "r") # Read
sorok = f.readlines()
f.close
print(sorok)

for i in range(len(sorok)):
    sorok[i]=sorok[i].strip()
print(sorok[0])
sum = int(sorok[1])+(int(sorok[2]))
print(sum)
```

## Érdekes
```Python
my_list = [1, 2, "in", True, "ABC"]

print(1 ??? my_list)  # outputs True
print("A" ??? my_list)  # outputs True
print(3 ??? my_list)  # outputs True
print(False ??? my_list)  # outputs False

my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False
```