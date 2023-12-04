l = []
for i in range(10):
    l.append(i**2)
print(l)

l = [i ** 2 for i in range(10)]
l = [
    [2,3,3,4],
    [3,4,5,8],
    [3,4,5,6,6]
]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])