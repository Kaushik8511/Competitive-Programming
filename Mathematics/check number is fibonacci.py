import math
n = 12

def perfectSquare(n):
    if n<0:return False
    x = int(math.sqrt(n))
    return x*x==n

def fun(n):
    return perfectSquare(5*(n**2)+4)or perfectSquare(5*(n**2)-4)

print(fun(n))
    
