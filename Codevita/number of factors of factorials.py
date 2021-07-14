def sieve(n):
    dp = [True for i in range(n+1)]
    i=2
    while i*i<=n:
        if dp[i]:
            for j in range(i*i,n+1,i):dp[j]=False
        i+=1
    return dp

def exp(n,k):
    ret,div = 0,k
    while n//div:
        ret+=(n//div)
        div*=k
    return ret
             


def solve(n):
    if n<2:return 1
    prime = sieve(n)
    res = []
    for i in range(2,n+1):
        if prime[i]:res.append(exp(n,i))
    ret = 1
    for i in res:ret*=(i+1)
    return ret


try:
    n = int(input())
    if n<0:raise Exception()
    print(solve(n))
except:print("invalid input")
