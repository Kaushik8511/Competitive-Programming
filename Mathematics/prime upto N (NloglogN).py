n = 1000000
prime = [True for i in range(n+1)]

def sieve(n):
        prime[0]=False
        prime[1]=False
        i=2
        while(i*i<=n):
                if prime[i]:
                        j=i*i
                        while(j<=n):
                                prime[j]=False
                                j+=i
                i+=1

sieve(n)
p=[]
for i in range(len(prime)):
        if prime[i]:
                p.append(i)

