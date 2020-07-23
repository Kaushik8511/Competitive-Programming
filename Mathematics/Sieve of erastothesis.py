num = 1253238
prime = [True for i in range(num+1)]

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

sieve(num)
ct=0
for i in range(len(prime)):
        if prime[i]:
                ct+=1

                
print(ct)
