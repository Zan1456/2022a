# x=input("x=")
# input("y=")

x = "ha"*3

x = 3 == 2
print(x)

x = 3 != 2
print(x)

x = 3
if x == 3:
    print("Az x értéke 3")
elif x<3:
    print("Az x értéke kisebb 3")
else:
    print("egyik feltétel sem igaz")

x = 5
feltetel = True
while feltetel:
    print("ciklusmag")
    if x == 7:
        feltetel = False
    x += 1
print(x)

i = 1
while not True:
    print(i)
    i += 1

while not True:
    pass

for i in range(10):
    pass # 0-9

# break
# continue

x = "szia"
for i in x:
    print(i)

x = 5
while x < 4:
    pass
else:
    print("Nem lépett be a ciklusba.")

ijk = 7
for ijk in range(12,10):
    print(ijk)
else:
    print("else ág", ijk)

x = 3
y = 6
print(x > y)
print(not x <= y)
print(True and True)
print(True and False)
print(True and False and True)
print(True or False or True)
print(True or False or False)

print( 1 and 0 )
print( 1 and 1 )
print( (1 and 1) and (1 and 1))
print( (1 and 1) and (1 and 0))
print( (1 or 1) or (1 or 1))
print( (1 or 1) or (1 or 0))
print( (1 or 0) or (1 or 0))
print( (1 or 0) or (0 or 0))