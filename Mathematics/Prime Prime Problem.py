n = 10
p = [True for i in range(n+1)]
pp = [0 for i in range(n+1)]
l=3
r=5
def PPP(n):
        p[0]=False
        p[1]=False
        i=2
        while(i*i<=n):
                if p[i]:
                        j=i*i
                        while(j<=n):
                                p[j]=False
                                j+=i
                i+=1
        ct = 0
        temp = 0
        for i in range(1,len(pp)):
                ct += p[i]
                if p[i] and p[ct]:
                        temp+=1
                pp[i]=temp
                

PPP(n)
print(pp[r]-pp[l])

