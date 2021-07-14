fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]

def ncr(n,r):
    if n==r:return 1
    res = fact[n]//fact[r]
    res//=fact[n-r]
    return res
    

def solve(n,p):
    per_table = p//n
    rem = p%n
    res = 1
    for i in range(n):
        total = 0
        if rem:
            total+=1
            rem-=1
        total += per_table
        res*=ncr(p,total)
        p-=total
    return res

tables,people = map(int,input().split())
print(solve(tables,people))
