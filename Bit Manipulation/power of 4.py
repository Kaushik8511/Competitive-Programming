import  math
n = 8

def fun(n):
    if n&(n-1)==0:
        if (int(math.log2(n))+1)&1:return True
    return False

print(fun(n))
