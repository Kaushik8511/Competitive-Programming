num = 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18
d = {}

def PrimeFact(n):
        i=2
        while(i*i<=n):
                ct = 0
                while (n%i==0):
                        ct+=1
                        n//=i
                if ct>0:
                        d[i]=ct
                i+=1
        if n>1:
                d[n]=1

PrimeFact(num)
for i,j in d.items():
        while j!=0:
                print(i,end="*")
                j-=1
