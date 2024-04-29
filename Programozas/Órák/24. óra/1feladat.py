import random

#
while True:
    érték = int(input("Add meg a lista hosszát [10..20]: "))
    if 10 <= érték <= 20:
        break
    print("Hibás bemenet, próbáld újra!")

#
elemek = []
for i in range(érték):
    elemek.append(random.randint(1, 5))
print("Lista tartalma:", elemek)

#
összeg = 0
for i in range(len(elemek)):
    összeg += elemek[i]
print("A lista összege:", összeg)

#
i = len(elemek)-1
index = 0
ért = elemek[i]
while i > 0:
    i -= 1
    if érték < elemek[i]:
        érték = elemek[i]
        index = i

print(f"A listában lévő legnagyobb szám a(z) {ért}, helye {index}. index")
