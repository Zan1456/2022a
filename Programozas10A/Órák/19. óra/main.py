def read(filename):
    file = open(filename, encoding="utf-8")
    rows = file.readlines()
    file.close()
    return rows

def process(rows, first = 0, last = 0):
    numbers=[]
    for i in range(first,len(rows)-last):
        numbers.append(int(rows[i].strip()))
    return numbers

def atlag(numbers):
    szum = 0
    for i in range(len(numbers)):
        szum += numbers[i]
    return szum // len(numbers)

print("INPUT 1")
inp1 = read("input1")
in1 = process(inp1)
i1 = atlag(in1)
print(i1)


print("INPUT 2")
inp2 = read("input2")
in2 = process(inp2, 2, 1)
i2 = atlag(in2)
print(i2)


print("INPUT 3")
inp3 = read("input3")
in3 = process(inp3, 1, 1)
i3 = atlag(in3)
print(i3)


print("INPUT 4")
inp4 = read("input4")
in4 = process(inp4)
i4 = atlag(in4)
print(i4)


print("INPUT 5")
inp5 = read("input5")
in5 = process(inp5, 2, 1)
i5 = atlag(in5)
print(i5)


print("INPUT 6")
inp6 = read("input6")
inp6 = read("input6")
in6 = process(inp6, 2, 12)
i6 = atlag(in6)
print(i6)