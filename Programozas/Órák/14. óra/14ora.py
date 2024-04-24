def f(x:int, y:int)->int:
    """
        f(x, y)=3x+2y
    """
    return 3*x+2*y

print(f(3, 2))
print(f(y=4, x=233))

#
def ki(x:any):
    print(x)
    return

if print("valami")==None:
    print("None-val tért vissza")

x=ki("géza")
print(x)
if x==None:
    print("nem volt visszatérési érték.")

#
import math

class A_NULLA(Expection):
    pass
class DISZKRIMINANS_KISEBB_NULLANAL(Expection):
    pass

def masodfoku(a:float, b:float, c:float):
    """
        Másodfokú megoldóképlet
        Ha a = 0: A_NULLA hiba
        Ha a diszkrimináns < 0: DISZKRIMINANS_KISEBB_NULLANAL
        return int: 1 zérushely
        return tuple: 2 zéruhely
    """
    if a == 0:
        raise A_NULLA
    d=b**2-4*a*c
    if d < 0:
        raise DISZKRIMINANS_KISEBB_NULLANAL
    if d == 0:
        return (-b+ math.sqrt(d))/(2*a)
    
    x1 = (-b+ math.sqrt(d))/(2*a)
    x2 = (-b- math.sqrt(d))/(2*a)
    return x1, x2

try:
    x = masodfoku(0, 1, 2)
except A_NULLA:
    print("Az 'a' értéke nulla.")
except DISZKRIMINANS_KISEBB_NULLANAL:
    print("A diszkrimináns kisebb nullánál.")