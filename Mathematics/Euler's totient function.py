n = 6

def fun(n):
    res,i = n,2
    while i*i<=n:
        if n%i==0:
            while n%i==0:
                n//=i
            res*=(1-1/float(i))
        i+=1
    if n!=1:res*=(1-1/float(n))
    return int(res)

print(fun(n))
