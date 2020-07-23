num = int(input("enter a number"))

def isPrime(n):
        if n==0 or n==1:
                return False
        i=2
        while(i*i<=n):
                if n%i==0:
                        return False
                i+=1
        return True

print(isPrime(num))
