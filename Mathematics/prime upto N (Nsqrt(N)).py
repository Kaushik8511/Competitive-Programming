n = 1000000
prime = []

def rangePrime(n):
        for i in range(2,n+1):
                j = 2
                flag = True
                while(j*j<=i and flag):
                        if i%j==0:
                                flag=False
                        j+=1
                if flag:
                        prime.append(i)

rangePrime(n)
                
        
