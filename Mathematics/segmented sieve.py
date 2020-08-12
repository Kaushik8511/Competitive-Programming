import math
def sieve(n):
    dp = [True for _ in range(n+1)]
    i=2
    while i*i<=n:
        if dp[i]:
            for j in range(i*i,n+1,i):
                dp[j]=False
        i+=1

    prime=[]
    for i in range(2,n+1):
        if dp[i]:prime.append(i)
    return prime

def segmentSieve(l,r,prime):
    dp = [True for i in range(r-l+1)]

    i=0
    while prime[i]*prime[i]<=r:
        curr = prime[i]
        start = (l//curr)*curr
        if start<l:start=start+curr
        for j in range(start,r+1,curr):
            dp[j-l]=False
        if start==curr:dp[start-l]=True
        i+=1
    for i in range(r-l+1):
        if dp[i]:print(l+i,end=" ")
        
        

l = int(input("enter left "))
r = int(input("enter right "))
prime = sieve(10**6)
segmentSieve(l,r,prime)
