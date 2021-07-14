def sieve(n):
    dp = [True for i in range(n+1)]
    dp[0]=dp[1]=False
    i=2
    while i*i<=n:
        if dp[i]:
            for j in range(i*i,n+1,i):dp[j]=False
        i+=1

    #print primes
    for i in range(n+1):
        if dp[i]:print(i,end=" ")


sieve(20)
