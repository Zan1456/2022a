def count(lista:list, condition)->int:
    c = 0
    for i in range(len(lista)):
        if condition(lista[i]):
            c += 1
    return c

print(count([1, 2, 3, 4, 5], lambda num: num %2 == 0))


def count(lista, condition): return sum(1 for i in range(len(lista)) if condition(lista[i]))
print(count([1, 2, 3, 4, 5], lambda num: num %2 == 0))

def maximum(lista, condition):
    index = 0
    maxi = lista[0]
    for i in range(len(lista)):
        if condition(lista[i], maxi):
            index = i
            maxi = lista[i]
    return index, maxi

print(maximum([1, 3, 78, 9, 6], lambda num1, num2:  num1 < num2))


##

osszeadas = lambda num1, num2: num1 + num2

print(osszeadas(1, 4))