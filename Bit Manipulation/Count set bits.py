n = 15

def fun(n):
    count=0
    while n:
        count+=(n&1)
        n=n>>1
    return count

print(fun(n))
        
