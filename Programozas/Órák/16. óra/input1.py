file = open("input.txt", "r", encoding="utf-8")
rows = file.readlines()
file.close()

numbers = []
for i in range(1, len(rows)):
    numbers.append(int(rows[i].strip()))

szum = 0
for i in range(len(numbers)):
    szum += numbers[i]
print(szum)