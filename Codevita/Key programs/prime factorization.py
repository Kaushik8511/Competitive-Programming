def prime_fact(n):
    if n<2:return []
    res = []
    i=2
    while i*i<=n:
        if n%i==0:
            while n%i==0:n//=i
            res.append(i)
        i+=1
    if n>1:res.append(n)
    return res

print(prime_fact(42543542))
