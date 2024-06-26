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

def cut(text, separator=" ", first=0, last=0):
    row=text.split(separator)
    numbers=process(row[first:len(row)-last])
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
in6 = process(inp6, 2, 12)
i6 = atlag(in6)
print(i6)


print("INPUT 91")
inp91 = read("input91")
in91 = cut(inp91[0])
i91 = atlag(in91)
print(i91)


print("INPUT 92")
inp92 = read("input92")
in92 = cut(inp92[0], first=1)
i92 = atlag(in92)
print(i92)


print("INPUT 93")
inp93 = read("input93")
in93 = cut(inp93[0], first=1, last=1)
i93 = atlag(in93)
print(i93)


print("INPUT 94")
inp94 = read("input94")
in94 = cut(inp94[0], first=2, last=1)
i94 = atlag(in94)
print(i94)


print("INPUT 95")
inp95 = read("input95")
in95 = cut(inp95[0], ";", 2, 1)
i95 = atlag(in95)
print(i95)